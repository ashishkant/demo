from django.forms import ModelForm
from .models import Post, Employee , Student

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', 'author', 'author']       

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'hire_date', 'salary']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'email']