# Generated by Django 4.1.1 on 2022-09-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='boolean',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='response',
            name='whom_id',
            field=models.IntegerField(default=0),
        ),
    ]
