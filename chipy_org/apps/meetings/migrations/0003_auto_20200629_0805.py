# Generated by Django 2.2.13 on 2020-06-29 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20200217_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='length_minutes',
            new_name='length',
        ),
    ]
