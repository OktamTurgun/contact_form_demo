from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactMessageForm
from .models import ContactMessage

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("messages"))
    else:
        form = ContactMessageForm()

    return render(request, "contacts/home.html", {"form": form})

def message_list(request):
    messages_qs = ContactMessage.objects.all()
    return render(request, "contacts/message_list.html", {"messages": messages_qs})
