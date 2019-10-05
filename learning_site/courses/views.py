from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Course, Step
# Create your views here.

def course_list(request):
    '''Takes request and renders page with list of all courses'''
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_pk):
    '''Takes the course primary key from path and shows its details'''
    course = get_object_or_404(Course, pk=course_pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_order_detail(request, course_pk, step_order):
    '''Unlike the step detail view in the course, 
    I want to show the steps by order rather than id'''
    steps = get_list_or_404(Step, course_id=course_pk, order=step_order)
    return render(request, 'courses/step_detail.html', {'steps': steps, 'order': step_order})
