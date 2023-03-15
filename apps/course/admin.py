from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.common.models import Author
from .models import Category, SocialMedia, Course, CourseComment, Section, Lecture, LectureViewed, LectureComment, \
    Certificate, CourseUser


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'get_html_photo', 'email')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name')
    # list_editable = ('is_published',)
    list_filter = ('gender',)
    # prepopulated_fields = {"slug": ("firs_name",)}
    fields = (
        'gender', 'first_name', 'last_name', 'email', 'profile_pic', 'get_html_photo', 'bio', 'created_at',
        'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.profile_pic:
            return mark_safe(f"<img src='{object.profile_pic.url}' width=50>")

    get_html_photo.short_description = "Avatar_photo"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # list_editable = ('is_published',)
    # list_filter = ('gender',)
    # prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'icon', 'get_html_photo', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "Category_icon"


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'link', 'redirects', 'order')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    # prepopulated_fields = {"slug": ("name",)}
    fields = (
        'name', 'icon', 'link', 'redirects', 'order', 'get_html_photo', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' width=50>")

    get_html_photo.short_description = "Social Media icon"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'original_price', 'discounted_price', 'discount_expire_date', 'badge_id')
    list_display_links = ('id', 'title', 'author')
    search_fields = ('title', 'author')
    # list_editable = ('is_published',)
    # list_filter = ('gender',)
    #prepopulated_fields = {"slug": ("title",)}
    fields = (
        'title', 'badge_id', 'author', 'category_id', 'original_price', 'discounted_price', 'discount_expire_date',
        'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True


class CourseUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user')
    list_display_links = ('id', 'course', 'user')
    search_fields = ('course',)
    # list_editable = ('is_published',)
    # list_filter = ('gender',)
    # prepopulated_fields = {"slug": ("name",)}
    fields = (
        'user', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseUser, CourseUserAdmin)
admin.site.register(CourseComment)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(LectureViewed)
admin.site.register(LectureComment)
admin.site.register(Certificate)
