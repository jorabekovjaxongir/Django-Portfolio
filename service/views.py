from django.shortcuts import render
from blog.models import Blog, Category
from about.models import About
from collection.models import Collection
from .models import Service
from contact.models import ContactMe


# Create your views here.

def serviceView(request):
    service = Service.objects.all()
    about = About.objects.all()
    cme = ContactMe.objects.all()    
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    collection = Collection.objects.all().order_by('-id')[:9]
    context = {
        'abouts': about,        
        'services': service,
        'me': cme,
        'blogs': blog,
        'collections': collection,
        'categories': category,
    }
    return render(request, 'services.html', context)




