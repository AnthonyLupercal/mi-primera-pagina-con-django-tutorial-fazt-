#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewProject, CreateNewTask
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
    return render(request, 'projects/project.html',{
        'projects': projects
    })
#    return JsonResponse(projects, safe=False)
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'form' : CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        print(request.POST)
        print(project)
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks' : task
    })


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html',{
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

def create_task(request):
    if request.method == 'GET':
        # Show interface
        return render(request, 'tasks/create_task.html',{
            'form' : CreateNewTask()
        })
    else:
#        print(request.GET['title'])
#        print(request.GET['description'])
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
