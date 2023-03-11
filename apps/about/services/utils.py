from apps.about.models import NotificationView


def get_last_object(model_class):
    """
    Return the last object of given model class if at least one record exists
    """
    ads = model_class.objects.all()

    if ads.exists():
        return ads.order_by('-created_at').first()


def update_notification_view(notification_id, user_id):
    """
    Store or update information about that the user saw a given notification
    """

    if user_id is not None:
        obj, created = NotificationView.objects.update_or_create(
            notification_id=notification_id,
            user_id=user_id
        )
