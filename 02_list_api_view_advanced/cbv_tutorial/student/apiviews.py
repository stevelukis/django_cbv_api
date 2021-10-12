from rest_framework import generics, status
from rest_framework.response import Response

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


class StudentListYearRangeAPI(generics.ListAPIView):
    model = Student
    serializer_class = StudentSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_year = None
        self.end_year = None

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            self.start_year = data['start_year']
            self.end_year = data['end_year']
        except (KeyError, ValueError):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Student.objects.filter(year__gte=self.start_year, year__lte=self.end_year)



