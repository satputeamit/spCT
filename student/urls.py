from django.urls import path
from .views import home, StudentList, CourseDetails,CourseList

urlpatterns = [
    path('', home, name="home"),
    path('students', StudentList.as_view()),
    path('course', CourseList.as_view()),
    path('course/<int:pk>', CourseDetails.as_view()),

]
