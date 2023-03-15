from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.users.models import User


@receiver(post_save, sender=User)
def review_create(sender, instance, created, **kwargs):
    if created:
        instance.get_token()

