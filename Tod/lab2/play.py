---
# Lab exercise

- name: Lab 2
  hosts: ovechkin
  tasks:
  - name: Create deploy group
    group: name=deploy state=present
  - name: create deploy user
    user: name=deploy-user group=deploy shell="/bin/bash" state=present
  - name: Install web server
    yum: name=httpd state=present
  - name: Start web server
    service: name=httpd state=started
  - name: Install index.html
    copy: dest=/var/www/html src="files/index.html"
#  - name: reboot host
#    reboot:
#      reboot_timeout: 60
#  - name: Install wget and git
#    yum: name=wget,git state=present
  - name: Clone git repo
    git: clone=yes repo='https://github.com/scmgalaxy/ansible-role-template' dest=/tmp
