# Generated by Django 5.0.6 on 2024-07-22 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0002_sellertbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttbl',
            name='selleridFK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sellerapp.sellertbl'),
        ),
    ]