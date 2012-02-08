#!/usr/bin/env/python
__author__ = 'Bhaskar Bharath'

#import re
import urllib2
import os
import config
from datetime import datetime
import time
from models.models import *
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template

class NewDonation(webapp.RequestHandler):
    def post(self):
        donor_name=self.request.get('donation_donor')
        recep_name=self.request.get('donation_recep')
        amounttxt=self.request.get('donation_amount')
        startdtxt=self.request.get('donation_startd')
        enddtxt=self.request.get('donation_endd')
        comments=self.request.get('donation_comments')
        donor=Donor.all().filter("Email =", donor_name).fetch(1)[0]
        recep=Recipient.all().filter("Name =", recep_name).fetch(limit=1)[0]
        startd=datetime.strptime(startdtxt,"%d/%m/%y")
        endd=datetime.strptime(enddtxt,"%d/%m/%y")
        amount=float(amounttxt)
        
        donrep=DonorRecep(parent=donorrecep_key(donor, recep, amounttxt, startd, endd), Donor=donor, Recipient=recep, Amount=amount, DateSt=startd, DateEnd=endd)
        donrep.Comments=comments
        donor.IsActive=True
        recep.IsSupported=True
        donor.put()
        recep.put()
        donrep.put()
        logmsg="Added new donation for %s" %(amount)
        donorpath = os.path.join(os.path.dirname(__file__), '..', 'views', 'steward.html')
        template_values = {
            'user_name' : config.uname,
            'cats' : Category.all(),
            'projects' : Project.all(),
            'donors' : Donor.all(),
            'receps' : Recipient.all(),
            'logmsg' : logmsg,
            'logout' : users.create_logout_url('/'),
        }
        self.response.out.write(template.render(donorpath, template_values))

