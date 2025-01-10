from django.views.generic import(
    CreateView,
    ListView,
    DetailView
)
from django.urls import reverse
from .models import Course, Lecture

class CourseCreateView(CreateView):
    template_name = "courses/create_course.html"
    model = Course
    fields = ["course"]

    def get_success_url(self):
        return reverse("list_course")

class CourseListView(ListView):
    template_name = "courses/list_course.html"
    model = Course

    # force django to load the lectures of each course
    def get_queryset(self):
        return super().get_queryset().prefetch_related('lectures')


class LectureCreateView(CreateView):
    template_name = "courses/create_lecture.html"
    model = Lecture
    fields = ["title", "body", "instructor", "course"]

    def get_success_url(self):
        return reverse("list_lecture")


class LectureListView(ListView):
    template_name = "courses/list_lecture.html"
    model = Lecture

class LectureDetailView(DetailView):
    template_name = "courses/detail_lectue.html"
    model = Lecture
      
      