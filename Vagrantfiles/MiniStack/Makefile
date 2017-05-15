
BASE_PATH := ../..

.PHONY: all init up provision destory spec
.IGNORE: spec

all: clean init up spec

clean:
	# rm -fR $(BASE_PATH)/roles

init:
	pip install -r $(BASE_PATH)/requirements.txt
	ansible-galaxy install -r $(BASE_PATH)/requirements.yml -p $(BASE_PATH)/roles

up: init
	vagrant up

provision:
	vagrant provision

destory:
	vagrant destroy -f

spec:
	cd ../../spec && \
	testinfra -v test_elk-server.py --ssh-config=.ssh_config --sudo --connection=ansible --ansible-inventory=../Vagrantfiles/MiniStack/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --hosts='elk-server'

	cd ../../spec && \
	testinfra -v test_elk-log.py --ssh-config=.ssh_config --sudo --connection=ansible --ansible-inventory=../Vagrantfiles/MiniStack/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --hosts='elk-log'

	cd ../../spec && \
	testinfra -v test_app.py --ssh-config=.ssh_config --sudo --connection=ansible --ansible-inventory=../Vagrantfiles/MiniStack/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --hosts='test-app'
