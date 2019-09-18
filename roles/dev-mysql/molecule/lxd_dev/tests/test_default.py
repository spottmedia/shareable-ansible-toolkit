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


def test_mysql_config(host):
    config = host.file("/etc/mysql/mysql.conf.d/mysqld.cnf")
    assert config.contains("bind-address = 0.0.0.0")
    assert not config.contains("bind-address = 127.0.0.1")


def test_mysql_root_user_only_local(host):
    host.run_expect(
        [1],
        'echo `mysql -e "use mysql; SELECT user FROM user ' +
        'WHERE User like \"root\" and Host = \"%\";"` | grep "root"')


@pytest.mark.parametrize('user', [
    'root', 'vagrant', 'ubuntu'
])
def test_mysql_users(host, user):
    host.run_expect(
        [0],
        'echo `mysql -e "use mysql; SELECT user FROM user;"` | grep "{}"'
        .format(user))


@pytest.mark.parametrize('pkg', [
    'mysql-server'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'mysql'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
