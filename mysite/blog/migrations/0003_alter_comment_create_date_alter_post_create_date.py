# Generated by Django 4.1 on 2024-04-28 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_create_date_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 28, 11, 51, 46, 684456, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 28, 11, 51, 46, 684202, tzinfo=datetime.timezone.utc)),
        ),
    ]
