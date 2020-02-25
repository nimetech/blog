from django.db import models

# Create your models here.
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='children')
    
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

class Tag(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'blog_posts', default=1)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'posts', default='')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name= 'posts')
    tag = models.ManyToManyField(Tag, related_name= 'tags_post')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def tags(self):
        return "\n".join([t.name for t in self.tag.all()])
