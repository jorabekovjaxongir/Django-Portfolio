from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from about.models import About
from blog.forms import CommentForm, SubscribeForm
from blog.models import Blog, Category,Teg
from collection.models import Collection
from contact.models import ContactMe


def homeView(request):
    about = About.objects.all()
    collection = Collection.objects.all().order_by('-id')[:9]
    cme = ContactMe.objects.all()
    context = {
        'abouts': about,
        'collections': collection,
        'cme' : cme,
    }
    return render(request, 'index.html', context)

def blogView(request):
    about = About.objects.all()
    cme = ContactMe.objects.all()
    blog = Blog.objects.all().order_by('-id')
    p = Paginator(blog, 3)
    page = request.GET.get('page')
    blog = p.get_page(page)
    category = Category.objects.all()
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    collection = Collection.objects.all().order_by('-id')[:9]
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    teg = Teg.objects.all()
    context = {
        'abouts' : about,
        'cme' : cme,
        'blogs' : blog,
        'collections' : collection,
        'categories' : category,
        'tegs': teg,
        'form' : form
    }
    return render(request, 'blog.html', context)


def singlelView(request,pk):
    blog = Blog.objects.get(id=pk)
    about = About.objects.all()
    cme = ContactMe.objects.all()
    category = Category.objects.all()
    collection = Collection.objects.all().order_by('-id')[:9]
    blog1 = Blog.objects.all().order_by('-id')
    teg = Teg.objects.all()
    cat = request.POST.get('cat')
    if cat:
        blog = blog1.filter(category__title__iexact=cat)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    context = {
        'abouts' : about,
        'cme' : cme,
        'blog1' : blog1,
        'collections' : collection,
        'categories' : category,
        'tegs': teg,
        'blogs' : blog,
        'form': form,
    }
    return render(request, 'single.html', context)




