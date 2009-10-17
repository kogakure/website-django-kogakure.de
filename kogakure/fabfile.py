#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is a deployment script for "Fabric" (0.9+), a python-based tool like
# Capistrano. You can get it at http://www.fabfile.org/
# Change the values in env.### and start the command with "fab", e.g.
# fab restart_server

from fabric.api import env, local, run

env.hosts = ['hostname.com']
env.server_path = '/path/to/bin'
env.project_path = '/path/to/django/project/root'
env.memcached_ip = '127.0.0.1' # IP of memcached
env.memcached_port = '1234' # Port of memcached
env.memcached_size = '20' # in MByte

def deploy():
    "Push local changes to server, pull changes on server, restart server"
    local('git push;')
    run('cd $(project_path)/; git pull; delpyc' % env, pty=True)
    restart_server()
    
def stop_server():
    "Stop Apache"
    run('$(server_path)/stop' % env, pty=True)

def start_server():
    "Start apache"
    run('$(server_path)/start' % env, pty=True)

def restart_server():
    "Restart Apache"
    run('$(server_path)/stop' % env, pty=True)
    run('$(server_path)/start' % env, pty=True)

def restart_memcached():
    "Restart Memcached, restart server"
    run('kill `pgrep -u $LOGNAME memcached`' % env, pty=True)
    run('/usr/local/bin/memcached -d -l $(memcached_ip) -m $(memcached_size) -p $(memcached_port)' % env, pty=True)
    restart_server()