# Hello world

# list of commands
fab --list
# deploy 'nginx' container
fab nginx
# list of running containers
docker ps
# deploy 'nginx' container (idempotency check)
fab nginx
# force container update
fab nginx:force=yes
# start container from the custom image tag
fab nginx:1.11-alpine
# call 'backup' command at the very first of deploy process
fab nginx:backup=yes
# skip 'migrate' step during deploy process
fab nginx:migrate=no
# rollback container to a previous version
fab nginx.rollback
# start local Docker registry
docker run -d -p 5000:5000 --name registry registry:2


# Building Docker images

# list of commands
fab --fabfile fabfile_build --list
# build custom image
fab --fabfile fabfile_build custom.prepare
# push built image to the registry (don't forget provide your registry account in fabfile_build.py)
fab --fabfile fabfile_build custom.push
# deploy 'custom' container
fab --fabfile fabfile_build custom.upgrade
# all actions at once: prepare -> push -> upgrade
fab --fabfile fabfile_build custom
# list of running containers
docker ps


# Docker services (swarm mode)

# list of commands
fab --fabfile fabfile_swarm --list
# swarm initialization
fab --fabfile fabfile_swarm swarm-init
# deploy 'nginx' service
fab --fabfile fabfile_swarm nginx
# replicas list of the 'nginx' service
docker service ps nginx
# parallel (concurrent) deploy (may not work on Windows)
fab --fabfile fabfile_swarm nginx --parallel


# Defining and selecting infrastructures

# list of commands
fab --fabfile fabfile_infrastructure --list
# deploy on the default infrastructure
fab --fabfile fabfile_infrastructure web
# deploy on the 'docker2' infrastructure
fab --fabfile fabfile_infrastructure docker2 web
# deploy on the 'docker2' infrastructure with auto-confirmation
fab --fabfile fabfile_infrastructure docker2.confirm web
# failing attempt to deploy on the 'docker2' infrastructure using parallel mode
fab --fabfile fabfile_infrastructure docker2 web --parallel
# success deploy on the 'docker2' infrastructure with auto-confirmation using parallel mode
fab --fabfile fabfile_infrastructure docker2 web.confirm --parallel
# deploy on the 'docker3' infrastructure providing registry account used with particular infrastructure
fab --fabfile fabfile_infrastructure docker3:account web
# attempting to deploy container on the infrastructure with no host provided
fab --fabfile fabfile_infrastructure no_hosts web


# PostgreSQL master-slave configuration (vagrant configuration required)

# list of commands
fab --fabfile fabfile_postgres --list
# failing attempt to deploy containers in a single mode
fab --fabfile fabfile_postgres postgres
# success deploy of PostgreSQL cluster using parallel mode
fab --fabfile fabfile_postgres postgres --parallel
# show process list on one of cluster containers
docker exec -ti postgres ps aux
# delete one of cluster containers
docker rm --force postgres
# remove data used by deleted container
sudo rm -rf /data/fabricio_postgres
# promote new master or add new slave
fab --fabfile fabfile_postgres postgres --parallel
