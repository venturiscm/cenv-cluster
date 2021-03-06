# Generated by Django 2.2 on 2019-04-04 21:47

from django.db import migrations, models
import django.db.models.deletion
import systems.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('firewall', '0001_initial'),
        ('group', '0001_initial'),
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoadBalancer',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('config', systems.models.fields.EncryptedDataField(default={}, editable=False)),
                ('provider_type', models.CharField(editable=False, max_length=128, null=True)),
                ('variables', systems.models.fields.EncryptedDataField(default={}, editable=False)),
                ('state_config', systems.models.fields.EncryptedDataField(default={}, editable=False)),
                ('internal', models.BooleanField(default=False)),
                ('firewalls', models.ManyToManyField(editable=False, related_name='loadbalancer_relation', to='firewall.Firewall')),
                ('groups', models.ManyToManyField(related_name='loadbalancer_relation', to='group.Group')),
                ('network', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='loadbalancer_relation', to='network.Network')),
            ],
            options={
                'verbose_name': 'load_balancer',
                'verbose_name_plural': 'load_balancers',
                'db_table': 'cluster_load_balancer',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('network', 'name')},
            },
        ),
    ]
