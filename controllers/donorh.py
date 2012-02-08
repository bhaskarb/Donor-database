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

class NewDonor(webapp.RequestHandler):
    def post(self):
        donor_email=self.request.get('donor_email');
        donor_fname=self.request.get('donor_fname');
        donor_mname=self.request.get('donor_mname');
        donor_lname=self.request.get('donor_lname');
        donor_cats=self.request.get('donor_cat');
        donors=Donor.all();
        donors.filter("Email =", donor_email);
        if not donors.count():
            log_msg="Added New donor %s" %(donor_email)
            donor=Donor(parent=donor_key(donor_email), Email=donor_email);
        else:
            log_msg="Updated donor %s" %(donor_email)
            donor=donors.fetch(limit=1)[0]

        donor.FName=donor_fname;
        donor.Mname=donor_mname;
        donor.LName=donor_lname
        for donor_cat in donor_cats:
            cat=Category.all().filter("Name =", donor_cat);
            if cat.count():
                cat=cat.fetch(limit=1)[0]
                if cat.key() not in donor.Categories:
                    donor.Categories.append(cat.key())
        donor.put()

        cats=Category.all()  
        donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'steward.html')
        template_values = {
            'user_name' : config.uname,
            'cats' : cats,
            'projects' : Project.all(),
            'donors' : Donor.all(),
            'receps' : Recipient.all(),
            'logmsg' : log_msg,
            'logout' : users.create_logout_url('/'),
        }
        self.response.out.write(template.render(donorpath, template_values))

            
        
