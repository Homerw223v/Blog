# Generated by Django 4.1.4 on 2023-05-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBlog', '0002_alter_comment_post_date_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default='2023-04-05 16:06:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default='2023-04-05 16:06:49', editable=False, max_length=50),
        ),
    ]