from __future__ import annotations

from django.db import models


class Teacher(models.Model):
    name = models.TextField()


class Student(models.Model):
    name = models.TextField()


class Course(models.Model):
    title = models.TextField()

    instructor = models.ForeignKey(
        Teacher, related_name="courses", on_delete=models.PROTECT
    )
    students = models.ManyToManyField(Student, related_name="courses")
