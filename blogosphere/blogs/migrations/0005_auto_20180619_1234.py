# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-19 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_author_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='descripción'),
        ),
        migrations.AddField(
            model_name='author',
            name='description_es',
            field=models.TextField(blank=True, null=True, verbose_name='descripción'),
        ),
        migrations.AddField(
            model_name='author',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='descripción'),
        ),
        migrations.AddField(
            model_name='author',
            name='image_caption_en',
            field=models.TextField(blank=True, help_text='Leyenda de la imagen.', null=True, verbose_name='leyenda'),
        ),
        migrations.AddField(
            model_name='author',
            name='image_caption_es',
            field=models.TextField(blank=True, help_text='Leyenda de la imagen.', null=True, verbose_name='leyenda'),
        ),
        migrations.AddField(
            model_name='author',
            name='image_caption_fr',
            field=models.TextField(blank=True, help_text='Leyenda de la imagen.', null=True, verbose_name='leyenda'),
        ),
    ]
