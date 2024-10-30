# Generated by Django 5.0.6 on 2024-07-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0006_course_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastPaper1_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='yea1_sem1_pastpaper',
            field=models.ManyToManyField(blank=True, to='academic.pastpaper1_1'),
        ),
    ]