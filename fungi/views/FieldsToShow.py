from django import forms
# from fungi.views.choices import *
# from fungi.views.choices2 import *
from fungi.choices import *

def fields_to_show(user_search_fields):
    fields_to_show_dict = {}

    if user_search_fields.SearchCommonName:
        fields_to_show_dict['SearchCommonName'] = forms.CharField(required=False, max_length=255, label='Common Name', initial='cn')
        # print('fieldsToDisplay:::::::::::',fieldsToDisplay)

    if user_search_fields.SearchLatinName:
        fields_to_show_dict['SearchLatinName'] = forms.CharField(required=False, max_length=255, label='Latin Name', initial='')

    if user_search_fields.SearchGroup:
        fields_to_show_dict['SearchGroup'] = forms.CharField(required=False, max_length=255, label='Group', initial='')
        # print('fieldsToDisplay:::::::::::',  fields_to_show_dict['Group'])
    if user_search_fields.SearchHabitatAssociations:
        fields_to_show_dict['SearchHabitatAssociations'] = forms.CharField(required=False, max_length=255, label='Associated Trees', initial='')

    if user_search_fields.SearchHabitatPh:
        #print('user_search_fields.HabitatPh', user_search_fields.HabitatPh)
        fields_to_show_dict['SearchHabitatPh'] = forms.ChoiceField(choices=PhTypeChoices, required=False, label='Ph', initial='')

    if user_search_fields.SearchHabitatSubstrate:
        fields_to_show_dict['SearchHabitatSubstrate'] = forms.CharField(required=False, max_length=255, label='Substrate', initial='')

    if user_search_fields.SearchHabitatEnvironment:
        fields_to_show_dict['SearchHabitatEnvironment'] = forms.CharField(required=False, max_length=255, label='Environment', initial='')

    if user_search_fields.SearchHabitatSoil:
        fields_to_show_dict['SearchHabitatSoil'] = forms.CharField(required=False, max_length=255, label='Soil type', initial='')

    if user_search_fields.SearchMonthFound:
        print('user_search_fields.SearchMonthFound',user_search_fields.SearchMonthFound)
        fields_to_show_dict['SearchMonthFound'] = forms.ChoiceField(choices=MonthFoundChoices, required=False, label='Month/Season Found', initial='month')

    if user_search_fields.SearchCapColour:
        fields_to_show_dict['SearchCapColour'] = forms.CharField(required=False, max_length=255, label='Cap Colour', initial='')

    if user_search_fields.SearchCapShape:
        fields_to_show_dict['SearchCapShape'] = forms.CharField(required=False, max_length=255, label='Cap Shape', initial='')

    if user_search_fields.SearchCapRim:
        fields_to_show_dict['SearchCapRim'] = forms.ChoiceField(choices=CapRimChoices, required=False, label='Cap Rim', initial='')

    if user_search_fields.SearchCapTexture:
        fields_to_show_dict['SearchCapTexture'] = forms.ChoiceField(choices=CapTextureChoices, required=False, label='Cap Texture', initial='')

    if user_search_fields.SearchCapBruiseColour:
        fields_to_show_dict['SearchCapBruiseColour'] = forms.CharField(required=False, max_length=255, label='Cap Bruise Colour', initial='')

    if user_search_fields.SearchCapCutColour:
        fields_to_show_dict['SearchCapCutColour'] = forms.CharField(required=False, max_length=255, label='Cap Cut Colour', initial='')

    if user_search_fields.SearchCapWidth:
        fields_to_show_dict['SearchCapWidth'] = forms.CharField(required=False, max_length=255, label='Cap Width', initial='')

    if user_search_fields.SearchStipeColour:
        fields_to_show_dict['SearchStipeColour'] = forms.CharField(required=False, max_length=255, label='Stipe Colour', initial='')

    if user_search_fields.SearchStipeBruiseColour:
        fields_to_show_dict['SearchStipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Bruise Colour', initial='')

    if user_search_fields.SearchStipeCutColour:
        fields_to_show_dict['SearchStipeCutColour'] = forms.CharField(required=False, max_length=255, label='Stipe Cut Colour', initial='')

    if user_search_fields.SearchStipeLength:
        fields_to_show_dict['SearchStipeLength'] = forms.CharField(required=False, max_length=255, label='Stipe Length', initial='')

    if user_search_fields.SearchStipeThickness:
        fields_to_show_dict['SearchStipeThickness'] = forms.CharField(required=False, max_length=255, label='Stipe Thickness', initial='')

    if user_search_fields.SearchStipeShape:
        fields_to_show_dict['SearchStipeShape'] = forms.CharField(required=False, max_length=255, label='Stipe Shape', initial='')

    if user_search_fields.SearchStipeReticulationPresent:
        fields_to_show_dict['SearchStipeReticulationPresent'] = forms.ChoiceField(choices=ReticulationChoices, required=False, label='Stipe Reticutaion Present', initial='')

    if user_search_fields.SearchStipeReticulation:
        fields_to_show_dict['SearchStipeReticulation'] = forms.CharField(required=False, max_length=255, label='Reticulation', initial='')

    if user_search_fields.SearchStipeBase:
        fields_to_show_dict['SearchStipeBase'] = forms.CharField(required=False, max_length=255, label='Stipe Base', initial='')

    if user_search_fields.SearchStipeTexture:
        fields_to_show_dict['SearchStipeTexture'] = forms.ChoiceField(choices=StipeTextureChoices, required=False, label='Stipe Texture', initial='')

    if user_search_fields.SearchStipeRing:
        fields_to_show_dict['SearchStipeRing'] = forms.ChoiceField(choices=StipeRingChoices, required=False, label='Stipe Ring', initial='')

    if user_search_fields.SearchPoresPresent:
        fields_to_show_dict['SearchPoresPresent'] = forms.ChoiceField(choices=PoresPresentChoices, required=False, label='Pores Present', initial='')

    if user_search_fields.SearchPoreColour:
        fields_to_show_dict['SearchPoreColour'] = forms.CharField(required=False, max_length=255, label='Pore Colour', initial='')

    if user_search_fields.SearchPoreShape:
        fields_to_show_dict['SearchPoreShape'] = forms.CharField(required=False, max_length=255, label='Pore Shape', initial='')

    if user_search_fields.SearchPoreBruiseColour:
        fields_to_show_dict['SearchPoreBruiseColour'] = forms.CharField(required=False, max_length=255, label='Pore Bruise Colour', initial='')

    if user_search_fields.SearchTubeColour:
        fields_to_show_dict['SearchTubeColour'] = forms.CharField(required=False, max_length=255, label='Tube Colour', initial='')

    if user_search_fields.SearchTubeShape:
        fields_to_show_dict['SearchTubeShape'] = forms.CharField(required=False, max_length=255, label='Tube Shap', initial='')

    if user_search_fields.SearchTubeBruiseColour:
        fields_to_show_dict['SearchTubeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Tube Bruise Colour', initial='')

    if user_search_fields.SearchPoreMilk:
        fields_to_show_dict['SearchPoreMilk'] = forms.ChoiceField(choices=PoresMilkChoices, required=False, label='Pore Milk', initial='')

    if user_search_fields.SearchGillsPresent:
        fields_to_show_dict['SearchGillsPresent'] = forms.ChoiceField(choices=GillsPresentChoices, required=False, label='Gills Present', initial='')

    if user_search_fields.SearchGillsColour:
        fields_to_show_dict['SearchGillsColour'] = forms.CharField(required=False, max_length=255, label='Gills Colour', initial='')

    if user_search_fields.SearchGillsBruiseColour:
        fields_to_show_dict['SearchGillsBruiseColour'] = forms.CharField(required=False, max_length=255, label='Gills Bruise Colour', initial='')

    if user_search_fields.SearchGillsCutColour:
        fields_to_show_dict['SearchGillsCutColour'] = forms.CharField(required=False, max_length=255, label='Gills Cut Colour', initial='')

    if user_search_fields.SearchGillsAttachment:
        fields_to_show_dict['SearchGillsAttachment'] = forms.CharField(required=False, max_length=255, label='Gills Attachment', initial='')

    if user_search_fields.SearchGillsArrangement:
        fields_to_show_dict['SearchGillsArrangement'] = forms.CharField(required=False, max_length=255, label='Gills Arrangement', initial='')

    if user_search_fields.SearchGillsMilk:
        fields_to_show_dict['SearchGillsMilk'] = forms.ChoiceField(choices=GillsMilkChoices, required=False, label='Gill Milk', initial='')

    if user_search_fields.SearchFleshCapColour:
        fields_to_show_dict['SearchFleshCapColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Colour ', initial='')

    if user_search_fields.SearchFleshCapBruiseColour:
        fields_to_show_dict['SearchFleshCapBruiseColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Bruise Colour', initial='')

    if user_search_fields.SearchFleshCapCutColour:
        fields_to_show_dict['SearchFleshCapCutColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Cut Colour', initial='')

    if user_search_fields.SearchFleshStipeColour:
        fields_to_show_dict['SearchFleshStipeColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Colour', initial='')

    if user_search_fields.SearchFleshStipeBruiseColour:
        fields_to_show_dict['SearchFleshStipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Bruise Colour', initial='')

    if user_search_fields.SearchFleshStipeCutColour:
        fields_to_show_dict['SearchFleshStipeCutColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Cut Colour', initial='')

    if user_search_fields.SearchSporeColour:
        fields_to_show_dict['SearchSporeColour'] = forms.CharField(required=False, max_length=255, label='Spore Colour', initial='')

    if user_search_fields.SearchOtherCommonNames:
        fields_to_show_dict['SearchOtherCommonNames'] = forms.CharField(required=False, max_length=255, label='Other Common Name', initial='')

    if user_search_fields.SearchLatinSynonyms:
        fields_to_show_dict['SearchLatinSynonyms'] = forms.CharField(required=False, max_length=255, label='Latin Synonym', initial='')

    if user_search_fields.SearchKingdom:
        fields_to_show_dict['SearchKingdom'] = forms.CharField(required=False, max_length=255, label='Taxonmic Kingdom', initial='')

    if user_search_fields.SearchPhyum:
        fields_to_show_dict['SearchPhyum'] = forms.CharField(required=False, max_length=255, label='Taxonmic Phyum', initial='')

    if user_search_fields.SearchSubPhyum:
        fields_to_show_dict['SearchSubPhyum'] = forms.CharField(required=False, max_length=255, label='Taxonmic SubPhyum', initial='')

    if user_search_fields.SearchClass:
        fields_to_show_dict['SearchClass'] = forms.CharField(required=False, max_length=255, label='Taxonmic Class', initial='')

    if user_search_fields.SearchSubClass:
        fields_to_show_dict['SearchSubClass'] = forms.CharField(required=False, max_length=255, label='Taxonmic SubClass', initial='')

    if user_search_fields.SearchOrder:
        fields_to_show_dict['SearchOrder'] = forms.CharField(required=False, max_length=255, label='Taxonmic Order', initial='')

    if user_search_fields.SearchFamily:
        fields_to_show_dict['SearchFamily'] = forms.CharField(required=False, max_length=255, label='Taxonmic Family', initial='')

    if user_search_fields.SearchGenus:
        fields_to_show_dict['SearchGenus'] = forms.CharField(required=False, max_length=255, label='Taxonmic Genus', initial='')

    if user_search_fields.SearchPoisonType:
        fields_to_show_dict['SearchPoisonType'] = forms.CharField(required=False, max_length=255, label='Poison Type', initial='')

    if user_search_fields.SearchCulinaryRating:
        fields_to_show_dict['SearchCulinaryRating'] = forms.ChoiceField(choices=CulinaryRatingChoices, required=False, label='Culinary Rating', initial='')
        # fieldsToDisplay['CulinaryRating'] = forms.CharField(required=False, max_length=255, label='Culinary Rating', initial='')

    if user_search_fields.SearchOdour:
        fields_to_show_dict['SearchOdour'] = forms.CharField(required=False, max_length=255, label='Odour', initial='')

    if user_search_fields.SearchTaste:
        fields_to_show_dict['SearchTaste'] = forms.CharField(required=False, max_length=255, label='Taste', initial='')

    if user_search_fields.SearchStatusStatusData:
        fields_to_show_dict['SearchStatusStatusData'] = forms.CharField(required=False, max_length=255, label='Status', initial='')

    if user_search_fields.SearchStatusWhereFound:
        fields_to_show_dict['SearchStatusWhereFound'] = forms.CharField(required=False, max_length=255, label='Where Found', initial='')

    return fields_to_show_dict
