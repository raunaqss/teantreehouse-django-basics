from django.urls import path
from . import views
# this HAS to be named urlpatterns for it to work, because Django expects it that way of course 
urlpatterns=[
    path('', views.course_list, name='Course List')
]