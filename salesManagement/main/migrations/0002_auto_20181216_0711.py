# Generated by Django 2.1.4 on 2018-12-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='batch',
            name='quant',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='batch',
            name='uid',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='unitprice',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]