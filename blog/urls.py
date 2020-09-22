from django.urls import path
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, PageSitemap, CategorySitemap, TagSitemap, StaticViewSitemap
from blog import views 
# from .sitemaps import PostSitemap
from .robots_txt import robots_txt

sitemaps = {
    'posts': PostSitemap,
    'pages' : PageSitemap,
    'tags' : TagSitemap,
    'categories' : CategorySitemap,
    'static' : StaticViewSitemap,
}


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('post/<slug:slug>/',views.post_detail, name='post_detail' ),
    url(r'^post/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_post, name='category_post'),
    path('tag/<slug:slug>/', views.tag_post, name='tag_post'),
    # url(r'^tag/(?P<slug>[-\w]+)/$', views.tag_post, name='tag_post'),
    # path('<slug:slug>/', views.blog_page, name='blog_page'),
    url(r'^page/(?P<slug>[-\w]+)/$', views.blog_page, name='blog_page'),
    # url(r'^page/(?P<slug>[-\w]+)/$', views.blog_page, name='blog_page'),
    url(r'^sitemap\.xml', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
    url(r'^robots\.txt', robots_txt),
    # path("robots.txt", robots_txt),
]
