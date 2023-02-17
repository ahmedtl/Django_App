from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.


def index(request):
    return HttpResponse("Hello Twin 3")


def list(request):
    list_event = Event.objects.filter(state=True)
    c = {'events': list_event}
    return render(request, 'event/list_event.html', c)
