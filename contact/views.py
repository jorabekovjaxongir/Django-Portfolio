from django.shortcuts import render, redirect
from about.models import About
from  .models import Contact, ContactMe
from .forms import ContactForm
from collection.models import Collection

def contactView(request):
    about = About.objects.all()
    form  = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    cme = ContactMe.objects.all()
    contact = Contact.objects.all()
    collection = Collection.objects.all().order_by('-id')[:9]
    context = {
        'abouts': about,
        'cme' : cme,
        'contacts': contact,
        'form': form,
        'collections': collection,
    }
    return render(request, 'contact.html', context)

# Create your views here.
