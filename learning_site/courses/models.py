from django.db import models

# Create your models here.
class Course(models.Model):
    '''Model for a course on our learning site'''
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    '''Model for a step within a course'''
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, models.CASCADE)

    def __str__(self):
        return self.title
