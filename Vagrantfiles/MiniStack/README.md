
# Referneces

- <https://www.elastic.co/guide/en/logstash/current/deploying-and-scaling.html>

# Requirements

The following Vagrant plugins can be used:

 - [vagrant-cachier](https://github.com/fgrehm/vagrant-cachier)
 - [vagrant-hostmanager](https://github.com/devopsgroup-io/vagrant-hostmanager)
 - [vagrant plugin](https://github.com/tmatilai/vagrant-timezone)

# Versions

- Vagrant 1.8.1
  - vagrant-berkshelf (4.1.0)
  - vagrant-cachier (1.2.1)
  - vagrant-hostmanager (1.8.1)
  - vagrant-omnibus (1.4.1)
  - vagrant-proxyconf (1.5.2)
  - vagrant-share (1.1.5, system)
  - vagrant-triggers (0.5.2)
  - vai (0.9.3)

# Run


> Makefile

~~~
make
~~~

> Vagrant

~~~
vagrant up
~~~

## Run, Specific tags

> vagrant needs to provision the machines first to create the inventory file

### Tag: common

~~~
ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook playbook.yml -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --tags "common"
~~~

### Tag: logstash-shipper

~~~
ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook playbook.yml -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --tags "logstash-shipper"
~~~

### Tag: test-app, only

~~~
ANSIBLE_HOST_KEY_CHECKING=false ansible-playbook playbook.yml -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --tags "test-app" --skip-tags "filebeat,topbeat,packetbeat"
~~~

# Spec

~~~
unbuffer make spec | tee >(ansi2html > spec.html)
~~~

# Boxes

|Box|Description|Vagrant Name|Ansible Host|
|---|---|---|---|---|
|```10.10.10.20```|Test Application|```app```|```test-app```|
|```10.10.10.11```|Logstash Shipper|```log```|```elk-log```|
|```10.10.10.10```|Logstash Indexer|```elk```|```elk-server```|
|```10.10.10.10```|Elasticsearch|```elk```|```elk-server```|


# Ports

|Server|Application|Type|Port|
|---|---|---|---|
|```10.10.10.11```|Logstash|beat|```5000 ```|
|```10.10.10.11```|Logstash|beats|```5044```|
|```10.10.10.11```|Logstash|syslog|```5545```|
|```10.10.10.10```|Redis|Redis|```6379```|
|```10.10.10.10```|Elasticsearch|transport.tcp.port|```9200```|
|```10.10.10.10```|Elasticsearch|http.port|```9200```|

# Create self-signed unsecured cert

~~~
openssl req -x509 -batch -nodes -newkey rsa:2048 -keyout ../../files/certs/notsecure.key -out ../../files/certs/notsecure.crt -config ../../files/certs/notsecure.cnf -days 1825
~~~

> Check cert

~~~
openssl x509 -in ../../files/certs/notsecure.crt -text
~~~

> Convert to PKCS8

~~~
openSSL pkcs8 -in ../../files/certs/notsecure.key -topk8 -nocrypt -out ../../files/certs/notsecure.pk8
~~~

## Redis

~~~
redis-cli -h 10.10.10.10 KEYS *
~~~

> Results

~~~
1) "topbeat"
~~~

~~~
redis-cli -h 10.10.10.10 PUBSUB CHANNELS
~~~

> Results

~~~
1) "logstash"
~~~

## Elasticsearch

~~~
curl '10.10.10.10:9200/_cat/indices?v'
~~~

> Results

~~~
health status index   pri rep docs.count docs.deleted store.size pri.store.size
	yellow open   .kibana   5   1        103            0    147.2kb        147.2kb
~~~

## Flow

### filebeat

filebeat **>** logstash shipper (```10.10.10.11:5044```) **>** redis (```10.10.10.10:6379```) **<** logstash indexer (```10.10.10.10```) **>** elasticsearch (```10.10.10.10:9200```)

### topbeat

topbeat **>** redis (```10.10.10.10:6379```) **<** logstash indexer (```10.10.10.10```) **>** elasticsearch (```10.10.10.10:9200```)
