from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from .forms import ClientForm, AgentForm, PropertyForm, ProjectForm, AmenityForm, propertyTypesForm, SourceForm, LeadsForm, LeadsUpdateForm, CommentsForm
from .models import Client, Agent, Property, Project, Amenity, propertyTypes, Source, Leads, Comments, Owns
# Create your views here.
def home(request):
    return render(request, 'dashboard.html')

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid:
            client = form.save(commit=False)
            client.owner = request.user.id 
            client.save()
            messages.success(request, 'Client was added')
            return redirect('list_clients')
        else :
            messages.success(request, 'invalid form. try again')
            return redirect('add_client')
    else :
        form = ClientForm()
        
    return render(request, 'add_client.html', {'form': form})

def add_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            Agent = form.save(commit=False)
            Agent.owner = request.user.id 
            Agent.save()
            messages.success(request, 'Agent was added')
            return redirect('list_agents')
        else:
            messages.success(request, 'invalid form. try again')
            return redirect('add_agent')
    else:
        form = AgentForm()
    return render(request, 'add_agent.html', {'form': form })

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, user=request.user)
        if form.is_valid():
            pro = form.save(commit=False)
            pro.owner = request.user.id
            pro.save()
            messages.success(request, 'property was added')
            return redirect('list_properties')
        else :
            messages.success(request, 'invalid form. try again')
            return redirect('add_property')
    else :
        form = PropertyForm(user=request.user)
    return render(request, 'add_property.html', {'form': form})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, user=request.user)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.id
            project.save()
            messages.success(request, 'property was added')
            return redirect('list_projects')
        else:
            messages.success(request, 'invalid form. try again')
            return redirect('add_project')
    else :
        form = ProjectForm(user=request.user)
    return render(request, 'add_project.html', { 'form' : form })

def add_leads(request):
    leads = Leads.objects.filter(owner=request.user.id)
    if request.method == 'POST':
        form = LeadsForm(request.POST, user=request.user)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.owner = request.user
            if not lead.date:
                lead.date = timezone.now()
            lead.save()
            messages.success(request, 'leads was added')
            return redirect('fresh_leads')
    else :
        form = LeadsForm(user=request.user)
    return render(request, 'add_leads.html', { 'form' : form , 'leads' : leads })




def list_clients(request):
    clients = Client.objects.filter(owner=request.user.id).order_by('-id')
    return render(request, 'list_clients.html', {'clients' : clients})

def list_agents(request):
    agents = Agent.objects.filter(owner=request.user.id).order_by('-id')
    return render(request, 'list_agents.html', {'agents': agents})

def list_properties(request):
    properties = Property.objects.filter(owner=request.user.id).order_by('-id')
    return render(request, 'list_property.html', {'properties' : properties})


def list_projects(request):
    projects = Project.objects.filter(owner=request.user.id).order_by('-id')
    return render(request, "list_project.html", {"projects" : projects} )

def edit_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client edited successfully.')
            return redirect('list_clients')
        else:
            messages.error(request, 'Form submission is not valid. Please correct the errors.')
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'edit_client.html', {'form': form})

def edit_agent(request, agent_id):
    agent = Agent.objects.get(pk=agent_id)
    if request.method == 'POST':
        form = AgentForm(request.POST or None , instance=agent)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agent edited successfully.')
            return redirect('list_agents')
        else :
            messages.error(request, 'Something went wrong')
    else :
        form = AgentForm(instance=agent, user=request.user)
    return render(request, 'edit_agent.html', { 'form': form })

def edit_property(request, property_id):
    pro = Property.objects.get(pk=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST or None , instance=pro, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'property edited successfully.')
            return redirect('list_properties')
        else :
            messages.error(request, 'Something went wrong')
    else :
        form = PropertyForm(instance=pro, user=request.user)
    return render(request, 'edit_property.html', { 'form': form })

def edit_project(request, project_id):
    pro = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST or None , instance=pro, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'project edited successfully.')
            return redirect('list_projects')
        else :
            messages.error(request, 'Something went wrong')
    else :
        form = ProjectForm(instance=pro, user=request.user)
    return render(request, 'edit_projects.html', { 'form': form })

def edit_leads(request, lead_id):
    lead = Leads.objects.get(pk=lead_id)
    remarks = Comments.objects.filter(author=lead_id)
    if request.method == 'POST':
        form = LeadsUpdateForm(request.POST or None , instance=lead, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'lead edited successfully.')
            return redirect(request.path)
        else :
            messages.success(request, 'Something went wrong try again.')
    else :
        form = LeadsUpdateForm(instance=lead , user=request.user)
        add_remark = CommentsForm()
    return render(request, 'edit_leads.html', {'form': form, 'lead' : lead, 'remarks': remarks, 'add_remarks' : add_remark })

def add_comments(request, lead_id):
    if request.method == 'POST':
        comment = CommentsForm(request.POST)
        if comment.is_valid():
            c = comment.save(commit=False)
            c.author = lead_id
            c.owner = request.user
            c.save()
        return redirect('edit_leads', lead_id=lead_id)
    return 


def delete_client(request, client_id):
    client = Client.objects.get(pk=client_id)
    client.delete()
    return redirect('list_clients')

def delete_agent(request, agent_id):
    agent = Agent.objects.get(pk=agent_id)
    agent.delete()
    return redirect('list_agents')

def delete_property(request, property_id):
    pro = Property.objects.get(pk=property_id)
    pro.delete()
    return redirect('list_properties')

