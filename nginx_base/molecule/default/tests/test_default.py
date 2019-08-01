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


def test_htdocs(host):
    f = host.file('/var/www')

    assert f.exists
    assert f.user == 'www-data'
    assert f.group == 'www-data'
    assert f.is_directory
    assert f.mode == 0o2775


def test_no_default_vhost(host):
    f = host.file('/etc/nginx/sites-enabled/default')

    assert not f.exists


def test_nginx_config(host):
    config = host.file("/etc/nginx/nginx.conf")
    assert config.contains("server_names_hash_bucket_size 256;")
    assert not config.contains("(.*)#(.*)server_names_hash_bucket_size")

    assert not config.contains("(.*)#(.*)ssl_protocols")  # poodle
    assert config.contains("ssl_protocols TLSv1 TLSv1.1 TLSv1.2;")  # poodle


@pytest.mark.parametrize('pkg', [
    'nginx'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'nginx'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
