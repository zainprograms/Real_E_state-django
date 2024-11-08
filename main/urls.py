from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('add_client', views.add_client, name='add_client' ),
    path('add_agent', views.add_agent, name='add_agent' ),
    path('add_property', views.add_property, name='add_property' ),
    path('add_project', views.add_project, name='add_project' ),
    path('add_leads', views.add_leads, name='add_leads' ),
    path('add_Source', views.add_Source, name='add_Source'),
    path('list_clients', views.list_clients, name='list_clients' ),
    path('list_agents', views.list_agents, name='list_agents' ),
    path('list_properties', views.list_properties, name='list_properties' ),
    path('list_projects', views.list_projects, name='list_projects' ),
    path('edit_client/<int:client_id>', views.edit_client, name='edit_client' ),
    path('edit_agent/<int:agent_id>', views.edit_agent, name='edit_agent' ),
    path('edit_property/<int:property_id>', views.edit_property, name='edit_property' ),
    path('edit_project/<int:project_id>', views.edit_project, name='edit_project' ),
    path('delete_client/<int:client_id>', views.delete_client, name='delete_client' ),
    path('delete_agent/<int:agent_id>', views.delete_agent, name='delete_agent' ),
    path('delete_property/<int:property_id>', views.delete_property, name='delete_property' ),
    path('delete_amenity/<int:amenity_id>', views.delete_amenity, name='delete_amenity' ),
    path('delete_propertytype/<int:propertytype_id>', views.delete_propertytype, name='delete_propertytype' ),
    path('delete_project/<int:project_id>', views.delete_project, name='delete_project' ),
    path('delete_source/<int:source_id>', views.delete_source, name='delete_source' ),
    path('delete_leads/<int:lead_id>', views.delete_leads, name='delete_leads' ),
    path('view_client/<int:client_id>', views.view_client, name='view_client' ),
    path('view_agent/<int:agent_id>', views.view_agent, name='view_agent' ),
    path('view_property/<int:property_id>', views.view_property, name='view_property' ),
    path('view_project/<int:project_id>', views.view_project, name='view_project' ),
    path('amenities', views.amenities, name='amenities'),
    path('property_types', views.property_types, name='property_types'),
    path('fresh_leads', views.fresh_leads, name='fresh_leads'),
    path('old_leads', views.old_leads, name='old_leads'),
    path('all_leads', views.all_leads, name='all_leads'),
    path('edit_leads/<int:lead_id>', views.edit_leads, name='edit_leads'),
    path('add_comments/<int:lead_id>', views.add_comments, name='add_comments'),
    path('property_available', views.property_available, name='property_available'),
    path('property_unavailable', views.property_unavailable, name='property_unavailable'),
    path('upcoming_followups', views.upcoming_followups, name='upcoming_followups'),
    path('todays_followups', views.todays_followups, name='todays_followups'),
    path('attempt/<int:lead_id>/<int:property_id>', views.attempt, name='attempt.'),
    path('attempt/<int:lead_id>', views.attempt, name='attempt'),
    path('owns/<int:lead_id>/<int:property_id>', views.owns, name='owns'),
]