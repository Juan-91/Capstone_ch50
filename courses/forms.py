from django import forms
from .models import Course, Lecture
from ckeditor.widgets import CKEditorWidget


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course"]

class LectureForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lecture
        fields = ["title", "body", "instructor", "course"]