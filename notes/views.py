from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse
from .forms import NoteForm
from .models import Note

# Create your views here.
class CreateNoteView(CreateView):
    template_name = "notes/create_note.html"
    form_class = NoteForm

    def get_success_url(self):
        return reverse("list_note")

class ListNoteView(ListView):
    template_name = "notes/list_note.html"
    model = Note

