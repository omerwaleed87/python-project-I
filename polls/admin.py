# Register your models here.

from django.contrib import admin

from .models import User, Type, Location, Purpose, Listing

admin.site.register([User, Type, Location, Purpose, Listing])
