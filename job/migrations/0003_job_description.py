# Generated by Django 5.1.4 on 2024-12-14 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
    ]