# Generated by Django 2.1.7 on 2019-04-02 00:43

from django.db import migrations, models
import django.db.models.deletion
import systems.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('firewall_rule', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firewallrule',
            options={'ordering': ['name'], 'verbose_name': 'firewall rule', 'verbose_name_plural': 'firewall rules'},
        ),
        migrations.RemoveField(
            model_name='firewallrule',
            name='type',
        ),
        migrations.AddField(
            model_name='firewallrule',
            name='provider_type',
            field=models.CharField(editable=False, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='config',
            field=systems.models.fields.EncryptedDataField(default={}, editable=False),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='firewall',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='firewallrule_relation', to='firewall.Firewall'),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='id',
            field=models.CharField(editable=False, max_length=64, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='name',
            field=models.CharField(editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='state_config',
            field=systems.models.fields.EncryptedDataField(default={}, editable=False),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='updated',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='firewallrule',
            name='variables',
            field=systems.models.fields.EncryptedDataField(default={}, editable=False),
        ),
    ]
