import os


import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_innobackupex_binaries(host):
    host.run_expect([255], 'qpress')
    host.run_expect([0], 'innobackupex -v')
