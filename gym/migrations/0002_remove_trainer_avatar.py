# Generated by Django 4.2.6 on 2023-10-29 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='avatar',
        ),
    ]
