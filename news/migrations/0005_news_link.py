# Generated by Django 5.1.2 on 2024-10-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
