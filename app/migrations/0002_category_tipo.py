# Generated by Django 3.0.6 on 2020-06-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tipo',
            field=models.CharField(default='', max_length=255),
        ),
    ]
