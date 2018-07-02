# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-25 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminBool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.IntegerField(default=0)),
                ('boolean', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='adminForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='adminMChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.IntegerField(default=0)),
                ('other', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=50)),
                ('txt', models.CharField(max_length=500)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminForm')),
            ],
        ),
        migrations.CreateModel(
            name='adminSChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.IntegerField(default=0)),
                ('other', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=50)),
                ('txt', models.CharField(max_length=500)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminForm')),
            ],
        ),
        migrations.CreateModel(
            name='adminTextA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.IntegerField(default=0)),
                ('label', models.CharField(max_length=50)),
                ('txt', models.CharField(max_length=500)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminForm')),
            ],
        ),
        migrations.CreateModel(
            name='adminTextF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.IntegerField(default=0)),
                ('label', models.CharField(max_length=50)),
                ('txt', models.CharField(max_length=50)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminForm')),
            ],
        ),
        migrations.CreateModel(
            name='mChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
                ('mChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminMChoice')),
            ],
        ),
        migrations.CreateModel(
            name='sChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=50)),
                ('sChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminSChoice')),
            ],
        ),
        migrations.AddField(
            model_name='adminbool',
            name='formulario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.adminForm'),
        ),
    ]
