# Generated by Django 2.1.7 on 2019-03-18 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingrate',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shipping.Address'),
        ),
        migrations.AddField(
            model_name='shippingrate',
            name='basket_id',
            field=models.CharField(blank=True, db_index=True, max_length=32),
        ),
    ]