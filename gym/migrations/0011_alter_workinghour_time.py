# Generated by Django 4.2.6 on 2023-10-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0010_workinghour_remove_appointment_hour_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinghour',
            name='time',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
