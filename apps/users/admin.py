from django.contrib import admin
from apps.users.models import Position, User, UserCodeConfirmation


# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'username', )
    list_filter = ('auth_status', )
    search_fields = ('first_name', 'last_name', 'phone_number', 'username')


class UserCodeConfirmationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'is_confirmed', 'expired_at', )


admin.site.register(Position, PositionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserCodeConfirmation, UserCodeConfirmationAdmin)
