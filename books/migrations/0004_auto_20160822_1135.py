# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-22 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160818_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField()),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Category'),
        ),
    ]
