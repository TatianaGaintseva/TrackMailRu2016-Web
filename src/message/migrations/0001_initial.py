# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 17:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes_count', models.IntegerField(default=0, verbose_name='likes_count')),
                ('text', models.TextField(verbose_name='message_text')),
                ('published', models.BooleanField(default=True)),
                ('comments_count', models.IntegerField(default=0, verbose_name='comments_count')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='message_author')),
                ('chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Chat', verbose_name='message_chat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
