from django.shortcuts import redirect, render

from blog.forms import SubscribeForm
from blog.models import Blog
from .models import About, Section
from collection.models import Collection
from  contact.models import ContactMe


def aboutView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:9]
    cme = ContactMe.objects.all()
    section = Section.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.POST.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'abouts': about,
        'collections': collection,
        'cme' : cme,
        'sections':section,
        'blogs' : blog,
        'form' : form,
    }
    return render(request, 'about.html',context)
