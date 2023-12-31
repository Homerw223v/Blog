# Generated by Django 4.1.4 on 2023-05-07 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NBlog', '0004_alter_comment_author_alter_comment_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloger',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='bloger',
            name='bloger_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default='2023-07-05 15:15:56', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default='2023-07-05 15:15:56', editable=False, max_length=50),
        ),
    ]
