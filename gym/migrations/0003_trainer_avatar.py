# Generated by Django 4.2.6 on 2023-10-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_remove_trainer_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
