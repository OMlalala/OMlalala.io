from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

#from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.input_path = 'content'
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
# production = 'root@localhost:22'
# dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
# env.cloudfiles_username = 'my_rackspace_username'
# env.cloudfiles_api_key = 'my_rackspace_api_key'
# env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
#env.github_pages_branch = "gh-pages"

# Port for `serve`
#PORT = 8000

# def clean():
#     """Remove generated files"""
#     if os.path.isdir(DEPLOY_PATH):
#         shutil.rmtree(DEPLOY_PATH)
#         os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican {input_path} -o {deploy_path} -s pelicanconf.py'.format(**env))

# def rebuild():
#     """`build` with the delete switch"""
#     local('pelican -d -s pelicanconf.py')

# def regenerate():
#     """Automatically regenerate site upon file modification"""
#     local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    local('cd {deploy_path} && python -m http.server'.format(**env))

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def pub():
    build()
    local('cd {deploy_path} && '
            'pwd && '
            #'git pu && '
            'git add --all . && '
            #'git st && '
            'git ci -am "updating by local. @OMlalala" && '
            #'git pu cafe gitcafe-page '
            'git pu && '
            'pwd '.format(**env)
          )

# def preview():
#     """Build production version of site"""
#     local('pelican -s publishconf.py')

# def cf_upload():
#     """Publish to Rackspace Cloud Files"""
#     rebuild()
#     with lcd(DEPLOY_PATH):
#         local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#               '-U {cloudfiles_username} '
#               '-K {cloudfiles_api_key} '
#               'upload -c {cloudfiles_container} .'.format(**env))

# @hosts(production)
# def publish():
#     """Publish to production via rsync"""
#     local('pelican -s publishconf.py')
#     project.rsync_project(
#         remote_dir=dest_path,
#         exclude=".DS_Store",
#         local_dir=DEPLOY_PATH.rstrip('/') + '/',
#         delete=True,
#         extra_opts='-c',
#     )

# def gh_pages():
#     """Publish to GitHub Pages"""
#     rebuild()
#     local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))
