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
