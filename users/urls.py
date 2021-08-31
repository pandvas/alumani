
from django.contrib import admin
from django.urls import path, include
from .views import RegisterView,LoginView,UserView,LogoutView,RegisterUniversityView, RegisterDepartmentView,RegisterHodView, RegisterFacultyView, RegisterStudentView, RegisterCourseView, RegisterEventView, EventpollView, StudentPasswordView, ContactView, PaymentView, DepartmentMapperView, FacultyMapperView, StudentMapperView, RollNoMapperView, EventMapperView

urlpatterns = [
    path('admin/register/', RegisterView.as_view()),
    path('admin/login/', LoginView.as_view()),
    path('admin/', UserView.as_view()),
    path('admin/logout/', LogoutView.as_view()),
    path('admin/addUniversity/',RegisterUniversityView.as_view()),
    path('admin/addDepartment/', RegisterDepartmentView.as_view()),
    path('admin/addHod/', RegisterHodView.as_view()),
    path('admin/addFaculty/', RegisterFacultyView.as_view()),
    path('admin/addStudent/', RegisterStudentView.as_view()),
    path('admin/addCourse/', RegisterCourseView.as_view()),
    path('admin/addEvent/', RegisterEventView.as_view()),
    path('eventPoll/', EventpollView.as_view()),
    path('studentPassword/', StudentPasswordView.as_view()),
    path('contact/', ContactView.as_view()),
    path('payment/', PaymentView.as_view()),
    path('admin/departmentMapper/', DepartmentMapperView.as_view()),
    path('admin/facultyMapper/', FacultyMapperView.as_view()),
    path('admin/studentMapper/', StudentMapperView.as_view()),
    path('admin/rollNoMapper/', RollNoMapperView.as_view()),
    path('admin/eventMapper/', EventMapperView.as_view()),
]