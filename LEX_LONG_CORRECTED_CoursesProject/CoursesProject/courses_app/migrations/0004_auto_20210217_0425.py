# Generated by Django 2.2 on 2021-02-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0003_auto_20210217_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(default='this is the default now'),
            preserve_default=False,
        ),
    ]
