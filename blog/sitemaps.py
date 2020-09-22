from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Page, Category, Tag

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"
    
    def items(self):
        return ['blog_index']
        
    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
  changefreq = "daily"
  priority = 0.5

  def items(self):
    return Post.objects.filter(status = 1)
      
  def lastmod(self, obj):
    return obj.updated_on

class PageSitemap(Sitemap):
  changefreq = "weekly"
  priority = 0.9

  def items(self):
    return Page.objects.all()

  def lastmod(self,obj):
    return obj.updated_on

class CategorySitemap(Sitemap):
  changefreq = "daily"
  priority = 0.7

  def items(self):
    return Category.objects.all()

class TagSitemap(Sitemap):
  changefreq = "daily"
  priority = 0.7

  def items(self):
    return Tag.objects.all()
