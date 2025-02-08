# Generated by Django 5.1.6 on 2025-02-08 13:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=50)),
                ('recording_id', models.CharField(max_length=50)),
                ('fixation_id', models.CharField(max_length=50)),
                ('start_timestamp', models.FloatField()),
                ('end_timestamp', models.FloatField()),
                ('duration', models.FloatField()),
                ('fixation_detected_on_surface', models.BooleanField()),
                ('fixation_x', models.FloatField()),
                ('fixation_y', models.FloatField()),
                ('owner_id', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ecam_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'EcamData',
                'verbose_name_plural': 'EcamData',
                'db_table': 'EcamData',
            },
        ),
        migrations.CreateModel(
            name='Efis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=50)),
                ('recording_id', models.CharField(max_length=50)),
                ('fixation_id', models.CharField(max_length=50)),
                ('start_timestamp', models.FloatField()),
                ('end_timestamp', models.FloatField()),
                ('duration', models.FloatField()),
                ('fixation_detected_on_surface', models.BooleanField()),
                ('fixation_x', models.FloatField()),
                ('fixation_y', models.FloatField()),
                ('owner_id', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='efis_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'EfisData',
                'verbose_name_plural': 'EfisData',
                'db_table': 'EfisData',
            },
        ),
        migrations.CreateModel(
            name='Pfd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.CharField(max_length=50)),
                ('recording_id', models.CharField(max_length=50)),
                ('fixation_id', models.CharField(max_length=50)),
                ('start_timestamp', models.FloatField()),
                ('end_timestamp', models.FloatField()),
                ('duration', models.FloatField()),
                ('fixation_detected_on_surface', models.BooleanField()),
                ('fixation_x', models.FloatField()),
                ('fixation_y', models.FloatField()),
                ('owner_id', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pfd_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PfdData',
                'verbose_name_plural': 'PfdData',
                'db_table': 'PfdData',
            },
        ),
    ]
