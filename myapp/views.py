from django.http import HttpResponse
# Create your views here.
def hello (request):
    return HttpResponse('''
    <h1>Hello World!</h1>
    <p>My first Django app</p>
    ''')
def about (request):
    return HttpResponse('''
    <h1>About</h1>
    <p>My My about in Django app</p>
    ''')