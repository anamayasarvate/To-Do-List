# Generated by Django 2.2.3 on 2019-07-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190722_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
