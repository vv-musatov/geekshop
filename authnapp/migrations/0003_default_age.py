# Generated by Django 3.2.10 on 2022-01-30 14:54

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0002_user_model_extend"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 1, 14, 54, 27, 363368, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="age",
            field=models.PositiveIntegerField(default=18, verbose_name="возраст"),
        ),
    ]
