# Generated by Django 4.2.6 on 2023-10-19 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_userprofile_entries_to_gym'),
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietician',
            name='dietician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
        migrations.AlterField(
            model_name='mentaltrainer',
            name='mental_trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
        ),
    ]