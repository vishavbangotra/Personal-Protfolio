# Generated by Django 3.0.2 on 2020-05-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20200410_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('summary', models.CharField(max_length=256)),
                ('github', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='skills_frameworks',
        ),
        migrations.DeleteModel(
            name='skills_languages',
        ),
        migrations.DeleteModel(
            name='skills_tools_vcs',
        ),
    ]