from apps.blog.models import Post, PostView
from apps.users.models import User


def update_post_view(post_id, user_id, device_id):

    if user_id is not None:
        obj, created = PostView.objects.update_or_create(
            post_id=post_id,
            user_id=user_id,
        )
    elif device_id is not None:
        obj, created = PostView.objects.update_or_create(
            post_id=post_id,
            device_id=device_id
        )

    if created:
        post = Post.objects.get(id=post_id)
        post.view_count += 1
        post.save()
