
def test_filebeat_running_and_enabled(Service):
    filebeat = Service("filebeat")
    assert filebeat.is_running
    assert filebeat.is_enabled
