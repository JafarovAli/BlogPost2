from django.shortcuts import render
from django.db.models import Q 
from .models import Category, Post, Author,contact

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def contact(request):
    ContactName = contact.objects.get()
    context ={
        'ContactName':ContactName,
    }

    return render(request,'Contact.html',context)   
    
def postlistauthor (request,author_id):
    posts = Post.objects.filter(author_id=author_id).order_by('-timestamp')
    author = Author.objects.get(user_id = author_id)

    context = {
        'posts': posts,
        'author' : author,

    }
    return render(request, 'postlist_author.html', context)
    

def homepage (request):
    categories = Category.objects.all()[0:5]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'homepage.html',context)



    
def post (request,slug):
    post = Post.objects.get(slug = slug)
    latest = Post.objects.order_by('-timestamp')[:3]
    context = {
        'post': post,
        'latest': latest,
    }
    return render(request, 'post.html', context)


def about (request):
    return render(request, 'about_page.html')
    
def Contact (request):
    return render(request, 'Contact.html')

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'object_list': queryset
    }
    return render(request, 'search_bar.html', context)

def SearchAbout(request):
    qset= about.objects.all()
    qry= request.GET.get('q')
    if qry:
        queryset = queryset.filter(
            Q(title__icontains=qry) |
            Q(overview__icontains=qry)
        ).distinct()
    context = {
        'object_list1': qset
    }
    return render(request,'Search_About.html',context)

    



def postlist (request,slug):
    category = Category.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[category])

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_list.html', context)



def allposts(request):
    posts = Post.objects.order_by('-timestamp')

    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)



