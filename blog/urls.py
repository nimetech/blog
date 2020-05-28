from django.urls import path
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, PageSitemap
from blog import views 
# from .sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
    'pages' : PageSitemap,
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
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
]