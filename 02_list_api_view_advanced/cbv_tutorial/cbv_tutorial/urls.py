from django.contrib import admin
from django.urls import path

from student import apiviews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/student/list/', apiviews.StudentListAPI.as_view(), name='api_student_list'),
    path('api/student/list/year/<int:year>/', apiviews.StudentListYearAPI.as_view(), name='api_student_year_list'),
    path('api/student/list/year/range/',
         apiviews.StudentListYearRangeAPI.as_view(),
         name='api_student_year_range_list')
]
