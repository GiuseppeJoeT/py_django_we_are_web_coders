# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('threads', '0002_subject_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('thread', models.OneToOneField(null=True, to='threads.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='PollSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(related_name='subjects', to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poll', models.ForeignKey(related_name='votes', to='polls.Poll')),
                ('subject', models.ForeignKey(related_name='votes', to='polls.PollSubject')),
                ('user', models.ForeignKey(related_name='votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
