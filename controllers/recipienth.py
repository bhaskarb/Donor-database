#!/usr/bin/env/python
__author__ = 'Bhaskar Bharath'

#import re
import urllib2
import os
import config
from models.models import *
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template

class NewRecipient(webapp.RequestHandler):
    def post(self):
        recep_name=self.request.get('recep_name')
        recep_type=self.request.get('recep_type')
        recep_desc=self.request.get('recep_desc')
        recep_pname=self.request.get('recep_proj')
        projects=Project.all()
        projects.filter("Name =", recep_pname);
        recipients=Recipient.all()
        recipients.filter("Name =", recep_name);
        recipients.filter("Project =", recep_pname);
        if not recipients.count():
            project = projects.fetch(limit = 1)[0]
            recipient = Recipient(parent = recipient_key(recep_name, project), Name=recep_name, Project=project);        
            recipient.Type=recep_type
            recipient.Desc=recep_desc
            recipient.put()
            logmsg="Added New Recipient %s" %(recep_name)
        else:
            recipient=recipient.fetch(limit = 1)[0]
            recipient.Type=recep_type
            recipient.Desc=recep_desc
            logmsg="Updated Recipient %s" %(recep_name)
        cats=Category.all()
        projects=Project.all()
        donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'steward.html')
        template_values = {
            'user_name' : config.uname,
            'cats' : cats,
            'projects' : projects,
            'donors' : Donor.all(),
            'receps' : Recipient.all(),
            'logmsg' : logmsg,
            'logout' : users.create_logout_url('/'),
        }
        self.response.out.write(template.render(donorpath, template_values))
