# Generated by Django 4.2.6 on 2023-10-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='blog.image'),
        ),
    ]