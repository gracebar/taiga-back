# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_auto_20150629_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='Task',
            name='assigned_to_dummy',
            field=models.ManyToManyField(related_name='tasks_assigned_to_me_dummy', default=None, verbose_name='assigned to dummy', blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
