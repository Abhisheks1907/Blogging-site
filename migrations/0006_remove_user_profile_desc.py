# Generated by Django 3.0.8 on 2020-08-04 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chitchat', '0005_auto_20200731_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='desc',
        ),
    ]
