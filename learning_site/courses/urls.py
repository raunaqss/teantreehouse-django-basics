from django.urls import path, re_path
from . import views
# this HAS to be named urlpatterns for it to work, because Django expects it that way of course
app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='list'),
    re_path(r'(?P<course_pk>\d+)/(?P<step_order>\d+)', views.step_order_detail, name='step'),
    re_path(r'(?P<course_pk>\d+)', views.course_detail, name='detail')
]
