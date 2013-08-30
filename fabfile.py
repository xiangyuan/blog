# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import os
import os.path
import time
import SimpleHTTPServer
import SocketServer

from fabric.api import local, env
from fabric.contrib.project import rsync_project


PELICAN = 'pelican'
PELICANOPTS = ''

BASEDIR = os.getcwd()
INPUTDIR = os.path.join(BASEDIR, 'content')
OUTPUTDIR = os.path.join(BASEDIR, 'output')
DEVCONFFILE = os.path.join(BASEDIR, 'pelicanconf.py')
PUBCONFFILE = os.path.join(BASEDIR, 'publishconf.py')

PORT = 8000

env.hosts = ['dbrgn.ch']
env.path = '/var/www/blog2/'


def push():
    local('git push')


def build(target='publish'):
    CONFFILE = DEVCONFFILE if target == 'local' else PUBCONFFILE
    commands = [
        'rm -rf {}'.format(OUTPUTDIR),
        '{} --verbose {} -o {} -s {} {}'.format(PELICAN, INPUTDIR, OUTPUTDIR,
                                                CONFFILE, PELICANOPTS),
    ]
    local(' && '.join(commands))


def serve():
    # Server subclass with allow_reuse_address = True
    class TestServer(SocketServer.TCPServer):
        allow_reuse_address = True

    # Start SimpleHTTPServer
    os.chdir(OUTPUTDIR)
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = TestServer(('', PORT), handler)
    httpd.allow_reuse_address = True
    print('Serving at port {}'.format(PORT))
    httpd.serve_forever()


def prepare():
    # Minify CSS
    local('cssmin < {0}/theme/css/main.css > {0}/theme/css/main.min.css'.format(OUTPUTDIR))
    local('mv {0}/theme/css/main.min.css {0}/theme/css/main.css'.format(OUTPUTDIR))
    local('cssmin < {0}/theme/css/pygments.css > {0}/theme/css/pygments.min.css'.format(OUTPUTDIR))
    local('mv {0}/theme/css/pygments.min.css {0}/theme/css/pygments.css'.format(OUTPUTDIR))

    # Add timestamp to css files
    local('find %s -type f -exec sed -i "s/\(link.*\)main.css/\\1main.css?%s/g" {} \;' % (OUTPUTDIR, int(time.time())))
    local('find %s -type f -exec sed -i "s/\(link.*\)pygments.css/\\1pygments.css?%s/g" {} \;' % (OUTPUTDIR, int(time.time())))


def sync():
    localdir = OUTPUTDIR
    if not localdir.endswith('/'):
        localdir += '/'
    rsync_project(remote_dir=env.path,
                  local_dir=localdir,
                  delete=True,
                  exclude=['*.py', '*.pyc', 'requirements.txt'])


def deploy():
    build()
    prepare()
    sync()


def publish():
    deploy()
    push()
