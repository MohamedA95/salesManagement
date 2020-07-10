# Generated by Django 3.0.7 on 2020-07-10 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200710_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Currency'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='product_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Product'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='batch_id',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(quant__gt=0), null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Batch'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product_type',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Product'),
        ),
    ]
