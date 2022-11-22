from django.urls import path
from . import views

urlpatterns = [
    # root path rooms/
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RommDetail.as_view()),
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenityDetail.as_view()),
]
