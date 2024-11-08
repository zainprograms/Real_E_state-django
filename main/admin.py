from django.contrib import admin
from .models import Client, Agent, Property, Project, Amenity, propertyTypes, Source, Leads, Comments, Owns
# Register your models here.
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(Property)
admin.site.register(Project)
admin.site.register(Amenity)
admin.site.register(propertyTypes)
admin.site.register(Source)
admin.site.register(Leads)
admin.site.register(Comments)
admin.site.register(Owns)