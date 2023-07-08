from django.http import HttpResponse


# ====Django basics practice code======
# def index(request):
#     return  HttpResponse("hello..! world")
#
# def about(request):
#     return  HttpResponse("hello..! shivu")


# basics of pipeline
def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return  HttpResponse("removepunc <br> <a href='/'>back</a>")

def capfirst(request):
    return  HttpResponse("capitalize first  <br> <a href='/'>back</a>")

def newlineremove(request):
    return HttpResponse("new line remove <br> <a href='/'>back</a>")

def spaceremove(request):
    return HttpResponse("space remov <br>e <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("character count <br> <a href='/'>back</a>")
