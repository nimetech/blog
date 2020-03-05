from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    # field = ['tag']
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on', 'author', 'category', 'tags')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    # def get_tag(self):


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    # pass

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)