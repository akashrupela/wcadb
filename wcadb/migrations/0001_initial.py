# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cityname', models.CharField(max_length=50)),
                ('information', models.TextField(blank=True, null=True)),
                ('year', models.SmallIntegerField()),
                ('month', models.SmallIntegerField()),
                ('day', models.SmallIntegerField()),
                ('endmonth', models.SmallIntegerField()),
                ('endday', models.SmallIntegerField()),
                ('eventspecs', models.CharField(blank=True, max_length=160, null=True)),
                ('wcadelegate', models.TextField(blank=True, null=True)),
                ('organiser', models.TextField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, max_length=240, null=True)),
                ('venueaddress', models.CharField(blank=True, max_length=120, null=True)),
                ('venuedetails', models.CharField(blank=True, max_length=120, null=True)),
                ('external_website', models.CharField(blank=True, max_length=200, null=True)),
                ('cellname', models.CharField(max_length=45)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'competitions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Continents',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('recordname', models.CharField(max_length=3)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('zoom', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'continents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('zoom', models.SmallIntegerField()),
                ('iso2', models.CharField(blank=True, max_length=2, null=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=54)),
                ('rank', models.IntegerField()),
                ('format', models.CharField(max_length=10)),
                ('cellname', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formats',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sort_by', models.CharField(max_length=255)),
                ('sort_by_second', models.CharField(max_length=255)),
                ('expected_solve_count', models.IntegerField()),
                ('trim_fastest_n', models.IntegerField()),
                ('trim_slowest_n', models.IntegerField()),
            ],
            options={
                'db_table': 'formats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('primaryid', models.IntegerField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=10)),
                ('subid', models.SmallIntegerField()),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('countryid', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'persons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollsChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField()),
            ],
            options={
                'db_table': 'polls_choice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'polls_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ranksaverage',
            fields=[
                ('primaryid', models.IntegerField(primary_key=True, serialize=False)),
                ('personid', models.CharField(max_length=10)),
                ('best', models.IntegerField()),
                ('worldrank', models.IntegerField()),
                ('continentrank', models.IntegerField()),
                ('countryrank', models.IntegerField()),
            ],
            options={
                'db_table': 'ranksaverage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rankssingle',
            fields=[
                ('primaryid', models.IntegerField(primary_key=True, serialize=False)),
                ('personid', models.CharField(max_length=10)),
                ('best', models.IntegerField()),
                ('worldrank', models.IntegerField()),
                ('continentrank', models.IntegerField()),
                ('countryrank', models.IntegerField()),
            ],
            options={
                'db_table': 'rankssingle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('primaryid', models.IntegerField(primary_key=True, serialize=False)),
                ('pos', models.SmallIntegerField()),
                ('best', models.IntegerField()),
                ('average', models.IntegerField()),
                ('personname', models.CharField(blank=True, max_length=80, null=True)),
                ('personid', models.CharField(max_length=10)),
                ('value1', models.IntegerField()),
                ('value2', models.IntegerField()),
                ('value3', models.IntegerField()),
                ('value4', models.IntegerField()),
                ('value5', models.IntegerField()),
                ('regionalsinglerecord', models.CharField(blank=True, max_length=3, null=True)),
                ('regionalaveragerecord', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'results',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('cellname', models.CharField(max_length=45)),
                ('final', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'rounds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scrambles',
            fields=[
                ('scrambleid', models.IntegerField(primary_key=True, serialize=False)),
                ('groupid', models.CharField(max_length=3)),
                ('isextra', models.SmallIntegerField()),
                ('scramblenum', models.IntegerField()),
                ('scramble', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'scrambles',
                'managed': False,
            },
        ),
    ]
