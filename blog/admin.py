from django.contrib import admin
from .models import Category, Teg, Blog, Comment, Subscribe

admin.site.register(Category)
admin.site.register(Teg)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Subscribe)