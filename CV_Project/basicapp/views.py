from django.shortcuts import render
from basicapp.models import Contact
from basicapp.forms import ContactForm

def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

    return render(request, 'basicapp/home.html', {'form':form})
