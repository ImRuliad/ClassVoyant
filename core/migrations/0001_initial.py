# Generated by Django 5.2.3 on 2025-07-01 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=200)),
                ('units', models.IntegerField()),
            ],
        ),
    ]
