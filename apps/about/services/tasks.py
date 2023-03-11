from celery import shared_task
from apps.about.services.utils import update_notification_view


@shared_task(name='update_notification_view')
def update_notification_view_task(notification_id, user_id):
    print("Notification view task begin")
    update_notification_view(notification_id, user_id)
    print("Notification view task end")
