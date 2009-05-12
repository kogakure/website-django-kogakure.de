#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a deployment script for "Fabric", a python-based tool like
# Capistrano. You can get it at http://www.nongnu.org/fab/
# Change the values in with config.xyz and start the command with "fab", e.g.
# fab restart_server

config.fab_hosts = ['hostname.com']
config.server_path = '/path/to/bin'
config.project_path = '/path/to/django/project/root'
config.memcached_ip = '127.0.0.1' # IP of memcached
config.memcached_port = '1234' # Port of memcached
config.memcached_size = '20' # in MByte

def deploy():
    "Push local changes to server, pull changes on server, restart server"
    local('git push;', fail='warn')
    run('cd $(project_path)/; git pull; delpyc', fail='warn')
    restart_server()
    
def stop_server():
    "Stop Apache"
    run('$(server_path)/stop', fail='warn')

def start_server():
    "Start apache"
    run('$(server_path)/start', fail='warn')

def restart_server():
    "Restart Apache"
    run('$(server_path)/stop', fail='warn')
    run('$(server_path)/start', fail='warn')

def restart_memcached():
    "Restart Memcached, restart server"
    run('kill `pgrep -u $LOGNAME memcached`', fail='warn')
    run('/usr/local/bin/memcached -d -l $(memcached_ip) -m $(memcached_size) -p $(memcached_port)', fail='warn')
    restart_server()