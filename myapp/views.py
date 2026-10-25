#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Likla'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    print(type(username))
#    result = ((id + 100) * 3 / 2)
#    return HttpResponse("<h1>Hello " + username + "</h1>")
#    return HttpResponse(f"<h1>Hello {username}</h1>")
    return HttpResponse("<h1>Hello %s</h1>" % username)


def projects(request):
#    projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'project.html',{
        'projects': projects
    })
#    return JsonResponse(projects, safe=False)


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task.html',{
        'tasks' : tasks
    })
"""
def tasks(request, id):
    task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse('Task: %s' % task.title)
"""

"""
def tasks(request, name):
    task = Task.objects.get(title=name)
    return JsonResponse('Task: %s' % task.title, safe=False)
"""
