# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('affiliationId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('affiliation', models.CharField(help_text='as defined in eduPerson', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('buildingId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=256, null=True)),
                ('postalCode', models.CharField(max_length=16, null=True)),
                ('city', models.CharField(max_length=255)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('altitude', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('abbr', models.CharField(max_length=32, null=True)),
                ('ects', models.PositiveIntegerField(null=True)),
                ('description', models.TextField()),
                ('goals', models.TextField(null=True)),
                ('requirements', models.TextField(null=True)),
                ('level', models.CharField(choices=[('HBO-B', 'HBO-B'), ('HBO-M', 'HBO-M'), ('WO-B', 'WO-B'), ('WO-M', 'WO-M'), ('WO-D', 'WO-D')], max_length=8, null=True)),
                ('format', models.TextField(null=True)),
                ('language', models.CharField(choices=[('nl-NL', 'nl-NL'), ('en-US', 'en-US'), ('de-DE', 'de-DE')], max_length=2)),
                ('enrollment', models.TextField(null=True)),
                ('literature', models.TextField(null=True)),
                ('exams', models.TextField(null=True)),
                ('schedule', models.TextField(null=True)),
                ('link', models.URLField(null=True)),
                ('organization', models.CharField(max_length=255, null=True)),
                ('department', models.CharField(max_length=255, null=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courseresult',
            fields=[
                ('courseresultId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('grade', models.CharField(max_length=15, null=True)),
                ('comment', models.TextField(null=True)),
                ('passed', models.NullBooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('groupId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('type', models.CharField(choices=[('?LesGroep', '?LesGroep'), ('?LeerGroep', '?LeerGroep'), ('ou', 'ou'), ('affiliation', 'affiliation'), ('Generic', 'Generic')], max_length=32)),
                ('lastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grouprole',
            fields=[
                ('grouproleId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('member', 'member'), ('manager', 'manager'), ('administrator', 'administrator')], max_length=32)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Newsfeed',
            fields=[
                ('newsfeedId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='_newsfeed_groups_+', to='api.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Newsitem',
            fields=[
                ('newsitemId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('publishDate', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255, null=True)),
                ('image', models.URLField(null=True)),
                ('link', models.URLField(null=True)),
                ('content', models.TextField()),
                ('feeds', models.ManyToManyField(blank=True, related_name='items', to='api.Newsfeed')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('userId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('givenname', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('displayname', models.CharField(max_length=255)),
                ('commonname', models.CharField(max_length=255, null=True)),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('telephonenumber', models.CharField(max_length=32, null=True)),
                ('mobilenumber', models.CharField(max_length=32, null=True)),
                ('photoSocial', models.URLField(null=True)),
                ('photoOfficial', models.URLField(null=True)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('U', 'U'), ('X', 'X')], max_length=1, null=True)),
                ('organization', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('office', models.CharField(max_length=255, null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('affiliations', models.ManyToManyField(blank=True, to='api.Affiliation')),
                ('groups', models.ManyToManyField(blank=True, through='api.Grouprole', to='api.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('abbreviation', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('totalSeats', models.PositiveIntegerField(null=True)),
                ('totalWorkspaces', models.PositiveIntegerField(null=True)),
                ('availableWorkspaces', models.PositiveIntegerField(null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('altitude', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('buildingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='api.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('scheduleId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('startDateTime', models.DateTimeField(null=True)),
                ('endDateTime', models.DateTimeField(null=True)),
                ('description', models.TextField(null=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('buildingId', models.ManyToManyField(blank=True, related_name='_schedule_buildingId_+', to='api.Building')),
                ('courseId', models.ManyToManyField(blank=True, related_name='_schedule_courseId_+', to='api.Course')),
                ('groupId', models.ManyToManyField(blank=True, related_name='_schedule_groupId_+', to='api.Group')),
                ('lecturers', models.ManyToManyField(blank=True, related_name='_schedule_lecturers_+', to='api.Person')),
                ('roomId', models.ManyToManyField(blank=True, related_name='_schedule_roomId_+', to='api.Room')),
                ('userId', models.ManyToManyField(blank=True, related_name='_schedule_userId_+', to='api.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Testresult',
            fields=[
                ('testresultId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('lastModified', models.DateTimeField(auto_now=True)),
                ('assessmentType', models.CharField(max_length=255, null=True)),
                ('testDate', models.DateField()),
                ('grade', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('passed', models.NullBooleanField()),
                ('weight', models.PositiveSmallIntegerField(null=True)),
                ('courseId', models.ManyToManyField(blank=True, related_name='_testresult_courseId_+', to='api.Course')),
                ('courseresult', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testresults', to='api.Courseresult')),
                ('userId', models.ManyToManyField(blank=True, related_name='_testresult_userId_+', to='api.Person')),
            ],
        ),
        migrations.AddField(
            model_name='grouprole',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, through='api.Grouprole', to='api.Person'),
        ),
        migrations.AddField(
            model_name='courseresult',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Person'),
        ),
        migrations.AddField(
            model_name='course',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='courses', to='api.Group'),
        ),
        migrations.AddField(
            model_name='course',
            name='lecturers',
            field=models.ManyToManyField(blank=True, related_name='_course_lecturers_+', to='api.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='grouprole',
            unique_together=set([('person', 'group')]),
        ),
    ]
