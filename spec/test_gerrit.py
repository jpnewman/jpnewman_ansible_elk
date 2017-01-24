# filebeat
def test_filebeat_running_and_enabled(Service):
    filebeat = Service("filebeat")
    assert filebeat.is_running
    assert filebeat.is_enabled


# packetbeat
def test_packetbeat_running_and_enabled(Service):
    packetbeat = Service("packetbeat")
    assert packetbeat.is_running
    assert packetbeat.is_enabled


# topbeat
def test_topbeat_running_and_enabled(Service):
    topbeat = Service("topbeat")
    assert topbeat.is_running
    assert topbeat.is_enabled


# log indexer
def test_ping_to_elk_server(Command):
    command = Command('ping -c 4 -q elk-server')
    assert command.rc == 0
    assert '0% packet loss' in command.stdout.rstrip()


def test_connection_to_redis_server(Command):
    command = Command('nc -z -v -w 5 elk-server 6379')
    assert command.rc == 0
    assert 'succeeded!' in command.stderr.rstrip()


# log shipper
def test_ping_to_lumberjack_log_shipper_server(Command):
    command = Command('ping -c 4 -q elk-log-001')
    assert command.rc == 0
    assert '0% packet loss' in command.stdout.rstrip()


def test_connection_to_lumberjack(Command):
    command = Command('nc -z -v -w 5 elk-log-001 5000')
    assert command.rc == 0
    assert 'succeeded!' in command.stderr.rstrip()


def test_connection_to_beats(Command):
    command = Command('nc -z -v -w 5 elk-log-001 5044')
    assert command.rc == 0
    assert 'succeeded!' in command.stderr.rstrip()


def test_connection_to_syslog(Command):
    command = Command('nc -z -v -w 5 elk-log-001 5545')
    assert command.rc == 0
    assert 'succeeded!' in command.stderr.rstrip()
