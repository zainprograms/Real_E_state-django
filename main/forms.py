from django import forms
from django.forms import ModelForm
from .models import Client, Agent, Property, Project, Amenity, propertyTypes, Source, Leads, Comments

class ClientForm(forms.ModelForm):
    
  class Meta:
    model = Client
    fields = ('client_name' , 'client_contact', 'client_mail', 'client_DOB', 'client_address', 'client_city', 'client_state', 'client_pin', 'occupation' )
    labels = {
        'client_name' : '',
        'client_contact' : '',
        'client_mail' : '',
        'client_DOB' : '',
        'client_address' : '',
        'client_city' : '',
        'client_state' : '',
        'client_pin' : '',
        'occupation' : 'Occupation',
        }
    widgets = { 
      'client_name' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Client name"}),
      'client_contact' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Client contact"}),
      'client_mail' : forms.EmailInput(attrs={'class':'form-control', "placeholder": "Client mail"}),
      'client_DOB': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),

      'client_address' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Client address"}),
      'client_city' : forms.TextInput(attrs={'class':'form-control', "placeholder": "City"}),
      'client_state' : forms.TextInput(attrs={'class':'form-control', "placeholder": "State"}),
      'client_pin' : forms.TextInput(attrs={'class':'form-control', "placeholder": "PIN"}),
      'occupation' : forms.Select(attrs={'class':'form-select', "placeholder": "Occupation"}),}

