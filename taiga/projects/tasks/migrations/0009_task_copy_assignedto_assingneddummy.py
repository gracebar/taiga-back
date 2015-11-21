# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.db import connection
from taiga.projects.userstories.models import *
from taiga.projects.tasks.models import *
from taiga.projects.issues.models import *
from taiga.projects.models import *
import sys
sys.setrecursionlimit(100000)

def copy_assignedto_to_assingnedtodummy(task_model):
    table_name = task_model._meta.db_table
    query = "select id from %s"%(table_name)
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor.fetchall():
        id = row[0]
        instance = task_model.objects.get(id=id)
        if instance.assigned_to is not None:
            instance.assigned_to_dummy = [instance.assigned_to]
            print("mapping values from assigned to dummy field")
        instance.save()


def fix_assign_dummy(apps, schema_editor):
    print("copying data from assigned to new field")
    copy_assignedto_to_assingnedtodummy(Task)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_task_assigned_to_dummy'),
    ]

    operations = [
        migrations.RunPython(fix_assign_dummy),
    ]
