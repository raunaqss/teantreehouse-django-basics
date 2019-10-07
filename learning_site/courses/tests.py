from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Course, Step
# Create your tests here.

class CourseTestCase(TestCase):
    '''Test everything Courses'''
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
    
    def test_default_step_order_is_0(self):
        self.assertEqual(self.eg_course_step.order, 0)

    def test_step_is_in_course(self):
        self.assertIn(self.eg_course_step, self.eg_course.step_set.all())
        self.assertIn(self.eg_course_step_1, self.eg_course.step_set.all())

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertQuerysetEqual(Course.objects.all(), resp.context['courses'], transform=lambda x: x)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', args=[self.eg_course.pk]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'courses/course_detail.html')
        self.assertEqual(self.eg_course, resp.context['course'])



        
