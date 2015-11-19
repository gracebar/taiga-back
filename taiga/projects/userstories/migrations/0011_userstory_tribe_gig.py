# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userstories', '0010_remove_userstory_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='tribe_gig',
            field=django_pgjson.fields.JsonField(default=None, blank=True, null=True),
        ),
    ]
