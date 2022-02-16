# Generated by Django 3.2.10 on 2022-02-16 21:47

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0006_alter_shopuser_activation_key_expires"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 2, 18, 21, 47, 53, 934278, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
