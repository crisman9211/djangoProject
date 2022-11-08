from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project,Task
# Create your views here.
def index(request):
    return HttpResponse('''
    Index page
    ''')
def hello (request,username: str):
    print(username)
    return HttpResponse(
    # '''
    # <h1>Hello World!</h1>
    # <p>My first Django app</p>
    # <p>My name is {username}</p>
    # '''.format(username=username)
    "<h1> Hello %s </h1>" % username
    )
def about (request):
    return HttpResponse('''
    <h1>About</h1>
    <p>My My about in Django app</p>
    ''')
def projects (request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)
    
def tasks (request,id:int):
    # tasks = list(Task.objects.filter(id=id).values())
    # task=Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return HttpResponse('Task: %s' % task.title)
