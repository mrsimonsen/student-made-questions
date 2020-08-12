# Generated by Django 3.1 on 2020-08-11 23:04

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(default=4, validators=[catalog.models.v_MA], verbose_name='Number of choices')),
            ],
        ),
        migrations.CreateModel(
            name='MC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField(default=4, validators=[catalog.models.v_MC], verbose_name='Number of choices')),
            ],
        ),
        migrations.RenameField(
            model_name='fb',
            old_name='num_blanks',
            new_name='num',
        ),
    ]
