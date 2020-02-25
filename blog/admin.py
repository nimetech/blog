from django.contrib import admin

# Register your models here.
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'updated_on', 'author', 'category')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    # def category(self):
    #     return ",".join([str(p) for p in self.category.all()])

                # return ",".join([str(p) for p in self.parent.all()])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # pass

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)