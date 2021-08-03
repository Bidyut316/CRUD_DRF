from django.urls import path
from . import views

urlpatterns = [
    path('apis/', views.apiOverview, name="api-overview"),
    path('students/', views.studentDetails, name='student_details'),
    path('add-student/', views.addStudent, name='add_student'),
    path('update-student/<str:pk>/', views.updateStudent, name='update_student'),
    path('delete-student/<str:pk>/', views.deleteStudent, name='delete_student')

]
