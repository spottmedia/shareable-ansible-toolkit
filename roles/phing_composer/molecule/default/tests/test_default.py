import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_phing_version_doesnt_error_out(host):
    cmd = host.run("phing -v")
    assert cmd.stderr == ''
    assert cmd.stdout == '2.16.1'
