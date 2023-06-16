from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from .models import *
#from .models import Show
#from .models import ShowSearchFields
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
#from usersettings.forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect

def filtershome(request):
	all_users= get_user_model().objects.all()
	all_show = ShowSearchFields.objects.all()
	context = {
		'shows' : all_show,
		'usersexists' : all_users #not currently rendered
	}
	return render(request, 'filtershome.html', context)

class ShowFieldsEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Show
	template_name = 'show_details_form.html'  # <app>/<model>_<viewtype>.html
	fields = [
	'ShowOtherCommonNames','ShowLatinSynonyms', 'ShowGroup',
	'ShowPoresAndTubes',	'ShowGills',	'ShowSpores','ShowFlesh','ShowHabitat','ShowCuisine',	'ShowFruitingBody',
	'ShowStipe','ShowSeasons','ShowSimilarFungi','ShowStatus','ShowFungiComments','ShowLatinNames',
	'ShowClassification', 'ShowOnlyUKOccurences','ShowMacromycetes','ShowFungiNotes'
	] 
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'id-EditFilter'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		self.helper.add_input(Submit('submit', 'Submit'))

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False

class SearchFieldsEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ShowSearchFields
	template_name = 'searchfields_form.html'  # <app>/<model>_<viewtype>.html
	#fields = '__all__'
	fields = [
	'id',
	'SearchExactMatch',
	'SearchCommonName',
	'SearchLatinName',
	'SearchGroup',
	'SearchHabitatAssociations',
	'SearchMonthFound',
	'SearchHabitatPh',
	'SearchHabitatSubstrate',
	'SearchHabitatEnvironment',
	'SearchHabitatSoil',
	'SearchCapColour',
	'SearchCapShape',
	'SearchCapRim',
	'SearchCapTexture',
	'SearchCapBruiseColour',
	'SearchCapCutColour',
	'SearchCapWidth',
	'SearchStipeColour',
	'SearchStipeBruiseColour',
	'SearchStipeCutColour',
	'SearchStipeLength',
	'SearchStipeThickness',
	'SearchStipeShape',
	'SearchStipeReticulationPresent',
	'SearchStipeReticulation',
	'SearchStipeBase',
	'SearchStipeTexture',
	'SearchStipeRing',
	'SearchPoresPresent',
	'SearchPoreColour',
	'SearchPoreShape',
	'SearchPoreBruiseColour',
	'SearchTubeColour',
	'SearchTubeShape',
	'SearchTubeBruiseColour',
	'SearchPoreMilk',
	'SearchGillsPresent',
	'SearchGillsColour',
	'SearchGillsBruiseColour',
	'SearchGillsCutColour',
	'SearchGillsAttachment',
	'SearchGillsArrangement',
	'SearchGillsMilk',
	'SearchFleshCapColour',
	'SearchFleshCapBruiseColour',
	'SearchFleshCapCutColour',
	'SearchFleshStipeColour',
	'SearchFleshStipeBruiseColour',
	'SearchFleshStipeCutColour',
	'SearchSporeColour',
	'SearchOtherCommonNames',
	'SearchLatinSynonyms',
	'SearchKingdom',
	'SearchPhyum',
	'SearchSubPhyum',
	'SearchClass',
	'SearchSubClass',
	'SearchOrder',
	'SearchFamily',
	'SearchGenus',
	'SearchPoisonType',
	'SearchCulinaryRating',
	'SearchOdour',
	'SearchTaste',
	'SearchStatusStatusData',
	'SearchStatusWhereFound'
	]

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		show = self.get_object()
		if self.request.user == show.user:
			return True
		return False

