# Generated by Django 4.1.4 on 2023-07-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_member_joined_date_remove_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
