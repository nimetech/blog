from .models import Page, Tag, Category

def pages_menu(context):
    pages_menu = Page.objects.filter(status = 1)
    return {'pages_menu': pages_menu}

def category_menu(context):
    cat_menu = Category.objects.all()
    return {'cat_menu': cat_menu}
