# Generated by Django 3.2 on 2022-03-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bgm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='org_score',
            name='poster',
            field=models.TextField(default=''),
        ),
    ]
