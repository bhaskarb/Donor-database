#!/usr/bin/env/python
__author__ = 'Bhaskar Bharath'

#import re
import logging 
import urllib2
import os
import config
from models.models import *
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template

class NewProject(webapp.RequestHandler):
    def post(self):
        proj_name=self.request.get('proj_name')
        proj_loc=self.request.get('proj_loc')
        proj_desc=self.request.get('proj_desc')
        projects = Project.all()
        projects.filter("Name =", proj_name)
        if projects.count():
            project = projects.fetch(limit = 1)[0]
            project.Location = proj_loc
            project.Desc = proj_desc
            project.put()
        else:
            print "New project Name=%s" %(proj_name)
            project = Project(parent=project_key(proj_name), Name=proj_name)
            project.Location = proj_loc
            project.Desc = proj_desc
            project.put()

###Create the steward for the project
        steward = Steward(parent = steward_key(config.uname), Email = config.uname, Project = project);
        steward.put()
        cats=Category.all()
        projects=Project.all()
##
        donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'steward.html')
        template_values = {
            'user_name' : config.uname,
            'cats' : cats,
            'projects' : projects,
            'donors' : Donor.all(),
            'receps' : Recipient.all(),
            'logmsg' : '',
            'logout' : users.create_logout_url('/'),
        }
        self.response.out.write(template.render(donorpath, template_values))

            
