# Generated by Django 3.0.8 on 2020-08-04 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chitchat', '0006_remove_user_profile_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='about',
            field=models.TextField(default=' '),
        ),
    ]