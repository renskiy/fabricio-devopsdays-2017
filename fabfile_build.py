from fabricio import tasks, docker
from fabricio.misc import AvailableVagrantHosts

all_hosts = AvailableVagrantHosts(guest_network_interface='eth1')
# all_hosts = ['127.0.0.1'] * 3

custom = tasks.ImageBuildDockerTasks(
    service=docker.Container(
        name='custom',
        image='nginx',
        options={
            # 'publish': '80:80',
        },
    ),
    hosts=all_hosts[:1],
    account='renskiy',
)
