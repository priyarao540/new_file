# Generated by Django 3.0.8 on 2020-09-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0021_auto_20200917_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='dataserializer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20, null=True)),
                ('emp_des', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
