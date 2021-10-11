from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer


class StudentListAPI(generics.ListAPIView):
    model = Student
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
