from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer


class StudentListAPI(generics.ListAPIView):
    model = Student
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentListYearAPI(generics.ListAPIView):
    model = Student
    serializer_class = StudentSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        return Student.objects.filter(year=year)
