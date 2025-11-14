from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from datetime import date as date_cls

from rest_framework import viewsets, permissions

from .models import Student, Attendance
from .serializers import StudentSerializer, AttendanceSerializer
from .forms import StudentForm, AttendanceFilterForm


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_class', 'roll_no')
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('student').all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.AllowAny]


@login_required
def dashboard(request):
    total_students = Student.objects.count()
    selected_date_str = request.GET.get('date')
    if selected_date_str:
        try:
            selected_date = date_cls.fromisoformat(selected_date_str)
        except ValueError:
            selected_date = date_cls.today()
    else:
        selected_date = date_cls.today()

    present_count = Attendance.objects.filter(date=selected_date, present=True).count()
    absent_count = Attendance.objects.filter(date=selected_date, present=False).count()

    context = {
        'total_students': total_students,
        'selected_date': selected_date,
        'present_count': present_count,
        'absent_count': absent_count,
    }
    return render(request, 'dashboard.html', context)


@login_required
def students_list(request):
    q = request.GET.get('q', '').strip()
    students = Student.objects.all().order_by('student_class', 'roll_no')
    if q:
        students = students.filter(name__icontains=q) | students.filter(roll_no__icontains=q) | students.filter(student_class__icontains=q)
    return render(request, 'students/list.html', {'students': students, 'query': q})


@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Student'})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('students_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form, 'title': 'Edit Student'})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted.')
        return redirect('students_list')
    return render(request, 'students/confirm_delete.html', {'student': student})


@login_required
def attendance_mark(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        student_class = request.POST.get('student_class')
        try:
            selected_date = date_cls.fromisoformat(date_str)
        except Exception:
            selected_date = date_cls.today()
        students = Student.objects.all()
        if student_class:
            students = students.filter(student_class=student_class)

        for s in students:
            present_val = request.POST.get(f'present_{s.id}') == 'on'
            att_obj, _ = Attendance.objects.get_or_create(student=s, date=selected_date)
            att_obj.present = present_val
            att_obj.save()
        messages.success(request, 'Attendance saved.')
        return redirect('attendance_records')

    # GET
    form = AttendanceFilterForm(request.GET or None)
    students = Student.objects.all().order_by('roll_no')
    if form.is_valid():
        student_class = form.cleaned_data.get('student_class')
        if student_class:
            students = students.filter(student_class=student_class)
    return render(request, 'attendance/mark.html', {'form': form, 'students': students})


@login_required
def attendance_records(request):
    form = AttendanceFilterForm(request.GET or None)
    records = Attendance.objects.select_related('student').all().order_by('-date', 'student__roll_no')
    if form.is_valid():
        d = form.cleaned_data.get('date')
        c = form.cleaned_data.get('student_class')
        if d:
            records = records.filter(date=d)
        if c:
            records = records.filter(student__student_class=c)
    return render(request, 'attendance/records.html', {'form': form, 'records': records})


@login_required
def attendance_report(request):
    form = AttendanceFilterForm(request.GET or None)
    selected_date = None
    records = Attendance.objects.all()
    if form.is_valid():
        selected_date = form.cleaned_data.get('date')
        student_class = form.cleaned_data.get('student_class')
        if selected_date:
            records = records.filter(date=selected_date)
        if student_class:
            records = records.filter(student__student_class=student_class)

    present_count = records.filter(present=True).count()
    absent_count = records.filter(present=False).count()
    return render(request, 'attendance/report.html', {
        'form': form,
        'selected_date': selected_date,
        'present_count': present_count,
        'absent_count': absent_count,
    })

# Create your views here.
