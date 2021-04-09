from . import views
from django.urls import path

urlpatterns = [    
    path('', views.studentList, name='student-list'),
    path('student-create', views.studentCreate, name='student-create'),
    path('student-update/<int:id>', views.studentUpdate, name='student-update'),
    path('student-delete/<int:id>', views.studentDelete, name='student-delete'),
]