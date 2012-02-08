#!/usr/bin/env/python

from google.appengine.ext import db

class Category(db.Model):
    Name = db.StringProperty(required = True)

class Project(db.Model):
    Name = db.StringProperty(required=True)
    Location = db.PostalAddressProperty()
    Desc = db.TextProperty()
    Recipients = db.ListProperty(db.Key) # list of recipients
    Categories = db.ListProperty(db.Key) #List of categories
    
class Donor(db.Model):
    Email = db.EmailProperty(required=True)
    FName = db.StringProperty()
    MName = db.StringProperty()
    LName = db.StringProperty()
    TotalDonated = db.FloatProperty()
    SupportedFrom = db.DateTimeProperty()
    IsActive = db.BooleanProperty(default=False)
    DonorReceps = db.ListProperty(db.Key) # list of transactions
    Categories = db.ListProperty(db.Key) #List of categories

class Recipient(db.Model):
    Name = db.StringProperty(required = True)
    Type = db.StringProperty()
    Desc = db.TextProperty()
    IsSupported = db.BooleanProperty(default=False)
    Project = db.ReferenceProperty(Project, required = True)
    DonorReceps = db.ListProperty(db.Key) # list of transactions

class DonorRecep(db.Model):
    Amount = db.FloatProperty(required = True)
    DateSt = db.DateTimeProperty(required = True)
    DateEnd = db.DateTimeProperty(required = True)
    Comments = db.TextProperty()
    Donor = db.ReferenceProperty(Donor, required = True)
    Recipient = db.ReferenceProperty(Recipient, required = True)    

class Steward(db.Model):
    Email = db.EmailProperty(required=True)
    FName = db.StringProperty()
    MName = db.StringProperty()
    LName = db.StringProperty()
    Project = db.ReferenceProperty(Project, required = True, collection_name='Stewards')
    
def steward_key(email=None):
  """Constructs a datastore key for a DbUser entity with Name."""
  return db.Key.from_path('Email', email or 'default_email')
    
def donor_key(email=None):
  """Constructs a datastore key for a Donor entity with Email."""
  return db.Key.from_path('Email', email or 'default_email')
    
def project_key(name=None):
  """Constructs a datastore key for a Project entity with Name."""
  return db.Key.from_path('Name', name or 'default_name')

def category_key(name=None):
  """Constructs a datastore key for a Category entity with Name."""
  return db.Key.from_path('Name', name or 'default_name')
    
def recipient_key(name=None, project=None):
  """Constructs a datastore key for a Recipient entity with Name."""
  return db.Key.from_path('Name', name or 'default_email', 'Project', project.Name)
  
def donorrecep_key(donor=None, recep=None, amount=None, start=None, stop=None):
  """Constructs a datastore key for a Recipient entity with Name."""
  return db.Key.from_path('Donor', donor.Email, 'Recipient', recep.Name, 'Amount', amount, 'DateSt', start.isoformat(), 'DateEnd', stop.isoformat())

