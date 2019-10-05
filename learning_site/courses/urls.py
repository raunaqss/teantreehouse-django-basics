from django.urls import path, re_path
from . import views
# this HAS to be named urlpatterns for it to work, because Django expects it that way of course 
urlpatterns = [
    path('', views.course_list, name='Course List'),
    re_path(r'(?P<pk>\d+)', views.course_detail, name='Course Detail')
]