# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-13 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_phone', models.CharField(max_length=14)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.Material')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
