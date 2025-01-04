from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from .forms import SignupForm
from .models import Profile


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
    
class SignUpView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('login')
    
    #extend the save functionality
    def form_valid(self, form):
        user = form.save(commit=False)
        passw = form.cleaned_data['password']
        user.set_password(passw)
        user.save()

        #create an empty profile for the user
        Profile.objects.create(user=user)

        return super().form_valid(form)


def user_logout(request):
        logout(request)
        return redirect('login')