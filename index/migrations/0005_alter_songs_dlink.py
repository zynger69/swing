# Generated by Django 3.2 on 2021-10-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_songs_dlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='dlink',
            field=models.CharField(default='', max_length=255),
        ),
    ]
