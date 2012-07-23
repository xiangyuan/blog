from fabric.api import local, env
from fabric.contrib.project import rsync_project

env.hosts = ['ich-wars-nicht.ch']
env.path = '/var/www/dbrgn/blog/'

def push():
    local('git push')

def serve():
    local('run-rstblog serve')

def build():
    local('rm -rf _build/ && run-rstblog build')
    local('python gensitemap.py > _build/sitemap.xml')

def sync():
    rsync_project(remote_dir=env.path,
                  local_dir='_build/',
                  delete=True,
                  exclude=['*.py', '*.pyc', 'requirements.txt'])

def deploy():
    build()
    sync()

def publish():
    deploy()
    push()
