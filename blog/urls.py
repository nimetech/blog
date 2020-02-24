from django.urls import path
from blog import views 

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]