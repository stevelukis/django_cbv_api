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

    def verify_list(self, expected, result):
        self.assertEqual(len(result), len(expected))

        for i in range(len(expected)):
            student_exp = expected[i]
            student_res = result[i]

            self.assertEqual(student_exp.name, student_res['name'])
            self.assertEqual(student_exp.year, student_res['year'])

    def setUp_list1(self):
        num_students = 10
        self.student_list = create_random_students(num_students)

    def test_student_list(self):
        self.setUp_list1()

        url = reverse('api_student_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.verify_list(self.student_list, response.data)

    def setUp_list2(self):
        num_students_2016 = 10
        self.student_list_2016 = create_random_students(num_students_2016, 2016)

        num_students_2017 = 15
        self.student_list_2017 = create_random_students(num_students_2017, 2017)

    def test_student_list_specific_year(self):
        self.setUp_list2()

        url = reverse('api_student_year_list', kwargs={'year': 2016})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.verify_list(self.student_list_2016, response.data)

        url = reverse('api_student_year_list', kwargs={'year': 2017})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.verify_list(self.student_list_2017, response.data)
