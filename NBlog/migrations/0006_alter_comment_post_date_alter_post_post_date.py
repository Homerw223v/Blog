# Generated by Django 4.1.4 on 2023-05-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBlog', '0005_bloger_image_alter_bloger_bloger_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default='2023-07-05 16:00:49', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default='2023-07-05 16:00:49', editable=False, max_length=50),
        ),
    ]