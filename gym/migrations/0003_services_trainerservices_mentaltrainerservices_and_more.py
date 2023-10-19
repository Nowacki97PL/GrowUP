# Generated by Django 4.2.6 on 2023-10-19 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_alter_dietician_dietician_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrainerServices',
            fields=[
                ('services_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gym.services')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.trainer')),
            ],
            options={
                'abstract': False,
            },
            bases=('gym.services',),
        ),
        migrations.CreateModel(
            name='MentalTrainerServices',
            fields=[
                ('services_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gym.services')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.mentaltrainer')),
            ],
            options={
                'abstract': False,
            },
            bases=('gym.services',),
        ),
        migrations.CreateModel(
            name='DieticianServices',
            fields=[
                ('services_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gym.services')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.dietician')),
            ],
            options={
                'abstract': False,
            },
            bases=('gym.services',),
        ),
    ]
