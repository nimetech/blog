from .models import Page

def show_pages_menu(context):
    pages_menu = Page.objects.filter(status = 1)
    return {'pages_menu': pages_menu}