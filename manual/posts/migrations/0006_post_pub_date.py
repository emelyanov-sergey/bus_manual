# Generated by Django 4.1.6 on 2023-03-07 23:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_group_post_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
