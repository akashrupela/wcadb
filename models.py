# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Competitions(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50)
    cityname = models.CharField(max_length=50)
    countryid = models.CharField(max_length=50)
    information = models.TextField(blank=True, null=True)
    year = models.SmallIntegerField()
    month = models.SmallIntegerField()
    day = models.SmallIntegerField()
    endmonth = models.SmallIntegerField()
    endday = models.SmallIntegerField()
    eventspecs = models.CharField(max_length=160, blank=True, null=True)
    wcadelegate = models.TextField(blank=True, null=True)
    organiser = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=240, blank=True, null=True)
    venueaddress = models.CharField(max_length=120, blank=True, null=True)
    venuedetails = models.CharField(max_length=120, blank=True, null=True)
    external_website = models.CharField(max_length=200, blank=True, null=True)
    cellname = models.CharField(max_length=45)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competitions'


class Continents(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    recordname = models.CharField(max_length=3)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    zoom = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'continents'


class Countries(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    continentid = models.CharField(max_length=50)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    zoom = models.SmallIntegerField()
    iso2 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Events(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=54)
    rank = models.IntegerField()
    format = models.CharField(max_length=10)
    cellname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'events'


class Formats(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=50)
    sort_by = models.CharField(max_length=255)
    sort_by_second = models.CharField(max_length=255)
    expected_solve_count = models.IntegerField()
    trim_fastest_n = models.IntegerField()
    trim_slowest_n = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'formats'


class Persons(models.Model):
    id = models.CharField(max_length=10)
    subid = models.SmallIntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    countryid = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'
        unique_together = (('id', 'subid'),)


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Ranksaverage(models.Model):
    personid = models.CharField(max_length=10)
    eventid = models.CharField(max_length=6)
    best = models.IntegerField()
    worldrank = models.IntegerField()
    continentrank = models.IntegerField()
    countryrank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ranksaverage'
        unique_together = (('eventid', 'personid'),)


class Rankssingle(models.Model):
    personid = models.CharField(max_length=10)
    eventid = models.CharField(max_length=6)
    best = models.IntegerField()
    worldrank = models.IntegerField()
    continentrank = models.IntegerField()
    countryrank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rankssingle'
        unique_together = (('eventid', 'personid'),)


class Results(models.Model):
    competitionid = models.CharField(max_length=32)
    eventid = models.CharField(max_length=6)
    roundid = models.CharField(max_length=1)
    pos = models.SmallIntegerField()
    best = models.IntegerField()
    average = models.IntegerField()
    personname = models.CharField(max_length=80, blank=True, null=True)
    personid = models.CharField(max_length=10)
    personcountryid = models.CharField(max_length=50, blank=True, null=True)
    formatid = models.CharField(max_length=1)
    value1 = models.IntegerField()
    value2 = models.IntegerField()
    value3 = models.IntegerField()
    value4 = models.IntegerField()
    value5 = models.IntegerField()
    regionalsinglerecord = models.CharField(max_length=3, blank=True, null=True)
    regionalaveragerecord = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'
        unique_together = (('competitionid', 'eventid', 'roundid', 'personid'),)


class Rounds(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    cellname = models.CharField(max_length=45)
    final = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rounds'


class Scrambles(models.Model):
    scrambleid = models.IntegerField(primary_key=True)
    competitionid = models.CharField(max_length=32)
    eventid = models.CharField(max_length=6)
    roundid = models.CharField(max_length=1)
    groupid = models.CharField(max_length=3)
    isextra = models.SmallIntegerField()
    scramblenum = models.IntegerField()
    scramble = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrambles'
