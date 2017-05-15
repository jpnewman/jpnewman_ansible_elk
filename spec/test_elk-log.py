# server
def test_disk_free_space(Command):
    command = Command("df -P / | awk '/%/ {print $5}' | sed -e 's/%//'")
    assert int(command.stdout.strip()) <= 95


# logstash
def test_logstash_running_and_enabled(Service):
    logstash = Service("logstash")
    assert logstash.is_running
    assert logstash.is_enabled


# def test_logstash_config(Command):
#     command = Command('/usr/share/logstash/bin/logstash -t -f /etc/logstash/conf.d --path.settings=/etc/logstash/')
#     assert command.rc == 0
#     # assert command.stdout.rstrip() == 'Configuration OK'


def test_logstash_indexer_lumberjack_tcp_is_listening(Socket):
    assert Socket("tcp://:::5000").is_listening


def test_logstash_indexer_beats_tcp_is_listening(Socket):
    assert Socket("tcp://:::5044").is_listening


def test_logstash_indexer_syslog_tcp_is_listening(Socket):
    assert Socket("tcp://:::5545").is_listening


def test_logstash_indexer_syslog_udp_is_listening(Socket):
    assert Socket("udp://:::5545").is_listening


# log indexer
def test_ping_to_elk_server(Command):
    command = Command('ping -c 4 -q elk-server')
    assert command.rc == 0
    assert '0% packet loss' in command.stdout.rstrip()


def test_connection_to_redis_server(Command):
    command = Command('nc -z -v -w 5 elk-server 6379')
    assert command.rc == 0
    assert 'succeeded!' in command.stderr.rstrip()


def test_redis_command_output(Command):
    command = Command('redis-cli -h elk-server ping')
    assert command.rc == 0
    assert command.stdout.rstrip() == 'PONG'


def test_connection_to_elasticsearch(Command):
    command = Command('nc -z -v -w 5 elk-server 9200')
    assert command.rc == 0
    assert 'succeeded!' in command.stderr.rstrip()


# packetbeat
# def test_packetbeat_running_and_enabled(Service):
#     packetbeat = Service("packetbeat")
#     assert packetbeat.is_running
#     assert packetbeat.is_enabled


# topbeat
# def test_topbeat_running_and_enabled(Service):
#     topbeat = Service("topbeat")
#     assert topbeat.is_running
#     assert topbeat.is_enabled
