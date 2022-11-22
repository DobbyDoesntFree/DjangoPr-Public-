# Virtual Env

1. poetry init
2. add django (can be other things)
3. poetry shell (Entring to virtual env)
4. Check command django-admin
5. exit (Exiting from virtual env)
6. Set enterpreter (if dosen't appear, use this command)

   > poetry env info --path

      <br>

# Start Project, App, Setting

1. django-admin startproject config
2. python manage.py startapp ##
3. go to settings.py and add path

# Class

```python
class Human:
    def __init__(self, name):
        self.name = name
    def hola(self):
        print(f"Hola, {self.name}")
class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name) # 여기서 상속된 name이 정의됨
        self.xp=xp

alpha = Player("ASDF", 1000)
alpha.hola()
print(alpha.name, beta.name)
```

```
1. self attribute is mandatory
2. use like as Player(Human) to call parent Class
3. use super.__init__(name) for call parent class method (method override)
   (If super class dosen't has a method need to call like __init__(name), able to dosen't use super in child class)
4. def __str__(self): to show default value in case of call class
5. dir(Class) to show usable
```

# models.py

> Describe shape of database (mostly use Class)

```python
class House(models.Model):
    # House Model
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
```

- CharField : text dosen't so long and has limit
- PositiveBigIntegerField : literally int greater than 0
- TextField : literally field receieve text

1. Go to settings.py and Add the path of models.py

## Migration

> Modify shaepe of db (Modify include CRUD, Create django_session for admin is also somekind of modification)

When show error message like "You have 18 unapplied migration(s)." try these below

1. python manage.py makemigrations
   - make migration file (like git staging)
2. python manage.py migrate
   - apply migration (like git commit)

<br>

## model connection

> use pk(automatically generated id) to connect

```python
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
```

# users

> it should be consider as first things to do (almost every connection start from user)

## config/settings

> add code below

```python
   # Auth
CUSTOM_APPS = ["users.apps.UsersConfig",]
AUTH_USER_MODEL = 'users.User'
```

## user/apps

```python
from django.apps import AppConfig
class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
```

## user/models

```python
class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")  # ('value for db', 'value for adminpage')
        FEMALE = ("female", "Female")  # value for db must be match maxlength condition

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        KRW = "krw", "Korea Won"
        USD = "usd", "US Dollar"

    first_name = models.CharField(
        ("first name"),
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        ("last name"),
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    avatar = models.ImageField(blank=True)  # need Pillow
    is_host = models.BooleanField(default=False)  # or null=True
    gender = models.CharField(
        max_length=10,
        choices=GenderChoice.choices,
        default="male",
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default="kr",
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        default="krw",
    )
```

## user/admin

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)  # The class below will control user model
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "avatar",
                    "gender",
                    "language",
                    "currency",
                ),
                "classes": ("wide"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {"fields": ("last_login", "date_joined")},
        ),
    )
    list_display = ("username", "email", "name", "is_host")

```

## Clearing db

1. Delete 000n_initial.py (need terminate old db)
2. python manage.py makemigrations
   > by these sequences, you can manage(extends) user model without considering terminate db

# Create admin account [Create suepruser]

1. python manage.py createsuperuser (admin / rkskek13)

<br>

# rooms

## config/settings

> add code below

```python
   # Auth
