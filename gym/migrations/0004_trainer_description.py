# Generated by Django 4.2.6 on 2023-11-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_trainer_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='description',
            field=models.TextField(null=True),
        ),
    ]