# Generated by Django 2.1.1 on 2018-09-02 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20180902_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musictrack',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='musictrack',
            name='updated_at',
        ),
    ]
