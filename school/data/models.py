from __future__ import annotations

from django.db import models


class Teacher(models.Model):
    name = models.TextField()


class Student(models.Model):
    name = models.TextField()
