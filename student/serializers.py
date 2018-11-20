from rest_framework import serializers
from student.models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_name', 'class_name', 'code')  