# Generated by Django 5.0.6 on 2024-07-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0004_sellertbl_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttbl',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
