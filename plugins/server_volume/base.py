from systems.plugins.index import BasePlugin


class BaseProvider(BasePlugin('server_volume')):

    def store_related(self, instance, created, test):
        super().store_related(instance, created, test)
        if instance.type != 'device':
            self.mount_volume(instance)


    def mount_volume(self, instance):
        module = self.command.get_instance(
            self.command._module,
            self.manager.index.get_module_name(__file__)
        )
        mount_params = {
            'path': instance.name,
            'source': instance.location,
            'type': instance.type,
            'owner': instance.owner,
            'group': instance.group,
            'mode': instance.mode
        }
        if instance.options:
            mount_params['options'] = ",".join(instance.options)

        module.provider.exec_task(
            'mount',
            {
                "servers": "id={}".format(instance.server.id),
                "mounts": [ mount_params ]
            }
        )
