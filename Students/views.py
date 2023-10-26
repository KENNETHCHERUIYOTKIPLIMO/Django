from django.shortcuts import render


# Create your views here.


def contact(request):
    return  render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def classes(request):
    return render(request,'classes.html')

def services(request):
    return render(request,'services.html')


def home(request):
    return render(request,'home.html')