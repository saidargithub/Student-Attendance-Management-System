from rest_framework import serializers
from .models import Student, Attendance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_no', 'student_class', 'email']


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        source='student', queryset=Student.objects.all(), write_only=True
    )

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'student_id', 'date', 'present']