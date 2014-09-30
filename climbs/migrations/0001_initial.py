# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=512)),
                ('slug', models.SlugField(max_length=128)),
                ('current', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'businesses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Climb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=256)),
                ('current', models.BooleanField(default=True)),
                ('climb_type', models.IntegerField(blank=True, null=True, choices=[(0, 'Top rope'), (1, 'Lead'), (2, 'Bouldering')])),
                ('position', models.PositiveIntegerField(null=True, blank=True)),
                ('grade_type', models.IntegerField(blank=True, null=True, choices=[(0, 'Ewbanks')])),
                ('grade', models.CharField(max_length=16)),
                ('business', models.ForeignKey(to='climbs.Business')),
            ],
            options={
                'ordering': ['business', 'position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('like', models.NullBooleanField(default=None)),
                ('climb', models.ForeignKey(to='climbs.Climb')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rope',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'name/number')),
                ('current', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=256)),
                ('current', models.BooleanField(default=True)),
                ('climb_type', models.IntegerField(default=0, null=True, blank=True, choices=[(0, 'Top rope'), (1, 'Lead'), (2, 'Bouldering')])),
                ('position', models.PositiveIntegerField(null=True, blank=True)),
                ('business', models.ForeignKey(to='climbs.Business')),
            ],
            options={
                'ordering': ['business', 'position'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rope',
            name='wall',
            field=models.ForeignKey(to='climbs.Wall'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='climb',
            name='rope',
            field=models.ForeignKey(blank=True, to='climbs.Rope', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='climb',
            name='wall',
            field=models.ForeignKey(blank=True, to='climbs.Wall', null=True),
            preserve_default=True,
        ),
    ]
