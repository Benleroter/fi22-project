from django import forms
# from fungi.views.choices import *
# from fungi.views.choices2 import *
from fungi.choices import *

def fields_to_show(user_search_fields):
    fields_to_show_dict = {}

    if user_search_fields.CommonName:
        fields_to_show_dict['CommonName'] = forms.CharField(required=False, max_length=255, label='Common Name', initial='cn')
        # print('fieldsToDisplay:::::::::::',fieldsToDisplay)

    if user_search_fields.LatinName:
        fields_to_show_dict['LatinName'] = forms.CharField(required=False, max_length=255, label='Latin Name', initial='')

    if user_search_fields.Group:
        fields_to_show_dict['Group'] = forms.CharField(required=False, max_length=255, label='Group', initial='')
        # print('fieldsToDisplay:::::::::::',  fields_to_show_dict['Group'])
    if user_search_fields.HabitatAssociations:
        fields_to_show_dict['HabitatAssociations'] = forms.CharField(required=False, max_length=255, label='Associated Trees', initial='')

    if user_search_fields.HabitatPh:
        print('user_search_fields.HabitatPh', user_search_fields.HabitatPh)
        fields_to_show_dict['HabitatPh'] = forms.ChoiceField(choices=PhTypeChoices, required=False, label='Ph', initial='')

    if user_search_fields.HabitatSubstrate:
        fields_to_show_dict['HabitatSubstrate'] = forms.CharField(required=False, max_length=255, label='Substrate', initial='')

    if user_search_fields.HabitatEnvironment:
        fields_to_show_dict['HabitatEnvironment'] = forms.CharField(required=False, max_length=255, label='Environment', initial='')

    if user_search_fields.HabitatSoil:
        fields_to_show_dict['HabitatSoil'] = forms.CharField(required=False, max_length=255, label='Soil type', initial='')

    if user_search_fields.MonthFound:
        print('user_search_fields.MonthFound',user_search_fields.MonthFound)
        fields_to_show_dict['MonthFound'] = forms.ChoiceField(choices=MonthFoundChoices, required=False, label='Month/Season Found', initial='month')

    if user_search_fields.CapColour:
        fields_to_show_dict['CapColour'] = forms.CharField(required=False, max_length=255, label='Cap Colour', initial='')

    if user_search_fields.CapShape:
        fields_to_show_dict['CapShape'] = forms.CharField(required=False, max_length=255, label='Cap Shape', initial='')

    if user_search_fields.CapRim:
        fields_to_show_dict['CapRim'] = forms.ChoiceField(choices=CapRimChoices, required=False, label='Cap Rim', initial='')

    if user_search_fields.CapTexture:
        fields_to_show_dict['CapTexture'] = forms.ChoiceField(choices=CapTextureChoices, required=False, label='Cap Texture', initial='')

    if user_search_fields.CapBruiseColour:
        fields_to_show_dict['CapBruiseColour'] = forms.CharField(required=False, max_length=255, label='Cap Bruise Colour', initial='')

    if user_search_fields.CapCutColour:
        fields_to_show_dict['CapCutColour'] = forms.CharField(required=False, max_length=255, label='Cap Cut Colour', initial='')

    if user_search_fields.CapWidth:
        fields_to_show_dict['CapWidth'] = forms.CharField(required=False, max_length=255, label='Cap Width', initial='')

    if user_search_fields.StipeColour:
        fields_to_show_dict['StipeColour'] = forms.CharField(required=False, max_length=255, label='Stipe Colour', initial='')

    if user_search_fields.StipeBruiseColour:
        fields_to_show_dict['StipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Bruise Colour', initial='')

    if user_search_fields.StipeCutColour:
        fields_to_show_dict['StipeCutColour'] = forms.CharField(required=False, max_length=255, label='Stipe Cut Colour', initial='')

    if user_search_fields.StipeLength:
        fields_to_show_dict['StipeLength'] = forms.CharField(required=False, max_length=255, label='Stipe Length', initial='')

    if user_search_fields.StipeThickness:
        fields_to_show_dict['StipeThickness'] = forms.CharField(required=False, max_length=255, label='Stipe Thickness', initial='')

    if user_search_fields.StipeShape:
        fields_to_show_dict['StipeShape'] = forms.CharField(required=False, max_length=255, label='Stipe Shape', initial='')

    if user_search_fields.StipeReticulationPresent:
        fields_to_show_dict['StipeReticulationPresent'] = forms.ChoiceField(choices=ReticulationChoices, required=False, label='Stipe Reticutaion Present', initial='')

    if user_search_fields.StipeReticulation:
        fields_to_show_dict['StipeReticulation'] = forms.CharField(required=False, max_length=255, label='Reticulation', initial='')

    if user_search_fields.StipeBase:
        fields_to_show_dict['StipeBase'] = forms.CharField(required=False, max_length=255, label='Stipe Base', initial='')

    if user_search_fields.StipeTexture:
        fields_to_show_dict['StipeTexture'] = forms.ChoiceField(choices=StipeTextureChoices, required=False, label='Stipe Texture', initial='')

    if user_search_fields.StipeRing:
        fields_to_show_dict['StipeRing'] = forms.ChoiceField(choices=StipeRingChoices, required=False, label='Stipe Ring', initial='')

    if user_search_fields.PoresPresent:
        fields_to_show_dict['PoresPresent'] = forms.ChoiceField(choices=PoresPresentChoices, required=False, label='Pores Present', initial='')

    if user_search_fields.PoreColour:
        fields_to_show_dict['PoreColour'] = forms.CharField(required=False, max_length=255, label='Pore Colour', initial='')

    if user_search_fields.PoreShape:
        fields_to_show_dict['PoreShape'] = forms.CharField(required=False, max_length=255, label='Pore Shape', initial='')

    if user_search_fields.PoreBruiseColour:
        fields_to_show_dict['PoreBruiseColour'] = forms.CharField(required=False, max_length=255, label='Pore Bruise Colour', initial='')

    if user_search_fields.TubeColour:
        fields_to_show_dict['TubeColour'] = forms.CharField(required=False, max_length=255, label='Tube Colour', initial='')

    if user_search_fields.TubeShape:
        fields_to_show_dict['TubeShape'] = forms.CharField(required=False, max_length=255, label='Tube Shap', initial='')

    if user_search_fields.TubeBruiseColour:
        fields_to_show_dict['TubeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Tube Bruise Colour', initial='')

    if user_search_fields.PoreMilk:
        fields_to_show_dict['PoreMilk'] = forms.ChoiceField(choices=PoresMilkChoices, required=False, label='Pore Milk', initial='')

    if user_search_fields.GillsPresent:
        fields_to_show_dict['GillsPresent'] = forms.ChoiceField(choices=GillsPresentChoices, required=False, label='Gills Present', initial='')

    if user_search_fields.GillsColour:
        fields_to_show_dict['GillsColour'] = forms.CharField(required=False, max_length=255, label='Gills Colour', initial='')

    if user_search_fields.GillsBruiseColour:
        fields_to_show_dict['GillsBruiseColour'] = forms.CharField(required=False, max_length=255, label='Gills Bruise Colour', initial='')

    if user_search_fields.GillsCutColour:
        fields_to_show_dict['GillsCutColour'] = forms.CharField(required=False, max_length=255, label='Gills Cut Colour', initial='')

    if user_search_fields.GillsAttachment:
        fields_to_show_dict['GillsAttachment'] = forms.CharField(required=False, max_length=255, label='Gills Attachment', initial='')

    if user_search_fields.GillsArrangement:
        fields_to_show_dict['GillsArrangement'] = forms.CharField(required=False, max_length=255, label='Gills Arrangement', initial='')

    if user_search_fields.GillsMilk:
        fields_to_show_dict['GillsMilk'] = forms.ChoiceField(choices=GillsMilkChoices, required=False, label='Gill Milk', initial='')

    if user_search_fields.FleshCapColour:
        fields_to_show_dict['FleshCapColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Colour ', initial='')

    if user_search_fields.FleshCapBruiseColour:
        fields_to_show_dict['FleshCapBruiseColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Bruise Colour', initial='')

    if user_search_fields.FleshCapCutColour:
        fields_to_show_dict['FleshCapCutColour'] = forms.CharField(required=False, max_length=255, label='Cap Flesh Cut Colour', initial='')

    if user_search_fields.FleshStipeColour:
        fields_to_show_dict['FleshStipeColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Colour', initial='')

    if user_search_fields.FleshStipeBruiseColour:
        fields_to_show_dict['FleshStipeBruiseColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Bruise Colour', initial='')

    if user_search_fields.FleshStipeCutColour:
        fields_to_show_dict['FleshStipeCutColour'] = forms.CharField(required=False, max_length=255, label='Stipe Flesh Cut Colour', initial='')

    if user_search_fields.SporeColour:
        fields_to_show_dict['SporeColour'] = forms.CharField(required=False, max_length=255, label='Spore Colour', initial='')

    if user_search_fields.OtherCommonNames:
        fields_to_show_dict['OtherCommonNames'] = forms.CharField(required=False, max_length=255, label='Other Common Name', initial='')

    if user_search_fields.LatinSynonyms:
        fields_to_show_dict['LatinSynonyms'] = forms.CharField(required=False, max_length=255, label='Latin Synonym', initial='')

    if user_search_fields.Kingdom:
        fields_to_show_dict['Kingdom'] = forms.CharField(required=False, max_length=255, label='Taxonmic Kingdom', initial='')

    if user_search_fields.Phyum:
        fields_to_show_dict['Phyum'] = forms.CharField(required=False, max_length=255, label='Taxonmic Phyum', initial='')

    if user_search_fields.SubPhyum:
        fields_to_show_dict['SubPhyum'] = forms.CharField(required=False, max_length=255, label='Taxonmic SubPhyum', initial='')

    if user_search_fields.Class:
        fields_to_show_dict['Class'] = forms.CharField(required=False, max_length=255, label='Taxonmic Class', initial='')

    if user_search_fields.SubClass:
        fields_to_show_dict['SubClass'] = forms.CharField(required=False, max_length=255, label='Taxonmic SubClass', initial='')

    if user_search_fields.Order:
        fields_to_show_dict['Order'] = forms.CharField(required=False, max_length=255, label='Taxonmic Order', initial='')

    if user_search_fields.Family:
        fields_to_show_dict['Family'] = forms.CharField(required=False, max_length=255, label='Taxonmic Family', initial='')

    if user_search_fields.Genus:
        fields_to_show_dict['Genus'] = forms.CharField(required=False, max_length=255, label='Taxonmic Genus', initial='')

    if user_search_fields.PoisonType:
        fields_to_show_dict['PoisonType'] = forms.CharField(required=False, max_length=255, label='Poison Type', initial='')

    if user_search_fields.CulinaryRating:
        fields_to_show_dict['CulinaryRating'] = forms.ChoiceField(choices=CulinaryRatingChoices, required=False, label='Culinary Rating', initial='')
        # fieldsToDisplay['CulinaryRating'] = forms.CharField(required=False, max_length=255, label='Culinary Rating', initial='')

    if user_search_fields.Odour:
        fields_to_show_dict['Odour'] = forms.CharField(required=False, max_length=255, label='Odour', initial='')

    if user_search_fields.Taste:
        fields_to_show_dict['Taste'] = forms.CharField(required=False, max_length=255, label='Taste', initial='')

    if user_search_fields.StatusStatusData:
        fields_to_show_dict['StatusStatusData'] = forms.CharField(required=False, max_length=255, label='Status', initial='')

    if user_search_fields.StatusWhereFound:
        fields_to_show_dict['StatusWhereFound'] = forms.CharField(required=False, max_length=255, label='Where Found', initial='')

    return fields_to_show_dict
