from rest_framework import serializers
from .models import Category

# 모델 보고 자동으로 Serializer 생성
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 이거 하나면 충분함
        # exclude = ('created_at')
        # fields = ("name","kind")
        # 둘 중 하나만 선택. 제외할 것을 고르거나, 넣을 것을 고르거나
        fields = (
            "name",
            "kind",
        )
