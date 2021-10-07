from django.contrib import admin

# Register your models here.
from .models import BlogCategory,Comment,Blog,Contact


admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Contact)