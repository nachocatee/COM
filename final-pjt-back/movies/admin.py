from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Movies)
admin.site.register(Reviews)
admin.site.register(Comments)