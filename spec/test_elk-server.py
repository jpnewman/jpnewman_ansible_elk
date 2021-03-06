# server
def test_disk_free_space(Command):
    command = Command("df -P / | awk '/%/ {print $5}' | sed -e 's/%//'")
    assert int(command.stdout.strip()) <= 95


# elasticsearch
def test_elasticsearch_running_and_enabled(Service):
    elasticsearch = Service("elasticsearch")
    assert elasticsearch.is_running
    assert elasticsearch.is_enabled


def test_elasticsearch_is_listening(Ansible, Socket):
    hostvars = Ansible.get_variables()
    socket_addr = "{0}:9200".format(hostvars['ansible_host']) or "10.10.10.10:9200"
    assert Socket("tcp://{0}".format(socket_addr)).is_listening


def test_elasticsearch_log_for_errors(Command):
    command = Command("""
d1=$(date --date="-10 min" "+%Y-%m-%dT%H:%M")
d2=$(date "+%FT%R")
awk \
-v start="$d1" \
-v end="$d2" \
'$0 > start, $0 < end || $0 ~ d2' \
/var/log/elasticsearch/elasticsearch.log
""")
    assert '[ERROR' not in command.stdout.strip()


# redis server
# http://www.unixdaemon.net/tools/five-minutes-with-testinfra/
def test_redis_server_config_file(Sudo, File):
    with Sudo("root"):
        config_file = File('/etc/redis/redis.conf')
    assert config_file.contains('bind 127.0.0.1')  # TODO: make it a regex
    assert config_file.is_file


def test_redis_server_running_and_enabled(Sudo, Service):
    with Sudo("root"):
        redis_server = Service("redis-server")
    assert redis_server.is_running
    assert redis_server.is_enabled


def test_redis_server_socket_listening(Socket):
    socket = Socket('tcp://127.0.0.1:6379')
    assert socket.is_listening


def test_redis_command_output(Command):
    command = Command('redis-cli ping')
    assert command.rc == 0
    assert command.stdout.rstrip() == 'PONG'


def test_redis_log_for_errors(Command):
    command = Command("""
d1=$(date --date="-10 min" "+%Y-%m-%dT%H:%M")
d2=$(date "+%FT%R")
awk \
-v start="$d1" \
-v end="$d2" \
'$0 > start, $0 < end || $0 ~ d2' \
/var/log/redis/redis-server.log
""")
    assert '[ERROR' not in command.stdout.strip()


# http://redis.io/topics/admin
def test_redis_sysctl_overcommit_memory(Sysctl):
    overcommit_memory = Sysctl('vm.overcommit_memory')
    assert overcommit_memory == 1


def test_redis_sysctl_overcommit_memory_persistents(File):
    config_file = File('/etc/sysctl.conf')
    assert config_file.contains('vm.overcommit_memory=1')
    assert config_file.is_file


# def test_redis_transparent_hugepage_enabled(Command):
#     command = Command('cat /sys/kernel/mm/transparent_hugepage/enabled')
#     assert '[never]' in command.stdout.strip()


# def test_redis_transparent_hugepage_defrag(Command):
#     command = Command('cat /sys/kernel/mm/transparent_hugepage/defrag')
#     assert '[never]' in command.stdout.strip()


# kibana
def test_kibana_running_and_enabled(Service):
    kibana = Service("kibana4")
    assert kibana.is_running
    assert kibana.is_enabled


def test_kibana_is_listening(Socket):
    assert Socket("tcp://127.0.0.1:5601").is_listening


def test_kibana_log_for_errors(Command):
    command = Command("""
d1=$(date --date="-10 min" "+%Y-%m-%dT%H:%M")
d2=$(date "+%FT%R")
awk \
-v start="$d1" \
-v end="$d2" \
'$0 > start, $0 < end || $0 ~ d2' \
/var/log/nginx/kibana-error.log
""")
    assert '[ERROR' not in command.stdout.strip()


# nginx
def test_nginx_running_and_enabled(Service):
    nginx = Service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_is_listening(Socket):
    assert Socket("tcp://0.0.0.0:80").is_listening


def test_nginx_is_configtest(Sudo, Command):
    with Sudo("root"):
        # command.stdout does not contain [OK]. This is possiblly due to the way service writes it to the output.
        # command = Command('service nginx configtest')
        # assert '[ OK ]' in command.stdout.strip()
        command = Command('nginx -t')
    assert 'ok' in command.stderr.strip()
    assert 'successful' in command.stderr.strip()


def test_nginx_log_for_errors(Command):
    command = Command("""
d1=$(date --date="-10 min" "+%Y-%m-%dT%H:%M")
d2=$(date "+%FT%R")
awk \
-v start="$d1" \
-v end="$d2" \
'$0 > start, $0 < end || $0 ~ d2' \
/var/log/nginx/error.log
""")
    assert '[ERROR' not in command.stdout.strip()


# logstash
def test_logstash_indexer_running_and_enabled(Service):
    logstash = Service("logstash")
    assert logstash.is_running
    assert logstash.is_enabled


def test_logstash_log_for_errors(Command):
    command = Command("""
d1=$(date --date="-10 min" "+%Y-%m-%dT%H:%M")
d2=$(date "+%FT%R")
awk \
-v start="$d1" \
-v end="$d2" \
'$0 > start, $0 < end || $0 ~ d2' \
/var/log/logstash/logstash-plain.log
""")
    assert '[ERROR' not in command.stdout.strip()


# def test_logstash_config(Command):
#     command = Command('/usr/share/logstash/bin/logstash -t -f /etc/logstash/conf.d --path.settings=/etc/logstash/')
#     assert command.rc == 0
#     # assert command.stdout.rstrip() == 'Configuration OK'


# topbeat
# def test_topbeat_running_and_enabled(Service):
#     topbeat = Service("topbeat")
#     assert topbeat.is_running
#     assert topbeat.is_enabled
