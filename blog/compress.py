from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(featured_image):
    im = Image.open(featured_image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'PNG', quality=70) 
    # create a django-friendly Files object
    new_image = File(im_io, name=featured_image.name)
    return new_image