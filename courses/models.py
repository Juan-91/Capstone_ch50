from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Course(models.Model):
    course= models.CharField(max_length=128)
    students = models.ManyToManyField(User, related_name="assigned_courses", blank=True, null=True)
    def __str__(self):
        return self.course

class Lecture(models.Model):
    title = models.CharField(max_length=128)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lectures")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_lecture", args=[self.id])
