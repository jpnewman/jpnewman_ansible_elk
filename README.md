
# Ansible ELK Stack

This repo contains a vagrant file to create a ELK Stack via the following Ansible Galaxy roles: -

- geerlingguy.elasticsearch-curator
- geerlingguy.firewall
- geerlingguy.nginx
- geerlingguy.security
- jpnewman.common
- jpnewman.elasticsearch
- jpnewman.elk-filebeat
- jpnewman.elk-kibana
- jpnewman.elk-logstash-indexer
- jpnewman.elk-logstash-shipper
- jpnewman.elk-packetbeat
- jpnewman.elk-topbeat
- jpnewman.java
- jpnewman.json
- jpnewman.locale-timezone
- jpnewman.nginx
- jpnewman.redis

For more information look at the following readmes: -

- ```./.sublime-project/README.md```
- ```./Vagrantfiles/MiniStack/README.md```

# Referneces

- <https://ianunruh.com/2014/05/monitor-everything-part-3.html>
- <https://www.amazeelabs.com/en/blog/elasticsearch-reloaded>

# Install Vagrant Plugin

~~~bash
vagrant plugin install vagrant-triggers
vagrant plugin install vagrant-cachier
vagrant plugin install vagrant-hostmanager
~~~

# Install Python requirements

~~~bash
pip install -r requirements.txt
~~~

# Install Ansible Roles

~~~bash
ansible-galaxy install -r requirements.yml -p roles
~~~

## License

MIT / BSD

## Author Information

John Paul Newman