CUSTOM_APPS = ["rooms.apps.RoomsConfig",]
```

## models.py

```python
class House(models.Model):

    # House Model
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(
        verbose_name="Price per day", help_text="Enter positive number"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Is this house allow pet?"
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
# The connection above bring User class's id
# user(app name).User(class name which inside of user/models.py)
# on_delete is mandatory
# on_delete=model.CASCADE, (on_delete=models.SET_NULL, null=True)

    def __str__(self):  # this will run everytime when call this class
        return self.name
```

## admin.py

```python
# admin.py
from django.contrib import admin
from .models import House
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    #pass
    list_display= ("name","price", "address","pets_allowed")
    list_filter = ("name","price", "address","pets_allowed")
    search_fields = ("address__startswith",)
    # add comma. if not, VSC treat it as string

```

1. use "pass" to inherit everything
2. the code meaning HouseAdmin class control House (imported)model

# House.py

## config/settings

> add code below

```python
   # Auth
CUSTOM_APPS = ["houses.apps.HouseConfig",]
```

## models.py

```python
class House(models.Model):

    # House Model
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(
        verbose_name="Price per day", help_text="Enter positive number"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Is this house allow pet?"
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
# The connection above bring User class's id
# user(app name).User(class name which inside of user/models.py)
# on_delete is mandatory
# on_delete=model.CASCADE, (on_delete=models.SET_NULL, null=True)

    def __str__(self):  # this will run everytime when call this class
        return self.name
```

## admin.py

```python
# admin.py
from django.contrib import admin
from .models import House
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    #pass
    list_display= ("name","price", "address","pets_allowed")
    list_filter = ("name","price", "address","pets_allowed")
    search_fields = ("address__startswith",)
    # add comma. if not, VSC treat it as string

```

1. use "pass" to inherit everything
2. the code meaning HouseAdmin class control House (imported)model

- OneToOneField

```python
class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(  # by this the experiences can't have more Video
        # this maening experience able to have only one video
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
```

- releated_name

```python
class Room(CommonModel):
    users = models.ManyToManyField(
        "users.User",  # user, chatroom able to many to many rel
    )  # can cause problem since same classname connected to users.User model
    # same classname itself dosen't matter
```

- plural

```python
# in model
    class Meta:
        verbose_name_plural = "Categories"

# in apps
    verbose_name="Direct Message"
```

# DB modify

> use class object inside of model

## setup

1. python manage.py shell
2. from rooms.models import Room
3. Get Test case
   > room = Room.objects.get(name="##") or (id="##") can choice anything

> room.owner < grab object

> objects : manager (Interface for communicate with db) 3. Input Test case
> room.pk, room.id, room.price = 20, room.owner.email = "SSS@AA.com"
> like above, able to modify value of db
> or can be use like below

```python
for i in Room.objects.all():
    print(i.name)
```

4. close with room.save()

<br/>

## Object CRUD Methods

<br>

### All. objects.all()

> bring everything

### Get. objects.get(pk=1) # (id=1), get only one item

> bring just ONE item

### Filter. Room.objects.filter(pet_friendly=True)

> bring all case match condition

- Room.objects.filter(pet_friendly=True)
- Room.objects.filter(price\_\_gt=15)
  - gt meaning greater than (lt is less)
  - gte meaning greater than or equal (lte is less)
- Room.objects.filter(name\_\_contains="The")
- Room.objects.filter(name\_\_startswith="The")

### Create. Amenity.objects.create(name="Console Test", descriptions = "TEST")

> create object

- Amenity.objects.create(name="Console Test", descriptions = "TEST")

### Delete. Amenity.objects.get(pk=5).delete()

> find(get or filter) and delete

- to_del = Amenity.objects.get(pk=5)
- to_del.delete()

<br/>

## lookup \_\_

- (name**exact="AsdF"), (name**iexact="AsdF") # 일치 (i 유무 따라 대소문자 구분여부 결정)
- filter(pub_date**month**gte=6) # 이와 같이 연결 가능
- filter(pub_date**month**gte=6).exists # Return bool
- https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups 참고
- also able to use \_\_ with foreign key object (See Reverse Accessor below)

## Query Sets, Adv. Filtering

> chain filter

- Room.objects.filter(pet_friendly=True).exclude(price**lt=15).filter(name**contains="The")
- Room.objects.filter(pet_friendly=True,name**contains="The",price**gt=15).count()
  > admin application example

```python
    def total_amenities(self, room):
        # print(self) rooms.RoomAdmin
        # print(room) room name
        return room.amenities.count()
        #room.amenities. filter(), exclude()...
        # model.py에서는 room 없이 self.amenities.count()
```

## filter by Foreign Key , Reverse Accessor

> 누가 Foreign Key로 자신을 가르키는가?
>
> > review.user <> user.review

### Sol 1. filter by foreign key

1. from rooms.models import Room
2. Room.objects.filter(owner**username**startswith='admin')
3. from reviews.models import Review
4. Review.objects.filter(user**username**exact='admin').count()
   > filtering everytime is sucks

### Sol 2. Reverse Accessor "\_set"

1. from users.models import User
2. me = User.objects.get(pk=1)
3. dir(me) # to check commands
4. me.room_set.all() # me(User)에 달린 room 가져옴. all 없으면 메모리 주소 가져옴
   > though improved, it is quite annoying to use this method (search dir everytime? it sucks)

### Sol 3 Reverse Accessor "related_name"

> B가 A에 대해 Foreign Key를 가지면 (A>B)이고, A는 B_set을 가짐(이 과정은 자동으로 수행)

1. ForeignKey 생성된 곳에 related_name="##" (##은 원하는 이름) 추가
2. from users.models import User
3. me = User.objects.get(pk=1)
4. me.##.all()
   > It dosen't mandatory, using this method can save many time

# Urls, Views (without REST)

## urls.py

> create urls.py in each app and import all of these into config.urls

```python
#config
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rooms/", include("rooms.urls")),
]
```

```python
urlpatterns = [
    path("", views.list_all),
    path("<int:room_id>", views.list_one),
    # path("<int:room_id>/<str:room_name>", views.s),
] # path(가야할 곳, 가서 할 행동)
```

## views.py

```python
from django.shortcuts import render # render html
from django.http import HttpResponse # mandatory. need to return http obj to show
from .models import Room # import model if need to grab data from db
def list_all(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {"rooms": rooms, "title": "Title from django"},
    )
    # request, Page for render, context data
def list_one(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
        return render(request, "room_detail.html", {"room": room})
    except Room.DoesNotExist:
        return render(request, "room_detail.html", {"not_found": True})
```

## templates

```html
<h1>{{title}}</h1>
<ul>
  {%for room in rooms%}
  <li>
    <a href="/rooms/{{room.pk}}">
      {{room.name}}
      <br />{%for amen in room.amenities.all%}
      <!-- .all()이 아닌 .all -->
      <span>{{amen.name}}</span>
      {%endfor%}</a
    >
  </li>
  {%endfor%}
</ul>
```

```html
{%if not not_found%}
<h1>Detail for {{room.name}}</h1>
<h3>{{room.country}}/{{room.city}}</h3>
<h4>{{room.price}}</h4>
<p>{{room.description}}</p>
<h5>{{room.category.name}}</h5>
{%else%}
<h1>404 not found</h1>
{%endif%}
```

# REST Method 1 - Manually config

> fix the shit things above views

```python
# views.py
from .models import Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

# use api_view decorator
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories, many=True
        )  # required 있는 항목 작성않아도 들어감
        return Response(
            serializer.data,
        )
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)  # user에게 받은 데이터 뿐
        if serializer.is_valid():
            new_category = serializer.save()  # user에게 받은 데이터밖에 없음 >> create 실행
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


# .data comes from api_view


@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,  # db에서 가져온 데이터
            data=request.data,  # 유저가 작성한 데이터
            partial=True,  # 수정 항목 이외의 valid check 수행하지 않음
        )
        if serializer.is_valid():
            updated_category = (
                serializer.save()
            )  # user에게 받은 데이터 + db에서 가져온 데이터 >> update 실행
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)

