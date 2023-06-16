from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Show(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	slug = models.SlugField(null=False)
	ShowAll  = models.BooleanField(default=False ,verbose_name=  ' _'+'show all')
	ShowOtherCommonNames  = models.BooleanField(default=False ,verbose_name=  ' _'+'Common name')
	ShowLatinNames  = models.BooleanField(default=False ,verbose_name=  ' _'+'Latin name')
	ShowGroup = models.BooleanField(default=False ,verbose_name=  ' _'+'Group/Type')
	ShowLatinSynonyms  = models.BooleanField(default=False ,verbose_name=  ' _'+'Other Latin names')
	ShowClassification  = models.BooleanField(default=False ,verbose_name=  ' _'+'Classification')
	ShowPoresAndTubes  = models.BooleanField(default=False ,verbose_name=  ' _'+'Pores & Tubes')
	ShowGills  = models.BooleanField(default=False ,verbose_name=  ' _'+'Gills')
	ShowSpores  = models.BooleanField(default=False ,verbose_name=  ' _'+'Spores')
	ShowFlesh  = models.BooleanField(default=False ,verbose_name=  ' _'+'Flesh')
	ShowHabitat  = models.BooleanField(default=False ,verbose_name=  ' _'+'Habitat')
	ShowCuisine  = models.BooleanField(default=False ,verbose_name=  ' _'+'Cuisine')
	ShowFruitingBody  = models.BooleanField(default=False ,verbose_name=  ' _'+'FruitingBody')
	ShowStipe  = models.BooleanField(default=False ,verbose_name=  ' _'+'Stipe/Stem')
	ShowSeasons  = models.BooleanField(default=False ,verbose_name=  ' _'+'Seasons')
	ShowSimilarFungi  = models.BooleanField(default=False ,verbose_name=  ' _'+'Similar Fungi')
	ShowStatus  = models.BooleanField(default=False ,verbose_name=  ' _'+'Status')
	ShowFungiComments  = models.BooleanField(default=False ,verbose_name=  ' _'+'Comments')
	ShowOnlyUKOccurences = models.BooleanField(default=False ,verbose_name=  ' _'+'UK Species Only')
	ShowMacromycetes =  models.BooleanField(default=False ,verbose_name=  ' _'+'Macromycetes (Large fungi) Only')
	ShowSourcesList = models.BooleanField(default=True ,verbose_name=  ' _'+'Source lIST')
	DetailSources = models.BooleanField(default=True ,verbose_name=  ' _'+'Detail Sources')
	ShowFungiNotes = models.BooleanField(default=True ,verbose_name=  ' _'+'Fungi Notes')
	#ShowFungiNotes2 = models.BooleanField(default=True, verbose_name=' _' + 'Fungi Notes2')

	class Meta:
		managed = True
		db_table = 'Show'
		app_label  = 'usersettings'


	def __str__(self):
		return  'User name: '+f'{self.user.username}'+',  user ID: ' +str(self.user.id)

	def get_absolute_url(self):
		#return  reverse('usersettings:edit-show-filter', kwargs={'slug': self.slug})
		return  reverse('AllFungiList')
	
	# def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	def save(self, *args, **kwargs):
		if not self.slug:
			print('self.id = ', self.id)
			print('self.id = ', self.user.id)

			self.slug = slugify(self.user.id)
		return super().save(*args, **kwargs)

class ShowSearchFields(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	slug = models.SlugField(null=True)
	SearchExactMatch = models.BooleanField(default=False, verbose_name=  ' _'+'Exact match')
	SearchCommonName = models.BooleanField(default=False, verbose_name= ' _'+'Common name')
	SearchLatinName = models.BooleanField(default=False ,verbose_name=  ' _'+'Latin name')
	SearchGroup = models.BooleanField(default=False ,verbose_name=  ' _'+'Group/Type')
	SearchHabitatAssociations = models.BooleanField(default=False, verbose_name=  ' _'+'Associated Trees')
	SearchHabitatPh = models.BooleanField(default=False, verbose_name=  ' _'+'Ph')
	SearchHabitatSubstrate = models.BooleanField(default=False, verbose_name=  ' _'+'Substrate')
	SearchHabitatEnvironment = models.BooleanField(default=False, verbose_name=' _' + 'Environment')
	SearchHabitatSoil = models.BooleanField(default=False, verbose_name=  ' _'+'Soil')
	SearchMonthFound = models.BooleanField(default=False, verbose_name=  ' _'+'Month found')
	SearchCapColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	SearchCapShape = models.BooleanField(default=False, verbose_name=  ' _'+'Shape')
	SearchCapRim= models.BooleanField(default=False, verbose_name=  ' _'+'Rim')
	SearchCapTexture = models.BooleanField(default=False, verbose_name=  ' _'+'Texture')
	SearchCapBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Bruise colour')
	SearchCapCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Cut colour')
	SearchCapWidth = models.BooleanField(default=False, verbose_name=  ' _'+'width')
	SearchStipeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	SearchStipeBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Bruise colour')
	SearchStipeCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Cut colour')
	SearchStipeLength = models.BooleanField(default=False, verbose_name=  ' _'+'length')
	SearchStipeThickness = models.BooleanField(default=False, verbose_name=  ' _'+'thickness')
	SearchStipeShape = models.BooleanField(default=False, verbose_name=  ' _'+'Shape')
	SearchStipeReticulationPresent = models.BooleanField(default=False, verbose_name=  ' _'+'Reticulation present')
	SearchStipeReticulation = models.BooleanField(default=False, verbose_name=  ' _'+'Reticulation')
	SearchStipeBase = models.BooleanField(default=False, verbose_name=  ' _'+'Base')
	SearchStipeTexture = models.BooleanField(default=False, verbose_name=  ' _'+'Texture')
	SearchStipeRing = models.BooleanField(default=False, verbose_name=  ' _'+'Ring')
	SearchPoresPresent = models.BooleanField(default=False, verbose_name=  ' _'+'Pores Present')
	SearchPoreColour = models.BooleanField(default=False, verbose_name=  ' _'+'Pore Colour')
	SearchPoreShape = models.BooleanField(default=False, verbose_name=  ' _'+'PoreShape')
	SearchPoreBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Pore Bruise colour')
	SearchTubeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Tube Colour')
	SearchTubeShape = models.BooleanField(default=False, verbose_name=  ' _'+'Tube Shape')
	SearchTubeBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Tube Bruise colour')
	SearchPoreMilk = models.BooleanField(default=False, verbose_name=  ' _'+'Milk')
	SearchGillsPresent = models.BooleanField(default=False, verbose_name=  ' _'+'Present')
	SearchGillsColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	SearchGillsBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Bruise colour')
	SearchGillsCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Cut colour')
	SearchGillsAttachment = models.BooleanField(default=False, verbose_name=  ' _'+'Attachment')
	SearchGillsArrangement = models.BooleanField(default=False, verbose_name=  ' _'+'Arrangement')
	SearchGillsMilk = models.BooleanField(default=False, verbose_name=  ' _'+'Milk')
	SearchFleshCapColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh colour')
	SearchFleshCapBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh bruise colour')
	SearchFleshCapCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh cut colour')
	SearchFleshStipeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Fesh colour')
	SearchFleshStipeBruiseColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh bruise colour')
	SearchFleshStipeCutColour = models.BooleanField(default=False, verbose_name=  ' _'+'Flesh cut colour')
	SearchSporeColour = models.BooleanField(default=False, verbose_name=  ' _'+'Colour')
	SearchOtherCommonNames = models.BooleanField(default=False, verbose_name=  ' _'+'alt. common names')
	SearchLatinSynonyms = models.BooleanField(default=False, verbose_name=  ' _'+'alt. latin names')
	SearchKingdom = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Kingdom')
	SearchPhyum = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Phyum')
	SearchSubPhyum = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. SubPhyum')
	SearchClass = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Class')
	SearchSubClass = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. SubClass')
	SearchOrder = models.BooleanField(default=False, verbose_name=  ' _'+'Tax, Order')
	SearchFamily = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Family')
	SearchGenus = models.BooleanField(default=False, verbose_name=  ' _'+'Tax. Genus')
	SearchPoisonType = models.BooleanField(default=False, verbose_name=  ' _'+'Poision type')
	SearchCulinaryRating = models.BooleanField(default=False, verbose_name=  ' _'+'Culinary rating')
	SearchOdour = models.BooleanField(default=False, verbose_name=  ' _'+'Ononedour')
	SearchTaste = models.BooleanField(default=False, verbose_name=  ' _'+'Taste')
	SearchStatusStatusData = models.BooleanField(default=False, verbose_name=  ' _ '+'Status')
	SearchStatusWhereFound = models.BooleanField(default=False, verbose_name=  ' _'+'Where found (geographically')
	#StatusUKOccurences = models.BooleanField(default=False, verbose_name=  ' _'+'UK Occurences')
	SearchStatusRecordedInUK= models.BooleanField(default=False, verbose_name=  ' _'+'In UK')
	SearchFungiNotes = models.BooleanField(default=False, verbose_name=' _' + 'Fungi Notes')
	SearchMonthFoundNotes = models.BooleanField(default=False, verbose_name=  ' _'+'Month Found Notes')
	SearchWhereFoundNotes = models.BooleanField(default=False, verbose_name=  ' _'+'Where Found Notes')
	SearchEnvironmentNotes = models.BooleanField(default=False, verbose_name=  ' _'+'Environmental Notes')




	class Meta:
		managed = True
		db_table = 'ShowSearchFields'
		verbose_name = 'ShowSearchFields'
		verbose_name_plural = 'ShowSearchFields'
		app_label  = 'usersettings'

	def __str__(self):
		#return f'{self.user.username}'+' ID:' +str(self.user.id)+'; Record ID:'+str(self.id)
		return 'User name: ' + f'{self.user.username}' + ',  user ID: ' + str(self.user.id)


	def get_absolute_url(self):
		#return  reverse('usersettings:edit-search-fields', kwargs={'slug': self.slug})
		return  reverse('search_fungi')


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.user.id)
		return super().save(*args, **kwargs)