class AgentForm(forms.ModelForm):
    
  class Meta:
    model = Agent
    fields = ('agent_name' , 'agent_contact', 'agent_mail', 'agent_DOB', 'agent_PAN',  'agent_deals_in','agent_address', 'agent_city', 'agent_state', 'agent_pin' )
    labels = {
        'agent_name' : '',
        'agent_contact' : '',
        'agent_mail' : '',
        'agent_DOB' : 'YYYY-MM-DD',
        'agent_address' : '',
        'agent_city' : '',
        'agent_state' : '',
        'agent_pin' : '',
        'agent_PAN' : '',
        'agent_deals_in' : '',
        }
    widgets = { 
      'agent_name' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Agent name"}),
      'agent_contact' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Agent contact"}),
      'agent_mail' : forms.EmailInput(attrs={'class':'form-control', "placeholder": "Agent mail"}),
      'agent_DOB' : forms.DateInput(attrs={'class':'form-control', "placeholder": "DOB"}),
      'agent_address' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Agent address"}),
      'agent_city' : forms.TextInput(attrs={'class':'form-control', "placeholder": "City"}),
      'agent_state' : forms.TextInput(attrs={'class':'form-control', "placeholder": "State"}),
      'agent_pin' : forms.TextInput(attrs={'class':'form-control', "placeholder": "PIN"}),
      'agent_PAN' : forms.TextInput(attrs={'class':'form-control', "placeholder": "PAN"}),
      'agent_deals_in' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Deals in"}),}


class PropertyForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super(PropertyForm, self).__init__(*args, **kwargs)
    
    # Filter clients, property types, and sources based on the owner field
    self.fields['property_types'].queryset = propertyTypes.objects.filter(owner=user.id)
    self.fields['property_agent'].queryset = Agent.objects.filter(owner=user.id)
    self.fields['amenities'].queryset = Amenity.objects.filter(owner=user.id)

  class Meta:
    model = Property
    fields = ('property_title','location' , 'property_types', 'size', 'property_age', 'property_agent', 'property_cost', 'loan_availability', 'property_description', 'amenities' )
    labels = {
        'property_title' : '',
        'location' : '',
        'property_types' : 'Property type',
        'size' : 'Size',
        'property_age' : '',
        'property_agent' : 'Agent',
        'property_cost' : '',
        'loan_availability' : 'Loan availability ',
        'property_description' : '',
        'amenities' : 'amenities'
        }
    widgets = { 
      'property_title' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Property title"}),
      'location' : forms.TextInput(attrs={'class':'form-control', "placeholder": "location"}),
      'property_types' : forms.Select(attrs={'class':'form-select', "placeholder": "type"}),
      'size' : forms.TextInput(attrs={'class':'form-control', "placeholder": "in Sq. Ft"}),
      'property_age' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Property age"}),
      'property_agent' : forms.Select(attrs={'class':'form-select', "placeholder": "Agent"}),
      'property_cost' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Cost"}),
      'loan_availability' :  forms.CheckboxInput(attrs={'class':'form-check-input', 'placeholder': 'loan'}),
      'property_description' : forms.Textarea(attrs={'class':'form-control', "placeholder": "Description"}),
      'amenities' : forms.SelectMultiple(attrs={'class':'form-select', "placeholder": "amenities"}),}

class ProjectForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super(ProjectForm, self).__init__(*args, **kwargs)
    
    # Filter clients, property types, and sources based on the owner field
    self.fields['add_properties'].queryset = Property.objects.filter(owner=user.id)
    
  class Meta:
    model = Project
    fields = ('project_name', 'add_properties', 'project_location', 'project_area', 'project_description')
    labels = {
        'project_name' : '',
        'add_properties' : 'Add_properties',
        'project_location' : '',
        'project_area' : '',
        'project_description' : '',

        }
    widgets = { 
      'project_name' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Project name"}),
      'add_properties' : forms.SelectMultiple(attrs={'class':'form-select', "placeholder": "Property" }),
      'project_location' : forms.TextInput(attrs={'class':'form-control', "placeholder": "location"}),
      'project_area' : forms.TextInput(attrs={'class':'form-control', "placeholder": "Project area"}),
      'project_description' : forms.Textarea(attrs={'class':'form-control', "placeholder": "description"}),}


class AmenityForm(forms.ModelForm):
    
  class Meta:
    model = Amenity
    fields = ('name',)
    labels = {
        'name' : ''}
    widgets = { 
      'name' : forms.TextInput(attrs={'class':'form-control', "placeholder": "name"})}

      

class propertyTypesForm(forms.ModelForm):
    
  class Meta:
    model = propertyTypes
    fields = ('name',)
    labels = {
        'name' : ''}
    widgets = { 
      'name' : forms.TextInput(attrs={'class':'form-control', "placeholder": "name"})}

class SourceForm(forms.ModelForm):

  class Meta:
    model = Source
    fields = ('name',)
    labels = {
        'name' : ''}
    widgets = { 
      'name' : forms.TextInput(attrs={'class':'form-control', "placeholder": "name"})}

class LeadsForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super(LeadsForm, self).__init__(*args, **kwargs)
    
    # Filter clients, property types, and sources based on the owner field
    self.fields['client'].queryset = Client.objects.filter(owner=user.id)
    self.fields['property_Types'].queryset = propertyTypes.objects.filter(owner=user.id)
    self.fields['Source'].queryset = Source.objects.filter(owner=user.id)


  class Meta:
    model = Leads
    fields = ('client', 'location', 'property_Types', 'Source', 'min_area', 'max_area', 'min_budget', 'max_budget')
    labels = {
        'client' : 'Client',
        'location' : '',
        'property_Types' : 'Property type',
        'Source' : 'Source',
        'min_area': '',
        'max_area': '',
        'min_budget': '',
        'max_budget': '',
    }


    widgets = { 
      'client' : forms.Select(attrs={'class':'form-select', "placeholder": "Client"}),
      'location' : forms.TextInput(attrs={'class':'form-control', "placeholder": "location"}),
      'property_Types' : forms.Select(attrs={'class':'form-control'}),
      'min_area' : forms.TextInput(attrs={'class':'form-control', "placeholder": "min area"}),
      'max_area' : forms.TextInput(attrs={'class':'form-control', "placeholder": "max area"}),
      'min_budget' : forms.TextInput(attrs={'class':'form-control', "placeholder": "min budget"}),
      'max_budget' : forms.TextInput(attrs={'class':'form-control', "placeholder": "max budget"}),
      'Source' : forms.Select(attrs={'class':'form-control'}),
      }

class LeadsUpdateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    super(LeadsUpdateForm, self).__init__(*args, **kwargs)
    
    # Filter clients, property types, and sources based on the owner field
    self.fields['client'].queryset = Client.objects.filter(owner=user.id)
    self.fields['property_Types'].queryset = propertyTypes.objects.filter(owner=user.id)
    self.fields['Source'].queryset = Source.objects.filter(owner=user.id)


  class Meta:
    model = Leads
    fields = ('client', 'location', 'property_Types', 'Source', 'min_area', 'max_area', 'min_budget', 'max_budget' ,'status', 'followUpDate')
    labels = {
        'client' : 'Client',
        'location' : '',
        'property_Types' : 'Property type',
        'Source' : 'Source',
        'min_area': '',
        'max_area': '',
        'min_budget': '',
        'max_budget': '',
        'status': '',
        'followUpDate': ''

        }
    widgets = { 
      'client' : forms.Select(attrs={'class':'form-select', "placeholder": "Client"}),
      'location' : forms.TextInput(attrs={'class':'form-control', "placeholder": "location"}),
      'property_Types' : forms.Select(attrs={'class':'form-control'}),
      'min_area' : forms.TextInput(attrs={'class':'form-control', "placeholder": "min area"}),
      'max_area' : forms.TextInput(attrs={'class':'form-control', "placeholder": "max area"}),
      'min_budget' : forms.TextInput(attrs={'class':'form-control', "placeholder": "min budget"}),
      'max_budget' : forms.TextInput(attrs={'class':'form-control', "placeholder": "max budget"}),
      'status' : forms.Select(attrs={'class':'form-select', "placeholder": "status"}),
      'followUpDate' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
      'Source' : forms.Select(attrs={'class':'form-control'}),
      }


class CommentsForm(forms.ModelForm):
    
  class Meta:
    model = Comments
    fields = ('data',)
    widgets = { 
      'data' : forms.Textarea(attrs={'class':'form-control', "placeholder": "Add Remarks Here"}),}