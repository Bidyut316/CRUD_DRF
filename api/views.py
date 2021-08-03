from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Student
from.serializers import StudentSerializer
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Student Details': '/students/',
        'Create': '/add-student/',
        'Update': '/update-student/<str:pk>/',
        'Delete': '/delete-student/<str:pk>/',
    }

    return Response(api_urls)

# Create


@api_view(['POST'])
def addStudent(request):
    student = StudentSerializer(data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data)

# Read


@api_view(['GET'])
def studentDetails(request):
    obj = Student.objects.all()
    Stu_serializer = StudentSerializer(obj, many=True)
    return Response(Stu_serializer.data)

# Update


@api_view(['POST'])
def updateStudent(request, pk):
    try:
        obj = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response("Student record not found")
    student = StudentSerializer(instance=obj, data=request.data)
    if student.is_valid():
        student.save()
    return Response(student.data)

# Delete


@api_view(['DELETE'])
def deleteStudent(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response("Student record not found")
    student.delete()
    return Response("Student record succsesfully deleted")
