from fabricio import tasks
from fabricio.apps.db.postgres import StreamingReplicatedPostgresqlContainer
from fabricio.misc import AvailableVagrantHosts

all_hosts = AvailableVagrantHosts(guest_network_interface='eth1')

db = tasks.DockerTasks(
    service=StreamingReplicatedPostgresqlContainer(
        name='postgres',
        image='postgres:9.6-alpine',
        pg_data='/data',
        pg_hba='postgres/pg_hba.conf',
        pg_conf='postgres/postgresql.conf',
        pg_recovery='postgres/recovery.conf',
        pg_recovery_master_promotion_enabled=True,
        options=dict(
            volume='/data:/data',
            env='PGDATA=/data',
            publish='5432:5432',
        ),
    ),
    hosts=all_hosts,
)
