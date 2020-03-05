from django.shortcuts import render
# from django.views import generic
from blog.models import Post, Category, Tag

# Create your views here.
# def blog(request):
#     return render(request, 'blog.html', {})

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, "index.html", context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post':post,
    }
    return render(request, "post_detail.html", context)

# def blog_category(request, category):
#     posts = Post.objects.get(
#         categories__name__slug = slug
#     ).order_by('-created_on')
#     context = {
#         'category': category,
#         'posts': posts,
#     }
#     return render(request, "category.html", context)

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