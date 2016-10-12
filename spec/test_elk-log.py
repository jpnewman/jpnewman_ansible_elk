

# logstash
def test_logstash_running_and_enabled(Service):
    logstash = Service("logstash")
    assert logstash.is_running
    assert logstash.is_enabled


def test_logstash_config(Command):
    command = Command('service logstash configtest')
    # assert command.stdout.rstrip() == 'Configuration OK'
    assert command.rc == 0


def test_logstash_indexer_lumberjack_tcp_is_listening(Socket):
    assert Socket("tcp://:::5000").is_listening


def test_logstash_indexer_beats_tcp_is_listening(Socket):
    assert Socket("tcp://:::5044").is_listening


def test_logstash_indexer_syslog_tcp_is_listening(Socket):
    assert Socket("tcp://:::5545").is_listening


def test_logstash_indexer_syslog_udp_is_listening(Socket):
    assert Socket("udp://:::5545").is_listening

# packetbeat
# def test_packetbeat_running_and_enabled(Service):
#     packetbeat = Service("packetbeat")
#     assert packetbeat.is_running
#     assert packetbeat.is_enabled
#
# topbeat
# def test_topbeat_running_and_enabled(Service):
#     topbeat = Service("topbeat")
#     assert topbeat.is_running
#     assert topbeat.is_enabled
