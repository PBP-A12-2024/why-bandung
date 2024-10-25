from django.urls import path
from .views import show_main, register, login_user, logout_user, profile, show_xml_by_id, show_json, show_json_by_id, show_xml, edit_journal, delete_journal, create_journal_entry_ajax, get_stores

app_name = 'dashboard'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),\
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('edit-journal/<uuid:id>', edit_journal, name='edit_journal'),
    path('delete-journal/<uuid:id>', delete_journal, name='delete_journal'),
    path('create_journal_entry_ajax', create_journal_entry_ajax, name='create_journal_entry_ajax'),
    path('get-stores/', get_stores, name='get_stores'),
]