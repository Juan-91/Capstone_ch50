# Generated by Django 5.1.4 on 2025-01-15 03:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_lecture_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='assigned_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
