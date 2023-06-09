"""fungi-id URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, re_path
    2. Add a URL to urlpatterns:  re_path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings

from django.urls import include, re_path
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from fungi import views
from fungi.views import *
#from fungi.views.fungi_notes import NotesIndex
from fungi.views.search import search
from users  import views as user_views
from django.contrib.auth import views as auth_views
#from usersettings.views import  ShowFieldsEdit

#from .views import ProductListView, ProductCreateView
#from fungi.views import FungiLatinSynonymsEditView

admin.autodiscover()
admin.site.enable_nav_sidebar = False

app_name = 'fungi'

urlpatterns = [
    path('', views.home, name='AllFungi-HomePage'),
    path('allfungi/', views.all_fungi, name='AllFungiList'),
    path('links/', views.links, name='Links-Page'),
    path('about/', views.about, name='AllFungi-AboutPage'),
    path('home/', views.home, name='AllFungi-HomePage'),
    path('detail/<slug:slug>/', FungiDetail.as_view(), name='FungiDetail-Page'),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

     path('admin/', admin.site.urls, name='admin:index'),

    path('sources/', views.all_sources, name='DataSources'),
    path('allgroups/', views.all_groups, name='fungi-group-list'),

    path('fungi/<int:slug>/netlinks/', views.FungiLinksView.as_view(), name='fungi_netlinks'),

    path('groups/', group_to_display, name='fungi-groups'),

    # GLOSSARY
    path('glossary/', show_glossary, name='glossary'),
    path('glossary/new', views.GlossaryTermView.as_view(), name='new_glossary_term'),
    path('glossary/<str:slug>/',GlossaryEntry.as_view(), name='glossary_entry'),
    path('glossary/add', views.GlossaryFormView.as_view(), name='glossary_form'),

    # FUNGI  CREATION & EDITING
    path('fungi/new/', views.FungiCreateView.as_view(), name='new_fungi'),
    path('fungi/<int:pk>/edit', views.FungiEditView.as_view(), name='fungi_edit'),

    # VIEWING, EDITING AND ADDING DATA
    path('fungi/<int:pk>/habitat/', views.FungiHabitatView.as_view(), name='fungi_habitat'),
    path('fungi/<int:pk>/fruiting_body/', views.FungiFruitingBodyView.as_view(), name='fungi_fruiting_body'),
    path('fungi/<int:pk>/stipe/', views.FungiStipeView.as_view(), name='fungi_stipe'),
    path('fungi/<int:pk>/cuisine/', views.FungiCuisineView.as_view(), name='fungi_cuisine'),
    path('fungi/<int:pk>/flesh/', views.FungiFleshView.as_view(), name='fungi_flesh'),
    path('fungi/<int:pk>/spores/', views.FungiSporesView.as_view(), name='fungi_spores'),
    path('fungi/<int:pk>/seasons/', views.FungiSeasonsView.as_view(), name='fungi_seasons'),
    path('fungi/<int:pk>/status/', views.FungiStatusView.as_view(), name='fungi_status'),
    path('fungi/<int:pk>/pores/', views.FungiPoresView.as_view(), name='fungi_pores'),
    path('fungi/<int:pk>/gills/', views.FungiGillsView.as_view(), name='fungi_gills'),
    path('fungi/<int:pk>/comments/', views.FungiCommentsView.as_view(), name='fungi_comments'),
    path('fungi/<int:pk>/taxonomy/', views.FungiTaxonomyView.as_view(), name='fungi_taxonomy'),
    path('fungi/<int:slug>/commonnames/', views.FungiCommonNamesView.as_view(), name='fungi_commonnames'),
    path('fungi/<int:slug>/similar/', views.FungiSimilarView.as_view(), name='fungi_similar'),
    path('fungi/<int:slug>/latinsynonyms/', views.FungiLatinSynomymsView.as_view(), name='fungi_latinsynonyms'),
    path('fungi/<int:slug>/refs/', views.FungiRefsView.as_view(), name='fungi_refs'),
    #path('fungi/<int:pk>/personalnotes/', views.FungiPersonalNotesView.as_view(), name='personal_notes'),

    path('Sources/', show_sources_list, name='show_sources'),

    # PASSWORD
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('usersettings/', include('usersettings.urls', namespace="usersettings")),

    # SEARCH
    path('search/', search, name='search_fungi'),

    #re_path('__debug__/', include(debug_toolbar.urls)),

    #path('Fungis/<int:pk>/notes/edit/', views.FunginotesEditView.as_view(), name='Fungi_note_edit'),
    #path('Fungis/<int:pk>/notes2/edit/', views.FunginotesEditView2.as_view(), name='Fungi_note_edit2'),
    path('Fungis/<int:pk>/notes/edit/', views.FunginoteEdit.as_view(), name="Fungi_note_edit"),
    path('Fungis/<int:pk>/notes/create/', views.FunginoteCreate.as_view(), name="Fungi_note_create"),
    path('Fungis/<int:pk>/notes/delete/', views.FunginoteDelete.as_view(), name="Fungi_note_delete"),

 ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

