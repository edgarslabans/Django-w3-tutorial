# Generated by Django 4.1.4 on 2023-07-19 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='joined_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
    ]
