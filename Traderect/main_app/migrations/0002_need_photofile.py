# Generated by Django 2.2.5 on 2019-10-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='need',
            name='photofile',
            field=models.ImageField(blank=True, db_column='photoFile', null=True, upload_to='main_app/static/main_app/img/need'),
        ),
    ]