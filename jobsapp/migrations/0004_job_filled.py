# Generated by Django 2.1.7 on 2019-04-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0003_job_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='filled',
            field=models.BooleanField(default=False),
        ),
    ]
