from django.http import HttpResponse

# Create your views here.


def index(request):
    d = {
        "name":"Arun",
        "age":30,
    }
    return HttpResponse(d)