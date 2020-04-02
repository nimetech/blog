from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag, Page

def published(modeladmin, request, queryset):
    queryset.update(status=1)
published.short_shortdescription = "Publish"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on', 'author', 'category', 'tags')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = [published]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on')
    search_fields = ['title', 'status', 'content']
    prepopulated_fields = { 'slug': ('title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Page,PageAdmin)