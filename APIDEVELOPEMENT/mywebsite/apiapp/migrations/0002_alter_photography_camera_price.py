# Generated by Django 4.0 on 2022-01-08 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='Camera_price',
            field=models.IntegerField(null=True),
        ),
    ]