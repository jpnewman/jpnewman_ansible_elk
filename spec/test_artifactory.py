
def test_filebeat_running_and_enabled(Service):
    filebeat = Service("filebeat")
    assert filebeat.is_running
    assert filebeat.is_enabled


def test_packetbeat_running_and_enabled(Service):
    packetbeat = Service("packetbeat")
    assert packetbeat.is_running
    assert packetbeat.is_enabled


def test_topbeat_running_and_enabled(Service):
    topbeat = Service("topbeat")
    assert topbeat.is_running
    assert topbeat.is_enabled
