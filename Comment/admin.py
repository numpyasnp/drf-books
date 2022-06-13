from django.contrib import admin

from .models import Books, Comment

admin.site.register(Comment)
admin.site.register(Books)
