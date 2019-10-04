from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
# Create your views here.

def course_list(request):
    return HttpResponse(', '.join([str(c) for c in Course.objects.all()]))
    