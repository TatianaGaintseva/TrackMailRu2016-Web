# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 16:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='modification_date')),
                ('likes_count', models.IntegerField(default=0, verbose_name='likes_count')),
                ('comments_count', models.IntegerField(default=0, verbose_name='comments_count')),
                ('title', models.CharField(default='none', max_length=100, verbose_name='event_title')),
                ('text', models.TextField(verbose_name='event_text')),
                ('object_id', models.PositiveIntegerField()),
                ('published', models.BooleanField(default=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user_to_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_to_show_event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]