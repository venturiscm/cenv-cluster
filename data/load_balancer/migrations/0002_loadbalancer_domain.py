# Generated by Django 2.2 on 2019-04-06 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0005_domain_valid_days'),
        ('load_balancer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadbalancer',
            name='domain',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='loadbalancer_relation', to='domain.Domain'),
        ),
    ]
