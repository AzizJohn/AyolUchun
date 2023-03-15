from django.contrib import admin

from apps.about.models import Feedback, Notification, NotificationView, Advertisement, UseTerm, Contact


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class NotificationViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'notification', 'user')


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'phone_number')


class UseTermAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'email')


# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(NotificationView, NotificationViewAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(UseTerm, UseTermAdmin)
admin.site.register(Contact, ContactAdmin)
