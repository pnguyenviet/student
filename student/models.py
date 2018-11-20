# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    student_name = models.TextField(max_length=100)
    class_name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    class Meta:
        ordering = ('created',)