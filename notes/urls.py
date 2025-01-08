from django.urls import path
from .views import ListNoteView, CreateNoteView

urlpatterns = [
    path("create/", CreateNoteView.as_view(), name= "create_note"),
    path("list/", ListNoteView.as_view(), name= "list_note"),
]