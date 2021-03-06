
# TestInfra specs for ELK Stack

<https://github.com/philpep/testinfra>

# Install Python requirements

~~~bash
pip install -r requirements.txt
~~~

# Run

## Run All

~~~bash
./run_all.sh
~~~

## Run All, HTML output

### Install dependencies

> Mac OS X

~~~
brew tap homebrew/dupes/expect
brew install homebrew/dupes/expect

pip install ansi2html
~~~

### Run

~~~
unbuffer ./run_all.sh | tee >(ansi2html > run_all.html)
~~~

## elk-server (MiniStack)

~~~bash
testinfra -v test_elk-server.py --ssh-config=.ssh_config --sudo --connection=ansible --ansible-inventory=../Vagrantfiles/MiniStack/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory --hosts='elk-server'
~~~

> The MiniStack should be created with vagrant first

## elk-log

~~~bash
testinfra -v test_elk-log.py --ssh-config=.ssh_config --sudo --hosts=elk-log
~~~

## Artifactory (parallel execution)

~~~bash
testinfra -n 2 -v test_artifactory.py --ssh-config=.ssh_config --sudo --hosts=art01
~~~

## Jenkins

~~~bash
testinfra -v test_jenkins.py --ssh-config=.ssh_config --sudo --hosts=jenkins-server
~~~

## Gerrit

~~~bash
testinfra -v test_gerrit.py --ssh-config=.ssh_config --sudo --hosts=gerrit-server
~~~

# HTML Output

## Install dependencies

> Mac OS X

~~~
brew tap homebrew/dupes/expect
brew install homebrew/dupes/expect

pip install ansi2html
~~~

## Run

~~~
unbuffer testinfra -v test_jenkins.py --ssh-config=.ssh_config --sudo --hosts=jenkins-server | tee >(ansi2html > jenkins.html)
~~~
