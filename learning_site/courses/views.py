from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.

def course_list(request):
    '''Takes request and renders page with list of all courses'''
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    '''Takes the course primary key from path and shows its details'''
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})