def delete_project(request, project_id):
    pro = Project.objects.get(pk=project_id)
    pro.delete()
    return redirect('list_projects')

def delete_amenity(request, amenity_id):
    amenity = Amenity.objects.get(pk=amenity_id)
    amenity.delete()
    return redirect('amenities')

def delete_propertytype(request, propertytype_id):
    pro = propertyTypes.objects.get(pk=propertytype_id)
    pro.delete()
    return redirect('property_types')

def delete_leads(request, lead_id):
    pro = Leads.objects.get(pk=lead_id, owner=request.user)
    pro.delete()
    return redirect('fresh_leads')

def view_client(request, client_id):
    client = Client.objects.get(pk=client_id)

    return render(request, 'view_client.html', {'client' : client})

def view_agent(request, agent_id):
    agent = Agent.objects.get(pk=agent_id)

    return render(request, 'view_agent.html', {'agent' : agent })

def view_property(request, property_id):
    pro = Property.objects.get(pk=property_id)
    return render(request, 'view_property.html', {'property' : pro})

def view_project(request, project_id):
    pro = Project.objects.get(pk=project_id)
    return render(request, 'view_project.html', {'project' : pro})

def amenities(request):
    amenities = Amenity.objects.filter(owner=request.user.id)
    if request.method == 'POST':
        form = AmenityForm(request.POST)
        if form.is_valid():
            amenities = form.save(commit=False)
            amenities.owner = request.user.id
            amenities.save()
            messages.success(request, 'An amenity has been created')
            return redirect('amenities')
        else :
            messages.success(request, 'form was invalid . try again')
            return redirect('amenities')
    else :
        form = AmenityForm()
    return render(request, 'amenities.html', {'form': form, 'amenities': amenities})

def property_types(request):
    types = propertyTypes.objects.filter(owner=request.user.id)
    if request.method == 'POST':
        form = propertyTypesForm(request.POST)
        if form.is_valid():
            ptype = form.save(commit=False)
            ptype.owner = request.user.id
            ptype.save()
            messages.success(request, 'An property Type has been created')
            return redirect('property_types')
        else :
            messages.success(request, 'form was invalid . try again')
            return redirect('property_types')
    else :
        form = propertyTypesForm()
    return render(request, 'property_types.html', {'form': form, 'types': types})

def add_Source(request):
    source = Source.objects.filter(owner=request.user.id)
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            s.owner = request.user.id
            s.save()
            messages.success(request, 'An Source has been created')
            return redirect('add_Source')
        else :
            messages.success(request, 'form was invalid . try again')
            return redirect('add_Source')
    else :
        form = SourceForm()
    return render(request, 'Source.html', {'form' : form , 'sources' : source })

def delete_source(request, source_id):
    source = Source.objects.get(pk=source_id)
    source.delete()
    return redirect('add_Source')


def fresh_leads(request):
    one_days_ago = timezone.now() - timedelta(days=2)
    leads = Leads.objects.filter(owner=request.user, date__gte=one_days_ago.date())
    return render(request, 'fresh_leads.html', {'leads' : leads})


def old_leads(request):
    one_days_ago = timezone.now() - timedelta(days=1)
    leads = Leads.objects.filter(owner=request.user, date__lt=one_days_ago.date())
    return render(request, 'old_leads.html', {'leads' : leads})

def all_leads(request):
    leads = Leads.objects.filter(owner=request.user)
    return render(request, 'all_leads.html', {'leads' : leads})

def property_available(request):
    properties  = Property.objects.filter(owner=request.user.id, status=True).order_by('-id')
    return render(request, 'property_available.html', {'properties' : properties} )

def property_unavailable(request):
    properties  = Property.objects.filter(owner=request.user.id, status=False).order_by('-id')
    return render(request, 'property_unavailable.html', {'properties' : properties} )

def upcoming_followups(request):
    today = timezone.now().date()
    leads = Leads.objects.filter(owner=request.user, followUpDate__gt=today)
    return render(request, 'upcoming_followups.html', {'leads': leads})

def todays_followups(request):
    today = timezone.now().date()
    leads = Leads.objects.filter(owner=request.user, followUpDate=today)
    return render(request, 'todays_followups.html', {'leads': leads})

def attempt(request, lead_id, property_id=None):
    lead = Leads.objects.get(pk=lead_id)
    properties = Property.objects.filter(location=lead.location, status=True)
    property_ = None  # Initialize property_ variable
    val = True

    if property_id:
        property_ = Property.objects.get(pk=property_id)
        try:
            if property_.property_cost is not None and lead.max_budget is not None:
                property_cost = int(property_.property_cost)
                length = int(lead.max_budget)
                # Perform the comparison
                if property_cost < length:
                    val = True
                else:
                    val = False 
        except ValueError as e:
            logger.error(f"Failed to convert string to integer: {e}")
            property_cost = 0
            pass
        
    return render(request, 'attempt.html', {'lead' : lead, 'properties' : properties, 'property' : property_, 'value' : val })

def owns(request, lead_id, property_id):
    lead = Leads.objects.get(pk=lead_id)
    pro = Property.objects.get(pk=property_id)
    if request.method == 'POST':
        own = Owns(client=lead.client, properties=pro, owner=request.user)
        if own :
            own.save()
            messages.success(request, 'Property submitted successfully')
            return redirect(request.path)
        else :
            messages.success(request, 'There was an Error Dealing this property')
            return redirect(request.path)
    return redirect('all_leads')