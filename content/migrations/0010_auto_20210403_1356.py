# Generated by Django 3.1.3 on 2021-04-03 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20210329_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='next_chapter',
        ),
        migrations.RemoveField(
            model_name='progress',
            name='previous_chapter',
        ),
    ]