from django.urls import path
from django.conf.urls import url
from blog import views 

urlpatterns = [
    # path('', views.blog, name='blog'),
    # path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.blog_index, name='blog_index'),
    # path('post/<slug:slug>/',views.post_detail, name='post_detail' ),
    url(r'^posts/(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_post, name='category_post'),
    path('tag/<slug:slug>/', views.tag_post, name='tag_post'),
    # url(r'^tag/(?P<slug>[-\w]+)/$', views.tag_post, name='tag_post'),
    # path('<slug:slug>/', views.blog_page, name='blog_page'),
    url(r'^page/(?P<slug>[-\w]+)/$', views.blog_page, name='blog_page'),
    # url(r'^page/(?P<slug>[-\w]+)/$', views.blog_page, name='blog_page'),
]