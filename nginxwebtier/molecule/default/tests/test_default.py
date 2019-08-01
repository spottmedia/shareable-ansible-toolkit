import os
import pytest


import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_phpfpm(host):
    config = host.file("/etc/php/7.1/fpm/pool.d/www.conf")
    assert config.exists
    assert config.contains("listen = 127.0.0.1:7777")
    assert not config.contains("listen = /run/php/php7.0-fpm.sock")
    assert not config.contains("listen = /run/php/php7.1-fpm.sock")


@pytest.mark.parametrize('svc', [
    'nginx', 'php7.1-fpm'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
