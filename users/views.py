from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout


"""
Class-based views:

View = generic view
ListView = get a list of records
DetailView = get a single(detail) record
DeleteView = create a new record
DeleteView = remove a record
UpdateView = modify an existing record
LoginView = login
"""



# Create your views here.
class UserLoginView(LoginView):
    template_name ="users/login.html"

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
        logout(request)
        return redirect('login')