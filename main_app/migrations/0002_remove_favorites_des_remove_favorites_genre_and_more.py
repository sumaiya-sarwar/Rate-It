# Generated by Django 4.1.1 on 2022-10-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='des',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='favorites',
            name='categories',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='favorites',
            name='description',
            field=models.TextField(default='None', max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default='None', max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='author',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='img',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='title',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
