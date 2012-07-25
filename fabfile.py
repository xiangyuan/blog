import time
from fabric.api import local, env
from fabric.contrib.project import rsync_project

env.hosts = ['ich-wars-nicht.ch']
env.path = '/var/www/dbrgn/blog/'

def push():
    local('git push')

def serve():
    local('run-rstblog serve')

def build():
    # Build HTML
    local('rm -rf _build/ && run-rstblog build')

    # Generate sitemaps
    local('python gensitemap.py > _build/sitemap.xml')

    # Minify CSS
    local('cssmin < _build/static/style.css > _build/static/style.min.css')
    local('mv _build/static/style.min.css _build/static/style.css')
    local('cssmin < _build/static/_pygments.css > _build/static/_pygments.min.css')
    local('mv _build/static/_pygments.min.css _build/static/_pygments.css')

    # Add timestamp to css files
    local('find _build -type f -exec sed -i "s/style.css/style.css?%s/g" {} \;' % int(time.time()))
    local('find _build -type f -exec sed -i "s/_pygments.css/_pygments.css?%s/g" {} \;' % int(time.time()))

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
