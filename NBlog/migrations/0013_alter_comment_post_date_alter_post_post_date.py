# Generated by Django 4.1.4 on 2023-05-09 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBlog', '0012_alter_comment_post_date_alter_post_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 0, 36, 53, 7467), max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 0, 36, 53, 7467), editable=False, max_length=50),
        ),
    ]
