# Generated by Django 5.0.6 on 2024-07-23 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0003_producttbl_selleridfk'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellertbl',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
