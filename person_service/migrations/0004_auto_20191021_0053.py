# Generated by Django 2.2.6 on 2019-10-20 22:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('person_service', '0003_auto_20191021_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 22, 53, 26, 174931, tzinfo=utc)),
        ),
    ]