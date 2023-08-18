# Generated by Django 4.1.4 on 2023-05-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBlog', '0010_alter_comment_post_date_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloger',
            name='bloger_bio',
            field=models.TextField(blank=True, help_text='Write about yourself', max_length=500, verbose_name='Biography'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default='2023-08-05 16:34:09', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default='2023-08-05 16:34:09', editable=False, max_length=50),
        ),
    ]
