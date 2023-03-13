# Generated by Django 4.1.7 on 2023-03-12 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_alter_section_options_alter_category_icon_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='lecturecomment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturecomment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lecture_comments', to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
    ]