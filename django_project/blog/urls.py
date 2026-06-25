from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='posts'),
    path('post/create', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('employee/create', views.create_employee, name='employee-create'),
    path('student/create', views.create_student, name='student-create'),
    path('about/',views.about, name='about'),
]