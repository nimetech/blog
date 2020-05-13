from django.shortcuts import render
# from django.views import generic
from blog.models import Post, Category, Tag, Page
from  django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_index(request):
    # pages = Page.objects.filter(status = 1)
    latest = Post.objects.filter(status = 1).latest('created_on')
    top_three = Post.objects.filter(status = 1).order_by('-created_on')[1:4]
    exclude = Post.objects.filter(status = 1).order_by('-created_on')[4:]
    posts = Post.objects.filter(status = 1).order_by('-created_on')
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
    }
    return render(request, "index.html", context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post':post,
    }
    return render(request, "post_detail.html", context)

def category_post(request,slug):
    posts = Post.objects.filter( category_id__slug = slug, status = 1 )
    
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
    }
    return render(request, "category.html", context)


def tag_post(request, slug):
    posts = Post.objects.filter( tag__slug = slug, status = 1 )

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
    }
    return render(request, "tag.html", context)

def blog_page(request, slug):
    page = Page.objects.get(slug=slug)
    context = {
        'page' : page,
    }
    return render(request, "page.html", context)