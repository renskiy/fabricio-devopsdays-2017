# fabricio-devopsdays-2017

Practical materials for using [Fabricio](https://github.com/renskiy/fabricio) as a Docker containers and services deploy tool.

## Slides

You can find slides with additional instructions [here](fabricio-master-class.pptx).

## Requirements

* Access to the Internet (you will have to use it in most scenarios)
* [Python](https://www.python.org/downloads/) 2.6 or 2.7
* pip ([macOS](http://softwaretester.info/install-and-upgrade-pip-on-mac-os-x/), [Windows](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation#pip-install), [Linux](https://packaging.python.org/install_requirements_linux/))
* (optional) virtualenv (`[sudo] pip install virtualenv`)
* (recommended) [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* (recommended) [Vagrant](https://www.vagrantup.com/downloads.html)
* (recommended) [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest)
* [Docker for Linux](https://docs.docker.com/engine/installation/linux/ubuntu/), [Docker for Mac](https://docs.docker.com/docker-for-mac/) or [Docker Toolbox](https://www.docker.com/products/docker-toolbox) for Windows*
* Registered account on [hub.docker.com](https://hub.docker.com)

\* Windows users cannot use "native" Docker and VirtualBox at the same time. This caused by incompatibility of VirtualBox with Microsoft Hyper-V technology used by Docker (by March 2017).

## Installation and setup

(optional) If you don't want to use VirtualBox and Vagrant, you can instead enable SSH access on your computer to allow Fabricio to deploy containers and services to the localhost. However, such way has some limitations in use (e.g. you can not try multi-host configurations like "PostgreSQL master-slave cluster").
    
Clone this repository and go to its directory:

    git clone https://github.com/renskiy/fabricio-devopsdays-2017.git
    cd fabricio-devopsdays-2017

(recommended) Create 3 Virtual Machines with Docker by running following command:

    vagrant up
    
Create and activate virtualenv (you can safely skip this step if you wish to install Fabricio for all users):
    
    # Linux and macOS
    virtualenv fabricio
    source fabricio/bin/activate
    
    # Windows
    virtualenv fabricio
    fabricio\Scripts\activate

Install [Fabricio](https://github.com/renskiy/fabricio#install):

    pip install --upgrade fabricio
    
Check if everything is OK:

    fab --version
    
(Windows only) If you are using Docker Machine (Docker Toolbox) then you should follow instructions from `docker-machine env` command to setup docker client.
    
Pull following Docker images (Linux users should add current user to 'docker' group to allow execute Docker commands without `sudo`):

    docker pull nginx:stable-alpine
    docker pull nginx:1.11-alpine
    docker pull registry:2

## Scenarios

List of scenarios which will be discussed during the master-class. Full list of commands used in each scenario can be found in [cmd_list.sh](cmd_list.sh).

### Hello World

    fab --list
    
Shows how to deploy and rollback basic containers. Available customization options (including tags, custom Docker registry, registry account, SSH tunneling, etc.).

### Building images

    fab --fabfile fabfile_build --list
    
How to build Docker image before deploy.

### Docker services (swarm mode)

    fab --fabfile fabfile_swarm --list
    
Docker services deploy. Parallel deploy. Failover deploy.

### Select infrastructure to deploy

    fab --fabfile fabfile_infrastructure --list
    
Defining roles and infrastructures. Per infrastructure customization.

### PostgreSQL master-slave cluster

    fab --fabfile fabfile_postgres --list

Deploying master-slave configuration of PostgreSQL. Configuration. Master promotion. Adding new slaves.

### Bonus scenario

    fab --fabfile fabfile_bonus --list
