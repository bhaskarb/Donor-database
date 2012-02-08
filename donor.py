#!/usr/bin/env/python
__author__ = 'Bhaskar Bharath'

from controllers import mainh,logpage,donorh,categoryh,projecth,recipienth,donationh
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

application = webapp.WSGIApplication([('/', mainh.MainPage),
                                       ('/login', logpage.LogPage),
                                       ('/newdonor', donorh.NewDonor),
                                       ('/newproj', projecth.NewProject),
                                       ('/newrecep', recipienth.NewRecipient),
                                       ('/newdonation', donationh.NewDonation),
                                       ('/newcat', categoryh.NewCategory)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
