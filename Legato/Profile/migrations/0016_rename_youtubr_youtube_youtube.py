# Generated by Django 3.2.4 on 2021-11-12 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0015_auto_20211113_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtube',
            old_name='youtubr',
            new_name='youtube',
        ),
    ]