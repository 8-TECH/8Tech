# Generated by Django 5.0.7 on 2024-08-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_club_officials_name_club_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='officials_name',
            field=models.CharField(default='8Tech', max_length=100),
        ),
    ]