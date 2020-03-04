from django.urls import path
from blog import views 

urlpatterns = [
    # path('', views.blog, name='blog'),
    # path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.blog_index, name='blog_index'),
    path('<slug:slug>/',views.post_detail, name='post_detail' ),
    path('category/<slug:slug>/', views.blog_category, name='blog_category'),

]