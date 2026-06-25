from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post , Employee, Student
from .forms import PostForm , EmployeeForm, StudentForm
from django.contrib import messages




def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})

# ...

def create_employee(request):
    if request.method == 'GET':
        context = {'form': EmployeeForm()}
        return render(request, 'blog/employee_form.html', context)
    elif request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The employee has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/employee_form.html', {'form': form})

def create_student(request):
    if request.method == 'GET':
        context = {'form': StudentForm()}
        return render(request, 'blog/student_form.html', context)
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The student has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/student_form.html', {'form': form})

# Create your views here.
def home(request):
    posts=Post.objects.all()
    employees=Employee.objects.all()
    students = Student.objects.all()  # Fetch all students from the database
    context = {'posts':posts,
        'employees':employees,
        'students':students,
        'title': 'Zen of Python'
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')