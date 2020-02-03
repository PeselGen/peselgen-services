# Generated by Django 3.0 on 2020-01-28 02:00

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetricsAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributes', jsonfield.fields.JSONField(default=dict)),
            ],
            options={
                'db_table': 'peselgen_attributes',
            },
        ),
    ]