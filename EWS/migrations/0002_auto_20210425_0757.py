# Generated by Django 3.1.6 on 2021-04-25 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EWS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Iname',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Size',
        ),
        migrations.RemoveField(
            model_name='item',
            name='Type',
        ),
    ]