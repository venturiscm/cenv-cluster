# Generated by Django 2.2 on 2019-04-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0004_domain_fullchain'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='valid_days',
            field=models.IntegerField(default=60),
        ),
    ]
