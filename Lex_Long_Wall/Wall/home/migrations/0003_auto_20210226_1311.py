# Generated by Django 2.2 on 2021-02-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comment_wall_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wall_post',
            name='user_likes',
            field=models.ManyToManyField(related_name='liked_posts', to='home.User'),
        ),
    ]
