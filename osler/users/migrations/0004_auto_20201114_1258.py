# Generated by Django 3.1.2 on 2020-11-14 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201019_1527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name']},
        ),
    ]
