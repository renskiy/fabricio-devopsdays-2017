from fabricio import docker, tasks

__all__ = []  # hack

service1 = tasks.DockerTasks(
    service=docker.Container(
        name='service1',
        image='nginx:stable-alpine',
    ),
    hosts=[],
)

service2 = tasks.DockerTasks(
    service=docker.Container(
        name='service2',
        image='nginx:stable-alpine',
    ),
    hosts=[],
)
