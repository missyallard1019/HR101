# Generated by Django 3.1.3 on 2021-03-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210212_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='tag_line',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='transcript',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='video_embed',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='review',
            name='first_img',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='review',
            name='second_img',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='review',
            name='third_img',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='video',
            name='authors',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='video',
            name='embed',
            field=models.CharField(max_length=300),
        ),
    ]
