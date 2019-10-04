from django.shortcuts import render

# all views have to accept a request, even if we don't use it
def hello_world(request):
    '''Take request and return simple example message'''
    return render(request, 'hello_world.html')
