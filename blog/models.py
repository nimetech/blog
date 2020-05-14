from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children', default='')
    
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "category"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])
        # return self.name
    
    def get_absolute_url(self):
        return F"/category/{self.slug}/"

class Tag(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return F"/tag/{self.slug}/"

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'blog_posts', default=1)
    # content = models.TextField()
    featured_image = models.ImageField(upload_to='featured_image', default = 'featured_image/none.jpg')
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name= 'posts_category')
    tag = models.ManyToManyField(Tag, related_name= 'tags_post')

    class Meta:
        ordering = ['-created_on']
        get_latest_by = 'created_on'

    def __str__(self):
        return self.title

    def tags(self):
        return "\n".join([t.name for t in self.tag.all()])
    
    def get_absolute_url(self):
        return F"/posts/{self.slug}/"

class Page(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_page', default=1)
    content = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return F"/page/{self.slug}/"