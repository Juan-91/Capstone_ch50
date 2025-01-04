from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending Email")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"This is an email from your portfolio page\nNmae:{name}\nEmail:{email}\nMessage:{message}"

            send_mail(
                "Email from " + name,
                message,
                email,
                ['juan.montiel@sdgku.edu']
            )

            print("Email sent")

        else:
            print("Invalid data on the form")
    else:
        
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})