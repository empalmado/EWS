# Generated by Django 3.1.6 on 2021-04-25 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0003_auto_20210425_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Iname',
            new_name='ProductName',
        ),
    ]