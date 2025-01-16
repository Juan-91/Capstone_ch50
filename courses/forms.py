from django import forms
from .models import Course, Lecture


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course"]

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ["title", "body", "instructor", "course"]