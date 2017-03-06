from fabricio import tasks
from fabricio.apps.db.postgres import StreamingReplicatedPostgresqlContainer
from fabricio.misc import AvailableVagrantHosts

all_hosts = AvailableVagrantHosts(guest_network_interface='eth1')

postgres = tasks.DockerTasks(
    service=StreamingReplicatedPostgresqlContainer(
        name='postgres',
        image='postgres:9.6-alpine',
        pg_data='/data/fabricio_postgres',
        pg_hba='postgres/pg_hba.conf',
        pg_conf='postgres/postgresql.conf',
        pg_recovery='postgres/recovery.conf',
        pg_recovery_master_promotion_enabled=True,
        pg_recovery_wait_for_master_seconds=5,
        options=dict(
            volume='/data/fabricio_postgres:/data',
            env='PGDATA=/data',
            publish='5432:5432',
        ),
    ),
    hosts=all_hosts,
)
