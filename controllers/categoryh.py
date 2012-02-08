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

class NewCategory(webapp.RequestHandler):
    def post(self):
        cat_name=self.request.get('cat_name')
        cats=Category.all()
        cats.filter("Name =", cat_name)
        if not cats.count():
            cat=Category(parent=category_key(cat_name), Name=cat_name)
            cat.put()
            logmsg="Category %s added" %(cat_name)
        else:
            logmsg="Category %s already exists" %(cat_name)

        cats=Category.all()  
        donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'steward.html')
        template_values = {
            'user_name' : config.uname,
            'cats' : cats,
            'projects' : Project.all(),
            'donors' : Donor.all(),
            'receps' : Recipient.all(),
            'logmsg' : logmsg,
            'logout' : users.create_logout_url('/'),
        }
        self.response.out.write(template.render(donorpath, template_values))
