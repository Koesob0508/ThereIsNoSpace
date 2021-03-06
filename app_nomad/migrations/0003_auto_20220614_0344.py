# Generated by Django 3.2.12 on 2022-06-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_nomad', '0002_auto_20220614_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='url',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coworking',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='coworking',
            name='url',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
