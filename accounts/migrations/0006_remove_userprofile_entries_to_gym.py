# Generated by Django 4.2.6 on 2023-10-19 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='entries_to_gym',
        ),
    ]