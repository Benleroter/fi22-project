# Generated by Django 4.1.3 on 2022-11-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0003_showsearchfields_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='showsearchfields',
            name='Odour',
            field=models.BooleanField(default=False, verbose_name=' _Ononedour'),
        ),
        migrations.AlterField(
            model_name='showsearchfields',
            name='slug',
            field=models.SlugField(),
        ),
    ]
