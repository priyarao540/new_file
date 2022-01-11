# Generated by Django 3.0.8 on 2020-09-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gauranj', '0011_auto_20200903_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentsnumber', models.CharField(max_length=25, null=True)),
                ('departments_head', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='sub',
        ),
        migrations.CreateModel(
            name='comapnyone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=25, null=True)),
                ('departmentinfo', models.ManyToManyField(blank=True, related_name='department_data', to='gauranj.departments')),
            ],
        ),
    ]