from django.urls import path
from .views import (
    CourseCreateView,
    CourseListView, 
    LectureCreateView,
    LectureListView,
    LectureDetailView
    )

urlpatterns = [
    path("create_course/", CourseCreateView.as_view(), name="create_course"),
    path("list_course/", CourseListView.as_view(), name="list_course"),
    path("create_lecture/", LectureCreateView.as_view(), name="create_lecture"),
    path("list_lecture/", LectureListView.as_view(), name="list_lecture"),
    path("detail_lecture/", LectureDetailView.as_view(), name="detail_lecture"),
]