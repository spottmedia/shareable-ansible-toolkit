# shareable-ansible-toolkit
Ansible roles looselly packed together to serve as convenience provisioning base for spottmedia machines


## Noteworthy members of the pack

### Mysql 8 

works on Ubuntu Bionic (might work on Debians in general, but not tested)

We've been pulling our hairs out to automate mysql installation using their recipes, and finally have found a post of a good man Geert:
https://geert.vanderkelen.org/2018/mysql8-unattended-dpkg/

and assembled it into our toolkit.

you need to call `dev-mysql8` role, which in turn will also install xtrabackup for mysql8 as a dependency, 
which we think is pretty much mandatory for AdminOps, and thus have included it by default.
`Dev` in the name suggests it doesn't really pay attention to security, and have to be wrapped with hardening roles, to be put into production, 
however even with that in mind it only listens on 127.0.0.1 for both mysql-exposed ports. Keep that in mind when using in clustered setup.

#### Instructions

requirements.yaml

```YAML

- src: https://github.com/spottmedia/shareable-ansible-toolkit.git
  scm: git
  version: origin/master
  
```

playbook.yaml

```YAML

- name: Converge for mysql 8 servers
  hosts: mysqls8
  vars:
    mysql_root_password: 'password'

  roles:
    - shareable-ansible-toolkit/dev-mysql8

  tags:
    - mysql8-servers
  
```

then simply converge
