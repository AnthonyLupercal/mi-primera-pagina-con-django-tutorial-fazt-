#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Index page</h1>")

def hello(request, username):
    print(type(username))
#    result = ((id + 100) * 3 / 2)
#    return HttpResponse("<h1>Hello " + username + "</h1>")
#    return HttpResponse(f"<h1>Hello {username}</h1>")
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse("About")
