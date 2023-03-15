from django.contrib import admin

from apps.blog.models import Post, PostCategory, PostView, Interview


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'view_count')
    list_filter = ('category', )
    search_fields = ('title', )


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', )


class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'device_id', )


class InterviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', )


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(PostView, PostViewAdmin)
admin.site.register(Interview, InterviewAdmin)
