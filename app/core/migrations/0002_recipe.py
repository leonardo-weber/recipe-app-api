# Generated by Django 3.2.25 on 2024-11-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_minutes', models.IntegerField()),
                ('link', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]