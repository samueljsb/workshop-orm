from __future__ import annotations

from typing import Any

from django.core.management.base import BaseCommand

from school.data.models import Course
from school.data.models import Grade
from school.data.models import Student
from school.data.models import Teacher


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        # Teachers
        mr_miyagi = Teacher.objects.create(name="Mr Miyagi")
        john_keating = Teacher.objects.create(name="John Keating")  # noqa: F841
        obi_wan_kenobi = Teacher.objects.create(name="Obi-Wan Kenobi")

        # Students
        greg_jackson = Student.objects.create(name="Greg Jackson")
        james_eddison = Student.objects.create(name="James Eddison")
        stuart_jackson = Student.objects.create(name="Stuart Jackson")
        rds = Student.objects.create(name="Rebecca Dibb-Simkin")

        # Courses
        business_101 = Course.objects.create(
            title="Business 101",
            instructor=mr_miyagi,
        )
        business_101.students.set([greg_jackson, james_eddison, stuart_jackson])

        win_friends = Course.objects.create(
            title="How to Win Friends and Influence People", instructor=obi_wan_kenobi
        )
        win_friends.students.set([greg_jackson, james_eddison, rds])

        # Grades
        # N.B. these grades are not a commentary on the real-world abilities of the
        # (fictional) teachers or (real) students.
        Grade.objects.create(course=business_101, student=greg_jackson, grade="A+")
        Grade.objects.create(course=business_101, student=james_eddison, grade="B-")
        Grade.objects.create(course=business_101, student=stuart_jackson, grade="A-")
        Grade.objects.create(course=win_friends, student=greg_jackson, grade="A")
        Grade.objects.create(course=win_friends, student=james_eddison, grade="C+")
        Grade.objects.create(course=win_friends, student=rds, grade="A+")
