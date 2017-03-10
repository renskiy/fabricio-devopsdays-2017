from fabric import api as fab

from .infrastructures import TEST, PRODUCTION
from .services import service1, service2


@fab.task(name='full-deploy')
def full_deploy(**kwargs):
    """
    deploy all services
    """
    fab.execute(service1.deploy, **kwargs)
    fab.execute(service2.deploy, **kwargs)
