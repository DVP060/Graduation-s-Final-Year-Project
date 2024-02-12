# Generated by Django 4.1.3 on 2023-02-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0002_monument_cityid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=6, null=True),
        ),
    ]