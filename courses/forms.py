from django import forms
from django.contrib.auth.models import User
from .models import Course, Lecture
from ckeditor.widgets import CKEditorWidget


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course", "students", "enrollkey"]

    def __init__(self, *args, **kwargs):
        # filter out super users
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = User.objects.filter(is_superuser=False)

class LectureForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lecture
        fields = ["title", "body", "instructor", "course"]