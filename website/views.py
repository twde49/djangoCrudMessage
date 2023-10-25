from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import ModelForm

from .models import Message


# Create your views here.
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["title", "content"]


baseUrl = "http://localhost:8000/website/"


def all_messages(request):
    messages = Message.objects.all()
    context = {
        "messages": messages
    }

    return render(request, "website/all.html", context)


def show_message(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'website/show.html', {"message": message})


def create_message(request):
    message_form = MessageForm(request.POST or None)
    if message_form.is_valid():
        message_form.save()
        return redirect(baseUrl)
    return render(request, "website/create.html", {"message_form": message_form})


def update_message(request, id):
    message = get_object_or_404(Message, id=id)
    message_form = MessageForm(request.POST or None, instance=message)
    if message_form.is_valid():
        message_form.save()
        return redirect(baseUrl)
    return render(request, "website/create.html", {'message_form': message_form})


def message_delete(request, id):
    message = get_object_or_404(Message, id=id)
    if message:
        message.delete()
    return redirect(baseUrl)
