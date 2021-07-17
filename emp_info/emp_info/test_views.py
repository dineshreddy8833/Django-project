from django.http.response import HttpResponse




def hello(request):
    return HttpResponse("Hello world!")
