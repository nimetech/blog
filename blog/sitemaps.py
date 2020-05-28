from django.contrib.sitemaps import Sitemap
from .models import Post, Page

class PostSitemap(Sitemap):
  changefreq = "weekly"
  priority = 0.9

  def items(self):
    return Post.objects.all()

  def lastmod(self, obj):
    return obj.updated_on

class PageSitemap(Sitemap):
  changefreq = "weekly"
  priority = 0.9

  def items(self):
    return Page.objects.all()

  def lastmod(self,obj):
    return obj.updated_on