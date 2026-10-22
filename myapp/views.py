#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Index page</h1>")

def hello(request, id):
    result = ((id + 100) * 3 / 2)
#    return HttpResponse("<h1>Hello " + username + "</h1>")
#    return HttpResponse(f"<h1>Hello {username}</h1>")
    return HttpResponse("<h1>Hello ID user: %s</h1>" % int(result))

def about(request):
    return HttpResponse("About")
