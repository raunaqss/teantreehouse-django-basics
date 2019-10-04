from django.http import HttpResponse

# all views have to accept a request, even if we don't use it
def hello_world(request):
    return HttpResponse('Hello, world!')