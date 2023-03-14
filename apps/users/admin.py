from django.contrib import admin
from apps.users.models import Position, User, UserCodeConfirmation

# Register your models here.

admin.site.register(Position)
admin.site.register(User)
admin.site.register(UserCodeConfirmation)
