from django.shortcuts import render
from django.http import HttpResponse


from .models import Message


# Create your views here.


def index(request):
    context = {
        "message": "coucou"
    }

    return render(request, 'website/home.html', context)


def bidule(request):
    return render(request, 'website/bidule.html', {
        "bidule": "un nouveau message"
    })


def all_messages(request):
    messages = Message.objects.all()
    context = {
        "messages": messages
    }

    return render(request, "website/all.html", context)


def show_message(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'website/show.html', {"message": message})


