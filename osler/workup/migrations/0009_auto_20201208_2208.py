# Generated by Django 3.1.2 on 2020-12-09 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workup', '0008_auto_20201207_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalworkup',
            name='will_return',
        ),
        migrations.RemoveField(
            model_name='workup',
            name='referral_location',
        ),
        migrations.RemoveField(
            model_name='workup',
            name='referral_type',
        ),
        migrations.RemoveField(
            model_name='workup',
            name='will_return',
        ),
    ]
