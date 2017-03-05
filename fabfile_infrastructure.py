from fabric import api as fab, colors
from fabricio import tasks, docker
from fabricio.misc import AvailableVagrantHosts

all_hosts = AvailableVagrantHosts(guest_network_interface='eth1')

fab.env.roledefs.update(
    # you can set up default roles here
    web=all_hosts[:1],  # docker-1
)


@tasks.infrastructure
def docker2():
    fab.env.update(
        roledefs={
            'web': all_hosts[1:2],  # docker-2
        },
    )


@tasks.infrastructure(color=colors.red)
def docker3(account):
    web.registry = 'localhost:5000'
    web.account = account
    web.ssh_tunnel_port = 5000

    fab.env.update(
        roledefs={
            'web': all_hosts[2:3],  # docker-3
        },
    )

web = tasks.ImageBuildDockerTasks(
    service=docker.Container(
        name='web',
        image='nginx',
        options=dict(
            # publish='80:80',
        ),
    ),
    roles=['web'],
    account='renskiy',
)
