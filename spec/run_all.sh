#!/usr/bin/env bash

echo "elk-server"
testinfra -v test_elk-server.py --ssh-config=$HOME/.ssh/config --sudo --hosts=elk-server

echo "elk-log-001"
testinfra -v test_elk-log.py --ssh-config=$HOME/.ssh/config --sudo --hosts=elk-log-001

echo "Artifactory"
testinfra -n 2 -v test_artifactory.py --ssh-config=$HOME/.ssh/config --sudo --hosts=art01,art02

echo "Jenkins"
testinfra -v test_jenkins.py --ssh-config=$HOME/.ssh/config --sudo --hosts=jenkins-server

echo "Gerrit"
testinfra -v test_gerrit.py --ssh-config=$HOME/.ssh/config --sudo --hosts=gerrit-server
