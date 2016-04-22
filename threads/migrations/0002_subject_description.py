# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='description',
            field=tinymce.models.HTMLField(default=b''),
        ),
    ]
