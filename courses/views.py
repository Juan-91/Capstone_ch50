from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse
from .forms import CourseForm, LectureForm
from .models import Course, Lecture
from django.http import HttpResponseRedirect



# Course
class CourseCreateView(CreateView):
    template_name = "courses/create_course.html"
    form_class = CourseForm

    def get_success_url(self):
        form_data = self.request.POST
        option = form_data.get("option")
        if(option == "Save & Create Topic"):
            return reverse("create_lecture")
        
        return reverse("list_course")

class CourseListView(ListView):
    template_name = "courses/list_course.html"
    model = Course

    # force django to load the lectures of each course
    def get_queryset(self):
        return super().get_queryset().prefetch_related('lectures')
    
class CourseDetailView(DetailView):
    template_name = "courses/detail_course.html"
    model = Course

    def get_queryset(self):
       return super().get_queryset().prefetch_related('lectures')

class CourseUpdateView(UpdateView):
    template_name = "courses/update_course.html"
    form_class = CourseForm
    model = Course

    def get_success_url(self):
        return reverse("list_course")

class CourseDeleteView(DeleteView):
    template_name = "courses/delete_course.html"
    model = Course

    def get_success_url(self) -> str:
       return reverse('list_course')
    









# Lecture
class LectureCreateView(CreateView):
    template_name = "courses/create_lecture.html"
    form_class = LectureForm

    def get_success_url(self):
        return reverse("list_lecture")


class LectureListView(ListView):
    template_name = "courses/list_lecture.html"
    model = Lecture

class LectureDetailView(DetailView):
    template_name = "courses/detail_lecture.html"
    model = Lecture

class LectureUpdateView(UpdateView):
    template_name = "courses/update_lecture.html"
    form_class = LectureForm
    model = Lecture

    def get_success_url(self):
        return reverse("list_lecture")

class LectureDeleteView(DeleteView):
    template_name = "courses/delete_lecture.html"
    model = Lecture

    def get_success_url(self) -> str:
        return reverse('list_lecture')