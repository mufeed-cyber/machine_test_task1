from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(customertbl)

admin.site.register(carttbl)
admin.site.register(wishlistbl)