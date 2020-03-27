from django.shortcuts import render
# from django.views import generic
from blog.models import Post, Category, Tag, Page


def blog_index(request):
    # pages = Page.objects.filter(status = 1)
    latest = Post.objects.filter(status = 1).latest('created_on')
    # posts = Post.objects.filter(status = 1).order_by('-created_on')
    # exclude = Post.objects.filter(status = 1).exclude(latest).order_by('-created_on')
    exclude = Post.objects.filter(status = 1).order_by('-created_on')[4:]
    # if posts in latest:
    top_three = Post.objects.filter(status = 1).order_by('-created_on')[1:4]


    context = {
        # 'posts': posts,
        # 'pages': pages,
        'latest' : latest,
        'exclude' : exclude,
        'top_three' : top_three,
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
    context = {
        # 'posts_category' : posts_category,
        'posts' : posts,
        # 'posts_category' : posts,
    }
    return render(request, "category.html", context)


def tag_post(request, slug):
    posts = Post.objects.filter( tag__slug = slug, status = 1 )
    context = {
        'posts' : posts,
    }
    return render(request, "tag.html", context)

def blog_page(request, slug):
    page = Page.objects.get(slug=slug)
    context = {
        'page' : page,
    }
    return render(request, "page.html", context)