# Generated by Django 3.0.8 on 2020-09-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0015_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
