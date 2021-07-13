from django.http import HttpResponse


def index(request):
    return HttpResponse("This is Homepage to my targets webapp.")
