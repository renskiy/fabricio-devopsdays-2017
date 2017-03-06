Vagrant.configure('2') do |config|

  config.vm.box = 'ubuntu/trusty64'

  config.vm.network 'private_network', type: 'dhcp'

  {
    "docker-1" => 8081,
    "docker-2" => 8082,
    "docker-3" => 8083,
  }.each do |host_name, public_port|
    config.vm.define host_name do |host|

      host.vm.hostname = host_name

      host.vm.network :forwarded_port, guest: 80, host: public_port

      # install Docker
      host.vm.provision 'docker', images: ["nginx:stable-alpine", "nginx:1.11-alpine"]

    end

  end

end
