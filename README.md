# fabricio-devopsdays-2017

Practical materials

## Requirements
* Python 2.6 or 2.7
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest)
* [Docker for Linux](https://docs.docker.com/engine/installation/linux/ubuntu/), [Docker for Mac](https://docs.docker.com/docker-for-mac/) or [Docker Toolbox](https://www.docker.com/products/docker-toolbox) for Windows*
* [Fabricio](https://pypi.python.org/pypi?name=fabricio&:action=display) 0.3.21+
* Registered account on [hub.docker.com](https://hub.docker.com)

\* Windows users cannot use "native" Docker and VirtualBox at the same time. This caused by incompatibility of VirtualBox with Microsoft Hyper-V technology used by Docker.

## Installation and setup

Create 3 Virtual Machines with Docker by running following command:

    vagrant up

## Scenarios

List of scenarios which will be discussed during master-class.

### Hello World

    fab --list
    
Shows how to deploy and rollback basic containers. Available customization options (including tags, custom Docker registry, registry account, SSH tunneling, etc.).

### Building images

    fab --fabfile fabfile_build --list
    
How to build Docker image before deploy.

### Docker services (swarm mode)

    fab --fabfile fabfile_swarm --list
    
Docker services deploy. Parallel deploy. Failover deploy.

### Infrastructures

    fab --fabfile fabfile_infrastructure --list
    
Defining roles and infrastructures. Per infrastructure customization.

### (optional) PostgreSQL master-slave cluster

    fab --fabfile fabfile_postgres --list

Deploying master-slave configuration of PostgreSQL. Configuration. Master promotion. Adding new slaves.
