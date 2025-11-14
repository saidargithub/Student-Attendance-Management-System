from django.contrib import admin
from .models import Student, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'student_class', 'email')
    search_fields = ('name', 'roll_no', 'student_class', 'email')
    list_filter = ('student_class',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'present')
    search_fields = ('student__name', 'student__roll_no')
    list_filter = ('date', 'present', 'student__student_class')

# Register your models here.
