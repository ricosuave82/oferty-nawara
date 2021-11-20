from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('/activities', views.activities, name="ajax_load_activities"),
    path('/subactivities', views.subactivities, name="ajax_load_subactivities"),

    path('/getSections', views.getSections, name="getSections"),
    path('/getTemplates', views.getTemplates, name="getTemplates"),
    path('/getActivity', views.getActivity , name="getActivity"),
    path('/saveRowData', views.saveRowData , name="saveRowData"),
    path('/addCustomActivity', views.addCustomActivity , name="addCustomActivity"),


    
]