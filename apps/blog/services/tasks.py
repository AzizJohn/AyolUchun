from celery import shared_task
from apps.blog.services.utils import update_post_view


@shared_task(name='update_post_view')
def update_post_view_task(post_id, user_id, device_id):
    print("Post Counter task begin")
    update_post_view(post_id, user_id, device_id)
    print("Post Counter task end")
