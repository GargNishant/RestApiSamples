# Generated by Django 3.0.8 on 2020-08-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='deviceDetail',
            field=models.TextField(blank=True, default='NA'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
