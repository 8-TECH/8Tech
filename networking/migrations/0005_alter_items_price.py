# Generated by Django 5.0.6 on 2024-07-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networking', '0004_remove_networking_price_items_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]