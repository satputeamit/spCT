from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Course
from .serializer import StudentSerializer, CourseSerializer


def home(request):
    stud = Student.objects.all()
    return render(request, "home.html", {"result": stud})


class StudentList(APIView):
    # model = Student

    def get(self, request):
        stud = Student.objects.all()
        serializer = StudentSerializer(stud, many=True)
        return Response(serializer.data)


class CourseList(APIView):
    def get(self, request):
        cors = Course.objects.all()
        serializer = CourseSerializer(cors, many=True)
        return Response(serializer.data)


class CourseDetails(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        cors = self.get_object(pk)
        serializer = CourseSerializer(cors)
        return Response(serializer.data)

    def delete(self, request, pk):
        print("pk :",pk)
        obj = self.get_object(pk)
        print("obj :",obj)
        obj.delete()
        return Response("Record deleted")