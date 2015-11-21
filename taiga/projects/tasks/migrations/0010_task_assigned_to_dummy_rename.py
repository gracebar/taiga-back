# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_task_copy_assignedto_assingneddummy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='Task',
            name='assigned_to',
        ),
        migrations.RenameField(
            model_name='Task',
            old_name='assigned_to_dummy',
            new_name='assigned_to',
        ),
    ]

