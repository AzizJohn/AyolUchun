from django.contrib import admin

from apps.about.models import Feedback, Notification, NotificationView, Advertisement, UseTerm, Contact


# Register your models here.
admin.site.register(Feedback)
admin.site.register(Notification)
admin.site.register(NotificationView)
admin.site.register(Advertisement)
admin.site.register(UseTerm)
admin.site.register(Contact)
