from django.urls import path
from .views import *
from . import views

app_name = 'usersettings'

urlpatterns = [
    path('filterhome/', views.filtershome, name='Filter-HomePage'),
    path('detailstoshow/<slug:slug>/update/', ShowFieldsEdit.as_view(), name='edit-show-filter'),
    path('editsearchfields/<slug:slug>/update/', SearchFieldsEdit.as_view(), name='edit-search-fields'),
]

