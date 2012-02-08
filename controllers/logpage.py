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

class LogPage(webapp.RequestHandler):
    def post(self):
        user_email = self.request.get('user_email')
        user_type = self.request.get('user_type')
        project_name = self.request.get('project')
        config.uname=user_email
        if user_type == "Donor":
            user = Donor.all()
            user.filter("Email =", user_email);
            if not user.count():
                donor = Donor(parent = donor_key(user_email), Email = user_email);
                donor.put()
                self.response.out.write("New Donor %s" %(user_email))
            else:
                self.response.out.write("Donor %s" %(user_email))
        elif user_type == "Steward":
            user = Steward.all()
            if project_name == "":
                donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'newsteward.html')
                template_values= {
                    'user_name' : user_email,
                    'logout' : users.create_logout_url('/'),
                }          
                self.response.out.write(template.render(donorpath, template_values))
            else:
                logging.debug("Name=" + project_name + "#")
                project=Project.all().filter("Name =", project_name).fetch(1)[0]
#                print "Project Name = %s aa %s aa" %(project.Name, config.uname)
                user.filter("Email =", user_email)
                user.filter("Project =", project)
                if not user.count():
                    steward = Steward(parent = steward_key(user_email), Email = user_email, Project = prj);
                    steward.put()
                else:
                    steward = user.fetch(limit = 1)
                donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'steward.html')
                template_values = {
                    'user_name' : user_email,
                    'cats' : Category.all(),
                    'projects' : Project.all(),
                    'donors' : Donor.all(),
                    'receps' : Recipient.all(),
                    'logmsg' : '',
                    'logout' : users.create_logout_url('/'),
                }
                self.response.out.write(template.render(donorpath, template_values))
        elif user_type == "Recipient":
            user = Recipient.all()
            proj_key = project_key(project_name)
            user.filter("Name =", user_email);
            user.filter("Project =", proj_key)
            if not user.count():
                recipient = Recipient(parent = recipient_key(user_email), Name = user_email, Project = proj_key);
                recipient.put()
                self.response.out.write("New Recipient %s" %(user_email))
            else:
                self.response.out.write("Recipient %s" %(user_email))
        else:
             self.response.out.write("Unknown class %s" %(user_email))

    def debug(self):
        users=DbUser.all()
        for user in users:
             self.response.out.write("%s, %s\n" %(user.Email, user.Type))
            
            
            

