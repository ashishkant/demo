from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , Employee




# Create your views here.
def home(request):
    posts=Post.objects.all()
    employees=Employee.objects.all()
    context = {'posts':posts,
        'employees':employees,
        'title': 'Zen of Python'
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')