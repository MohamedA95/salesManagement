# Generated by Django 2.2.4 on 2019-08-19 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190818_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistics',
            options={'ordering': ['-name']},
        ),
    ]
