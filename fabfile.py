from fabricio import tasks, docker
from fabricio.misc import AvailableVagrantHosts

all_hosts = AvailableVagrantHosts(guest_network_interface='eth1')

nginx = tasks.DockerTasks(
    service=docker.Container(
        name='nginx',
        image='nginx:stable-alpine',
        options={
            # 'publish': '80:80',
        },
    ),
    hosts=all_hosts[:1],
    # registry='docker.io',
    # account='renskiy',
    # migrate_commands=True,
    # backup_commands=True,
    # pull_command=True,
    # update_command=True,
    # revert_command=True,
)
