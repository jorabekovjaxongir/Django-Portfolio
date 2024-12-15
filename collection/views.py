from django.shortcuts import render
from .models import Collection
from about.models import About
from  contact.models import ContactMe


def collectionView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:16]
    cme = ContactMe.objects.all()
    context = {
        'abouts': about,
        'collections': collection,
        'cme' : cme,
    }
    return render(request, 'collection.html', context)


# Create your views here.
