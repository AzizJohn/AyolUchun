from django.contrib import admin

from .models import Post, PostCategory, PostView, Interview

# Register your models here.
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(PostCategory)
admin.site.register(Interview)
