# Generated by Django 3.0.8 on 2020-08-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0004_comblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comblog',
            name='last_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
