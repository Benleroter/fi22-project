# Generated by Django 4.1.3 on 2022-12-05 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0009_show_showfunginotes2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='ShowFungiNotes2',
        ),
    ]
