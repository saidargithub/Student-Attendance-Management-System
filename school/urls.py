from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    AttendanceViewSet,
    dashboard,
    students_list,
    student_create,
    student_edit,
    student_delete,
    attendance_mark,
    attendance_records,
    attendance_report,
)

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('students/', students_list, name='students_list'),
    path('students/new/', student_create, name='student_create'),
    path('students/<int:pk>/edit/', student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
    path('attendance/mark/', attendance_mark, name='attendance_mark'),
    path('attendance/records/', attendance_records, name='attendance_records'),
    path('attendance/report/', attendance_report, name='attendance_report'),
    path('api/', include(router.urls)),
]