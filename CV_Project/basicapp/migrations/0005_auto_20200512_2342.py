# Generated by Django 3.0.2 on 2020-05-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0004_auto_20200512_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
