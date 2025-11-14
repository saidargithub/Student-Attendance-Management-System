from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'date')
        ordering = ['-date', 'student__roll_no']

    def __str__(self):
        status = 'Present' if self.present else 'Absent'
        return f"{self.student.roll_no} - {self.date} - {status}"

# Create your models here.
