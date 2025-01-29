from django.urls import path
from .views import (
    CourseCreateView,
    CourseListView, 
    CourseDetailView,
    CourseUpdateView,
    CourseDeleteView,
    LectureCreateView,
    LectureListView,
    LectureDetailView,
    LectureUpdateView,
    LectureDeleteView,
    enroll_user_course
    )

urlpatterns = [
    path("create_course/", CourseCreateView.as_view(), name="create_course"),
    path("list_course/", CourseListView.as_view(), name="list_course"),
    path("create_lecture/", LectureCreateView.as_view(), name="create_lecture"),
    path("list_lecture/", LectureListView.as_view(), name="list_lecture"),

    path("detail/<int:pk>/", LectureDetailView.as_view(), name="detail_lecture"),
    path("detail_course/<int:pk>/", CourseDetailView.as_view(), name="detail_course"),

    path("update/<int:pk>/", LectureUpdateView.as_view(), name="update_lecture"),
    path("update_course/<int:pk>/", CourseUpdateView.as_view(), name="update_course"),
    
    path("delete/<int:pk>/", LectureDeleteView.as_view(), name="delete_lecture"),
    path("delete_course/<int:pk>/", CourseDeleteView.as_view(), name="delete_course"),

    path("enrollment/course/", enroll_user_course, name="course_enrollment")
]