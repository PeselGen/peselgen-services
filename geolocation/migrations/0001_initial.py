# Generated by Django 3.0 on 2020-05-20 00:02

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.CharField(max_length=30)),
                ('geojson', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'db_table': 'peselgen_geolocation',
            },
        ),
        migrations.CreateModel(
            name='GeolocationService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
