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


@pytest.mark.parametrize('pkg', [
    'apache2'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'apache2'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled
