from django.http import HttpResponse

def home(request):
    return HttpResponse("Views")

def healthCheck(request):
    return HttpResponse('Estoy vivo perro hpta')