
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

## elk-server

~~~bash
testinfra -v test_elk-server.py --ssh-config=.ssh_config --sudo --hosts=elk-server
~~~

## elk-log-001

~~~bash
testinfra -v test_elk-log.py --ssh-config=.ssh_config --sudo --hosts=elk-log-001
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
