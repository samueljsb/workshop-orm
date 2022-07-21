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


class Grade(models.Model):
    student = models.ForeignKey(
        Student, related_name="grades", on_delete=models.CASCADE
    )
    course = models.ForeignKey(Course, related_name="grades", on_delete=models.PROTECT)

    grade = models.CharField(max_length=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="one-grade_per_student_per_course",
            ),
        ]
