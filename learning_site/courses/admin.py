from django.contrib import admin
from .models import Course, Step
# Register your models here.

class StepInline(admin.StackedInline):
    '''Class to help define steps from within the admin form for courses'''
    model = Step

class CourseAdmin(admin.ModelAdmin):
    '''This class helps us modify Course model's admin class'''
    inlines = [StepInline, ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Step)
