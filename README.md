# ansible_skeleton
Skeleton for basic Ansible usage


## Installation basics
Ensure Ansible is installed. Always follow doc: https://docs.ansible.com/ansible/2.5/installation_guide/intro_installation.html

To check for already installed Ansible in Ubuntu:
  `apt -qq list ansible`
Output should look something like this:
  `ansible/bionic,bionic,now 2.5.1+dfsg-1 all [installerat]`


RHEL and CentOS

    RHEL7: $ sudo subsription-manager repos --enable rhel-7-server-ansible-2.5-rpms
    sudo yum install ansible


Ubuntu and such

    sudo apt install ansible (or apt-get install ansible)

Macintosh

    sudo easy_install pip
    sudo pip install ansible


## Inventory

If the location given to -i in Ansible is a directory (or as so configured in ansible.cfg), Ansible can use multiple inventory sources at the same time. When doing so, it is possible to mix both dynamic and statically managed inventory sources in the same ansible run. Instant hybrid cloud!


### OpenStack

Inventory script included in this repo, from: https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/openstack_inventory.py

    chmod +x openstack_inventory.py

The script should now be usable

    ./openstack_inventory.py --list

Check if you can connect to all hosts

    ansible -i openstack_inventory.py all -m ping
