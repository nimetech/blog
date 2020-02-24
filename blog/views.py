from django.shortcuts import render
# from django.views import generic
from blog.models import Post

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


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts      
    }
    return render(request, "category.html", context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post':post,
    }
    return render(request, "post_detail.html", context)