from django.http import HttpResponse


def mainpage(request):
    resp = HttpResponse('<h1>Проект Book с postgresql</h1>')
    return resp
