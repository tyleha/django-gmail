from fabric.api import env, abort, run
from fabric.contrib.project import rsync_project
from fabric.contrib.console import confirm
from fabric.decorators import runs_once
import os.path

# The user I want to log in with
env.user = 'uw'
anv.webapp_path - '/home/uw/gmail-stats/'
env.local_project_dir = os.path.dirname(env.real_fabfile)

def bluebox():
	env.name = 'bluebox'
	env.hosts = ['block647050-tha.blueboxgrid.com']

def touch_WSGI():
    """ Touches the wsgi file to trigger a refresh of the site """
    run('touch ' + env.webapp_path + 'gmailstats/wsgi.py')

def pull_github():
	run('cd '+env.webapp_path)
	run('git pull origin master')

#def restart_apache