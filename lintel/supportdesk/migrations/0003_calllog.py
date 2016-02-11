# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supportdesk', '0002_project_support_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_sid', models.CharField(max_length=100)),
                ('to_telephone', models.CharField(max_length=100)),
                ('from_telephone', models.CharField(max_length=100)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(null=True)),
                ('support_agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supportdesk.SupportAgent')),
            ],
        ),
    ]
