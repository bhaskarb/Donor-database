#!/usr/bin/env/python
__author__ = 'Bhaskar Bharath'

#import re
import urllib2
import os
from models.models import *
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
       #logging.debug("In main Page")
       path = os.path.join(os.path.dirname(__file__), '..', 'views', 'main.html')
       projects=Project.all()
       if projects.count():
           options=["Donor", "Recipient", "Steward"]
       else:
           options=["Steward"]
       template_values = {
          'projects' : projects,
          'options' : options,
          'logout' : users.create_logout_url('/'),
       }   
       self.response.out.write(template.render(path, template_values))
