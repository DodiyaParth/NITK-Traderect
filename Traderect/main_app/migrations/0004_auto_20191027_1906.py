# Generated by Django 2.2.5 on 2019-10-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20191027_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renttransaction',
            name='transid',
            field=models.AutoField(db_column='transId', primary_key=True, serialize=False),
        ),
    ]