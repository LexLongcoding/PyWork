# Generated by Django 2.2 on 2021-02-17 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0004_auto_20210217_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses_app.Description'),
        ),
    ]
