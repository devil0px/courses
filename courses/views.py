
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Courses
from .serializers import coursesSerilizers

class coursesView(viewsets.ModelViewSet):
	queryset = Courses.objects.all()
	serializer_class = coursesSerilizers