```

```python
from rest_framework import serializers
from .models import Category

# Select what, way to show
class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)  # read_only : 더 이상 수정 시 항목입력요구하지 않음
    # if wish to pk be string, just use like pk = serializers.charfield
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)  # ** 붙히면 가져온 값으로 dict 자동생성

    def update(self, instance, validated_data):  # self, db 값, 작성 값
        instance.name = validated_data.get("name", instance.name)
        # data 보냈으면 새 값으로, 없으면 기존 값으로 갱신 혹은 유지
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance

```

# Rest Method 2 - APIView (Recommanded)

```python
# views.py
from .models import Category
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView


class Categories(APIView):
    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(
            all_categories, many=True
        )  # required 있는 항목 작성않아도 들어감
        return Response(
            serializer.data,
        )

    def post(self, request):
        serializer = CategorySerializer(data=request.data)  # user에게 받은 데이터 뿐
        if serializer.is_valid():
            new_category = serializer.save()  # user에게 받은 데이터밖에 없음 >> create 실행
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

        return category

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        print(serializer)  # CategorySerializer가 ModelSerializer에 의해 자동생성된 것 확인 가능
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),  # db에서 가져온 데이터
            data=request.data,  # 유저가 작성한 데이터
            partial=True,  # 수정 항목 이외의 valid check 수행하지 않음
        )
        if serializer.is_valid():
            updated_category = (
                serializer.save()
            )  # user에게 받은 데이터 + db에서 가져온 데이터 >> 자동 update 실행
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)

```

```python
# serializer.py
from rest_framework import serializers
from .models import Category

# 모델 보고 자동으로 Serializer 생성
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 이거 하나면 충분함
        # exclude = ('created_at')
        # fields = ("name","kind")
        # 둘 중 하나만 선택. 제외할 것을 고르거나, 넣을 것을 고르거나
        fields = "__all__"
```

```python
# urls.py
from django.urls import path
from . import views
urlpatterns = [
    path("", views.Categories.as_view()),
    path("<int:pk>", views.CategoryDetail.as_view()),
]
```

# Rest Method 3 - Model View Set (Cheat code)

```python
# views.py
from .models import Category
from .serializers import CategorySerializer
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
```

```python
# serializers.py
from rest_framework import serializers
from .models import Category

# 모델 보고 자동으로 Serializer 생성
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 이거 하나면 충분함
        # exclude = ('created_at')
        # fields = ("name","kind")
        # 둘 중 하나만 선택. 제외할 것을 고르거나, 넣을 것을 고르거나
        fields = "__all__"
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.CategoryViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "<int:pk>",  # <int:pk> is mandatory. 기본값으로 pk 들어가있음
        views.CategoryViewSet.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
    ),
]
```

## More cheat code

- ReadonlyModelserializer
- Router (Cheat for urls.py)

# Relationship

## Showing everything

```python
# Serializer
class Roomserializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1 # enough for this
        # Can't customizable
```

## Customizing relationship

- create serializer based on model you want to use
- and import it

```python
class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer() # import from other serializer.py
    amenities = AmenitySerializer(many=True) # if you wish to span list, put many=True
    category = CategorySerializer() # 위와 비슷하지만 list가 아니므로 attr 필요 없음
    class Meta:
        model = Room
        fields = "__all__"

```

- when need to block edit

```python
# serializer는 import한 serializer의 shape을 원함
# user는 owner의 정보를 customized하면 안됨 never.
    owner = TinyUserSerializer(read_only=True)
```

4. Authenticate - Grab info by request

# TEST

```python
{
"name": "Category test",
"kind": "rooms"
}


{
    "name": "House created with DRF",
    "country": "Korea, Republic of",
    "city": "Seoul",
    "price": 999,
    "rooms": 2,
    "toilets": 2,
    "descriptions": "1",
    "address": "Seoul, Korea, 21234",
    "pet_friendly": true,
    "category":3,
    "kind": "private_room",
    "amenities":[1,2,3]
}
```
