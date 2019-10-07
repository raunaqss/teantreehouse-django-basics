from django.test import TestCase
from django.utils import timezone
from .models import Course, Step
# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        self.eg_course = Course.objects.create(
            title='Just an Example Course',
            description='Example description of our testing example course'
        )
        self.eg_course_step = Step.objects.create(
            title="First step",
            description="This is the first step's description.",
            course=self.eg_course
        )
        self.eg_course_step_1 = Step.objects.create(
            title="Another step",
            description="This is the other step's description",
            course=self.eg_course,
            order=1
        )

    def test_course_creation(self):
        now = timezone.now()
        self.assertLess(self.eg_course.created_at, now)

        
