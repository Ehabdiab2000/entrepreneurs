from django.urls import  path
from . import views

app_name='proj'

urlpatterns = [
    path('',views.project_list , name='project_list'),
    path('add',views.add_project , name='add_project'),
    path('<str:slug>',views.project_detail , name = 'project_detail')
]