import random

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from student.models import Student


def create_random_students(num_students, year=None):
    students_list = []
    for i in range(num_students):
        if year is None:
            year = random.randint(2015, 2019)
        student = Student.objects.create(name=f"name{random.randint(100, 1000)}",
                                         year=year)
        students_list.append(student)
    return students_list


class StudentListTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def setUp_list1(self):
        num_students = 10
        self.student_list = create_random_students(num_students)

    def test_student_list(self):
        self.setUp_list1()

        url = reverse('api_student_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        students_expected_list = self.student_list
        students_result_list = response.data
        self.assertEqual(len(students_result_list), len(students_expected_list))

        for i in range(len(students_expected_list)):
            student_exp = students_expected_list[i]
            student_res = students_result_list[i]

            self.assertEqual(student_exp.name, student_res['name'])
            self.assertEqual(student_exp.year, student_res['year'])
