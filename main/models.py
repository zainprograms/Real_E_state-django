from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Client(models.Model):
  client_name = models.CharField( max_length=150)
  client_contact = models.CharField(max_length=20)
  client_mail = models.EmailField(max_length=250,)
  client_DOB = models.DateField(auto_now=False, auto_now_add=False)
  client_address = models.CharField(max_length=500)
  client_city = models.CharField( max_length=100)
  client_state = models.CharField(max_length=50, blank=True, null=True)
  client_pin = models.IntegerField()
  OCCUPATION_CHOICES = [
        ('self_employed', 'Self Employed'),
        ('govt_employee', 'Government Employee'),
        ('private_employee', 'Private Employee'),
        ('others', 'Others'),
    ]
  occupation = models.CharField(max_length=20, choices=OCCUPATION_CHOICES)
  owner = models.IntegerField(blank=False, default=1)
  
  def __str__(self):
      return self.client_name


class Agent(models.Model):
  agent_name = models.CharField( max_length=150)
  agent_contact = models.CharField( max_length=150)
  agent_mail = models.EmailField( max_length=254)
  agent_DOB = models.DateField( auto_now=False, auto_now_add=False)
  agent_PAN = models.IntegerField(null=False)
  agent_deals_in = models.CharField( max_length=100)
  agent_address = models.CharField( max_length=250)
  agent_city = models.CharField( max_length=100)
  agent_state = models.CharField( max_length=80)
  agent_pin = models.IntegerField()
  owner = models.IntegerField(blank=False, default=1)

  def __str__(self):
      return self.agent_name

class Property(models.Model):
  property_title =models.CharField( max_length=50)
  location = models.CharField( max_length=150)
  types = {'residential' : 'Residential', 'commercial' : 'Commercial', 'other': 'Other'}
  property_types = models.ForeignKey("PropertyTypes", on_delete=models.CASCADE)
  size = models.CharField( max_length=100)
  property_age = models.IntegerField(null=False)
  property_agent = models.ForeignKey("Agent", blank=True, null=True, on_delete=models.CASCADE)
  property_cost = models.CharField( max_length=5000)
  # CONVERT IT INTO A INTEGER FIELD LATER
  loan_availability = models.BooleanField( default=False )
  property_description = models.TextField(max_length=500, blank=False)
  owner = models.IntegerField(blank=False, default=1)
  status = models.BooleanField(default=True)
  amenities = models.ManyToManyField('Amenity', blank=True) 

  def __str__(self):
      return self.property_title
  
class Project(models.Model):
  project_name = models.CharField( max_length=100)
  add_properties = models.ManyToManyField("Property", related_name='project', blank=True)
  project_location = models.CharField( max_length=50)
  project_area = models.CharField( max_length=50)
  project_description = models.TextField(max_length=1000)
  owner = models.IntegerField(blank=False, default=1)

  def __str__(self):
      return self.project_name
  

class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.IntegerField(default=1)

    def __str__(self):
      return self.name

class propertyTypes(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.IntegerField(default=1)

    def __str__(self):
      return self.name

class Leads(models.Model):
  client = models.ForeignKey("Client", on_delete=models.CASCADE)
  date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
  location = models.CharField( max_length=100)
  min_area = models.IntegerField(blank=True, null=True)
  max_area = models.IntegerField(blank=True, null=True)
  min_budget = models.IntegerField(blank=True, null=True)
  max_budget = models.IntegerField(blank=True, null=True)
  property_Types = models.ForeignKey("propertyTypes", on_delete=models.CASCADE)
  remarks = models.ForeignKey('Comments', on_delete=models.CASCADE, related_name='leads', null=True, blank=True)
  Source = models.ForeignKey("Source", on_delete=models.CASCADE, null=True, blank=True)
  Status_type = {
        "attempted": "Attempted",
        "unattempted": "Unattempted",
    }
  status = models.CharField(choices=Status_type.items(), max_length=50, default='unattempted')
  followUpDate = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
      return self.client.client_name
  
class Comments(models.Model):
  data = models.CharField( max_length=1000)
  author = models.IntegerField(default=1)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.data
  
class Owns(models.Model):
  client = models.ForeignKey("Client", on_delete=models.CASCADE)
  properties = models.ForeignKey("Property", on_delete=models.CASCADE)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
      return str(self.client) + ' - ' + str(self.properties)
  