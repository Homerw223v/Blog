# Generated by Django 4.1.4 on 2023-05-04 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBlog', '0003_alter_comment_post_date_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='NBlog.bloger'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(default='2023-04-05 16:12:42', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default='2023-04-05 16:12:42', editable=False, max_length=50),
        ),
    ]
