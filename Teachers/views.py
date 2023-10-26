from django.shortcuts import render

# Create your views here.


def aboutteachers(request):
    return render(request, 'aboutteachers.html')