from fabric import colors
from fabricio import tasks

__all__ = []  # hack


@tasks.infrastructure
def TEST():
    pass


@tasks.infrastructure(color=colors.red)
def PRODUCTION():
    pass
