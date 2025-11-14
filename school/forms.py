from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'student_class', 'email']


class AttendanceFilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    student_class = forms.CharField(max_length=50, required=False)