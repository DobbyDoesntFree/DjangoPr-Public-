from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import *
from .models import Amenity, Room
from categories.models import Category
from .serializers import AmenitySerializer, RoomListserializer, RoomDetailSerializer


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            new_amenity = serializer.save()
            return Response(AmenitySerializer(new_amenity).data)
        else:
            return Response(serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            amenity = Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound
        return amenity

    def get(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(amenity, data=request.data, partial=True)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListserializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:  # 0. 로그인 유무 확인 후
            serializer = RoomDetailSerializer(data=request.data)  # 1. 사용자 입력 데이터 받아옴
            if serializer.is_valid():  # 2. 데이터 유효성 검증 (1차 - 모델 양식)
                category_pk = request.data.get(
                    "category"
                )  # 3. 데이터 유효성 검증 (2차 - 카테고리 값 유무)
                if not category_pk:
                    raise ParseError("Category is mandatory")
                try:  # 4. 데이터 유효성 검증 (3차 - 카테고리 값이 room에 맞는가?)
                    category = Category.objects.get(pk=category_pk)
                    if category.kind != Category.CategoryKindChoices.ROOMS:
                        raise ParseError("Category dosen't match for room")
                except Category.DoesNotExist:
                    raise ParseError(
                        "Category data dosen't exists. Maybe wrong category id?"
                    )
                # 5. 데이터 저장 (login 상태이며, 카테고리 값이 적절)
                try:
                    with transaction.atomic():
                        # with 이하에서 error 발생 시 값이 db에 저장되지 "않음"
                        # with 안에서 try except 사용하지 않음
                        # 사용 시 except에 걸리는 error 발생하더라도 error로 간주하지 않아 db에 저장됨
                        room = serializer.save(
                            owner=request.user,
                            category=category,
                        )  # amenity 포함된 input이라도 여기에 없어서 아직 저장되지 않음.
                        # 6. Amenity 유효성 검증 및 추가
                        amenities = request.data.get("amenities")
                        for amenity_val in amenities:
                            amenity = Amenity.objects.get(pk=amenity_val)
                            room.amenities.add(amenity)  # 7. 최종 저장된 json 생성
                        serializer = RoomDetailSerializer(
                            room
                        )  # 8. serializer로 보여줄 값 생성
                        return Response(serializer.data)
                except Exception:
                    raise ParseError("Invalid amenity")
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated  # 로그인 상태가 아닐 시


class RommDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        print(room.category)
        return Response(RoomDetailSerializer(room).data)

    def delete(self, request, pk):
        room = self.get_object(pk)
        if not request.user.is_authenticated:  # 0. 로그인 유무 확인 후
            raise NotAuthenticated  # 로그인 상태가 아닐 시
        if room.owner != request.user:
            raise PermissionError(HTTP_403_FORBIDDEN)  # owner가 아닐 경우
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        room = self.get_object(pk)

        if not request.user.is_authenticated:  # 0. 로그인 유무 확인 후
            raise NotAuthenticated  # 로그인 상태가 아닐 시
        if room.owner != request.user:
            raise PermissionError  # owner가 아닐 경우

        serializer = RoomDetailSerializer(room, data=request.data, partial=True)
        # model에 맞는 validity 검증
        if serializer.is_valid():
            category_pk = request.data.get("category")  # input category 값(int)
            try:
                category = Category.objects.get(
                    pk=category_pk
                )  # input category 값 validity check (object)
                if category.kind != Category.CategoryKindChoices.ROOMS:
                    raise ParseError("Invalid category for room")
            except Category.DoesNotExist:
                raise ParseError("Invalid category for room")

            try:
                with transaction.atomic():
                    if category_pk:  # 수정 있을 때
                        updated_room = serializer.save(
                            owner=request.user, category=category
                        )
                    else:  # 수정 없을 때
                        updated_room = serializer.save(owner=request.user)
                    input_amenities = request.data.get("amenities")
                    if input_amenities != None:
                        updated_room.amenities.clear()
                        for amenity_val in input_amenities:
                            amenity = Amenity.objects.get(pk=amenity_val)
                            updated_room.amenities.add(amenity)
                    return Response(serializer.data)
            except Amenity.DoesNotExist:
                raise ParseError("Amenity dosen't exists")
        else:
            Response(serializer.errors)
