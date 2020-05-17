from django.shortcuts import render
import random
# from django.views import generic
from blog.models import Post, Category, Tag, Page
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_index(request):
    # pages = Page.objects.filter(status = 1)
    latest = Post.objects.filter(status = 1).latest('created_on')
    top_three = Post.objects.filter(status = 1).order_by('-created_on')[1:4]
    exclude = Post.objects.filter(status = 1).order_by('-created_on')[4:]
    posts = Post.objects.filter(status = 1).order_by('-created_on')
    recent_post = Post.objects.filter(status = 1).order_by('-created_on')[0:5]
    paginator = Paginator(exclude, 10) # Post per view set to 10 
    page = request.GET.get('page')
    try: 
        posts_view = paginator.page(page)
        
    except PageNotAnInteger:
        posts_view = paginator.page(1)
    except EmptyPage:
        posts_view = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        # 'pages': pages,
        'latest' : latest,
        'exclude' : exclude,
        'top_three' : top_three,
        'posts_view' : posts_view,
        'recent_post' : recent_post,
    }
    return render(request, "index.html", context)

def post_detail(request, slug):
    recent_post = Post.objects.filter(status = 1).order_by('-created_on')[0:5]
    post = Post.objects.get(slug=slug)
    category = post.category
    post_id = post.id
    similar = Post.objects.filter(category = category, status = 1).exclude(id = post_id).order_by('?')[:3]
    context = {
        'post':post,
        'recent_post' : recent_post,
        'similar' : similar,
    }
    return render(request, "post_detail.html", context)

def category_post(request,slug):
    posts = Post.objects.filter( category_id__slug = slug, status = 1 )
    recent_post = Post.objects.filter(status = 1).order_by('-created_on')[0:5]
    paginator = Paginator(posts, 10) # Post per view set to 10 
    page = request.GET.get('page')
    try: 
        posts_view = paginator.page(page)
        
    except PageNotAnInteger:
        posts_view = paginator.page(1)
    except EmptyPage:
        posts_view = paginator.page(paginator.num_pages)
    
    context = {
        # 'posts_category' : posts_category,
        'posts' : posts,
        'posts_view' : posts_view,
        # 'posts_category' : posts,
        'recent_post' : recent_post,
    }
    return render(request, "category.html", context)


def tag_post(request, slug):
    posts = Post.objects.filter( tag__slug = slug, status = 1 )
    recent_post = Post.objects.filter(status = 1).order_by('-created_on')[0:5]
    paginator = Paginator(posts, 10) # Post per view set to 10 
    page = request.GET.get('page')
    try: 
        posts_view = paginator.page(page)
        
    except PageNotAnInteger:
        posts_view = paginator.page(1)
    except EmptyPage:
        posts_view = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts,
        'posts_view' : posts_view,
        'recent_post' : recent_post,
    }
    return render(request, "tag.html", context)

def blog_page(request, slug):
    recent_post = Post.objects.filter(status = 1).order_by('-created_on')[0:5]
    page = Page.objects.get(slug=slug)
    context = {
        'page' : page,
        'recent_post' : recent_post,
    }
    return render(request, "page.html", context)