# Generated by Django 3.0.2 on 2020-05-12 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0003_auto_20200512_2239'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='projects',
            new_name='project',
        ),
    ]