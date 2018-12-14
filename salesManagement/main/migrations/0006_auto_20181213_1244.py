# Generated by Django 2.1.4 on 2018-12-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181213_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='id',
        ),
        migrations.AddField(
            model_name='batch',
            name='minselling',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='commission',
            name='product_name',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
