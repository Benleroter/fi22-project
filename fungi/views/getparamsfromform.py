def get_params_from_form(form):
    q_params = {}
    field_name = 'SearchCommonName'
    if field_name in form.fields:
        q_params["CommonName"] = form.cleaned_data['SearchCommonName']
        # print('q_params2: ', q_params)

    field_name = 'SearchOtherCommonNames'
    if field_name in form.fields:
        q_params["OtherCommonNames"] = form.cleaned_data['SearchOtherCommonNames']

    field_name = 'SearchLatinName'
    if field_name in form.fields:
        q_params["LatinName"] = form.cleaned_data['SearchLatinName']
        # q_params["LatinSynonyms"] = form.cleaned_data['SearchLatinName']

    field_name = 'SearchLatinSynonyms'
    if field_name in form.fields:
        q_params["LatinSynonyms"] = form.cleaned_data['SearchLatinSynonyms']

    field_name = 'SearchGroup'
    if field_name in form.fields:
        q_params["Group"] = form.cleaned_data['SearchGroup']
        # print('q_params2: ', q_params)

    field_name = 'SearchHabitatAssociations'
    if field_name in form.fields:
        q_params["HabitatAssociations"] = form.cleaned_data['SearchHabitatAssociations']

    field_name = 'SearchHabitatPh'
    if field_name in form.fields:
        q_params["HabitatPh"] = form.cleaned_data['SearchHabitatPh']

    field_name = 'SearchHabitatSubstrate'
    if field_name in form.fields:
        q_params["HabitatSubstrate"] = form.cleaned_data['SearchHabitatSubstrate']

    field_name = 'SearchHabitatEnvironment'
    if field_name in form.fields:
        q_params["HabitatEnvironment"] = form.cleaned_data['SearchHabitatEnvironment']

    field_name = 'SearchHabitatSoil'
    if field_name in form.fields:
        q_params["HabitatSoil"] = form.cleaned_data['SearchHabitatSoil']

    field_name = 'SearchMonthFound'
    if field_name in form.fields:
        q_params["Season"] = form.cleaned_data['SearchMonthFound']

    field_name = 'SearchCapColour'
    if field_name in form.fields:
        q_params["CapColour"] = form.cleaned_data['SearchCapColour']

    field_name = 'SearchCapShape'
    if field_name in form.fields:
        q_params["CapShape"] = form.cleaned_data['SearchCapShape']

    field_name = 'SearchCapRim'
    if field_name in form.fields:
        q_params["CapRim"] = form.cleaned_data['SearchCapRim']

    field_name = 'SearchCapTexture'
    if field_name in form.fields:
        q_params["CapTexture"] = form.cleaned_data['SearchCapTexture']

    field_name = 'SearchCapBruiseColour'
    if field_name in form.fields:
        q_params["CapBruiseColour"] = form.cleaned_data['SearchCapBruiseColour']

    field_name = 'SearchCapCutColour'
    if field_name in form.fields:
        q_params["CapCutColour"] = form.cleaned_data['SearchCapCutColour']

    field_name = 'SearchCapWidth'
    if field_name in form.fields:
        q_params["CapWidth"] = form.cleaned_data['SearchCapWidth']

    field_name = 'SearchStipeColour'
    if field_name in form.fields:
        q_params["StipeColour"] = form.cleaned_data['SearchStipeColour']

    field_name = 'SearchStipeBruiseColour'
    if field_name in form.fields:
        q_params["StipeBruiseColour"] = form.cleaned_data['SearchStipeBruiseColour']

    field_name = 'SearchStipeCutColour'
    if field_name in form.fields:
        q_params["StipeCutColour"] = form.cleaned_data['SearchStipeCutColour']

    field_name = 'SearchStipeLength'
    if field_name in form.fields:
        q_params["StipeLength"] = form.cleaned_data['SearchStipeLength']

    field_name = 'SearchStipeThickness'
    if field_name in form.fields:
        q_params["StipeThickness"] = form.cleaned_data['SearchStipeThickness']

    field_name = 'SearchStipeShape'
    if field_name in form.fields:
        q_params["StipeShape"] = form.cleaned_data['SearchStipeShape']

    field_name = 'SearchStipeReticulationPresent'
    if field_name in form.fields:
        q_params["StipeReticulationPresent"] = form.cleaned_data['SearchStipeReticulationPresent']

    field_name = 'SearchStipeReticulation'
    if field_name in form.fields:
        q_params["StipeReticulation"] = form.cleaned_data['SearchStipeReticulation']

    field_name = 'SearchStipeBase'
    if field_name in form.fields:
        q_params["StipeBase"] = form.cleaned_data['SearchStipeBase']

    field_name = 'SearchStipeTexture'
    if field_name in form.fields:
        q_params["StipeTexture"] = form.cleaned_data['SearchStipeTexture']

    field_name = 'SearchStipeRing'
    if field_name in form.fields:
        q_params["StipeRing"] = form.cleaned_data['SearchStipeRing']

    field_name = 'SearchPoresPresent'
    if field_name in form.fields:
        q_params["PoresPresent"] = form.cleaned_data['SearchPoresPresent']

    field_name = 'SearchPoreColour'
    if field_name in form.fields:
        q_params["PoreColour"] = form.cleaned_data['SearchPoreColour']

    field_name = 'SearchPoreShape'
    if field_name in form.fields:
        q_params["PoreShape"] = form.cleaned_data['SearchPoreShape']

    field_name = 'SearchPoreBruiseColour'
    if field_name in form.fields:
        q_params["PoreBruiseColour"] = form.cleaned_data['SearchPoreBruiseColour']

    field_name = 'SearchTubeColour'
    if field_name in form.fields:
        q_params["TubeColour"] = form.cleaned_data['SearchTubeColour']

    field_name = 'SearchTubeShape'
    if field_name in form.fields:
        q_params["TubeShape"] = form.cleaned_data['SearchTubeShape']

    field_name = 'SearchTubeBruiseColour'
    if field_name in form.fields:
        q_params["TubeBruiseColour"] = form.cleaned_data['SearchTubeBruiseColour']

    field_name = 'SearchPoreMilk'
    if field_name in form.fields:
        q_params["PoreMilk"] = form.cleaned_data['SearchPoreMilk']

    field_name = 'SearchGillsPresent'
    if field_name in form.fields:
        q_params["GillsPresent"] = form.cleaned_data['SearchGillsPresent']

    field_name = 'SearchGillsColour'
    if field_name in form.fields:
        q_params["GillsColour"] = form.cleaned_data['SearchGillsColour']

    field_name = 'SearchGillsBruiseColour'
    if field_name in form.fields:
        q_params["GillsBruiseColour"] = form.cleaned_data['SearchGillsBruiseColour']

    field_name = 'SearchGillsCutColour'
    if field_name in form.fields:
        q_params["GillsCutColour"] = form.cleaned_data['SearchGillsCutColour']

    field_name = 'SearchGillsAttachment'
    if field_name in form.fields:
        q_params["GillsAttachment"] = form.cleaned_data['SearchGillsAttachment']

    field_name = 'SearchGillsArrangement'
    if field_name in form.fields:
        q_params["GillsArrangement"] = form.cleaned_data['SearchGillsArrangement']

    field_name = 'SearchGillsMilk'
    if field_name in form.fields:
        q_params["GillsMilk"] = form.cleaned_data['SearchGillsMilk']

    field_name = 'SearchFleshCapColour'
    if field_name in form.fields:
        q_params["FleshCapColour"] = form.cleaned_data['SearchFleshCapColour']

    field_name = 'SearchFleshCapBruiseColour'
    if field_name in form.fields:
        q_params["FleshCapBruiseColour"] = form.cleaned_data['SearchFleshCapBruiseColour']

    field_name = 'SearchFleshCapCutColour'
    if field_name in form.fields:
        q_params["FleshCapCutColour"] = form.cleaned_data['SearchFleshCapCutColour']

    field_name = 'SearchFleshStipeColour'
    if field_name in form.fields:
        q_params["FleshStipeColour"] = form.cleaned_data['SearchFleshStipeColour']

    field_name = 'SearchFleshStipeBruiseColour'
    if field_name in form.fields:
        q_params["FleshStipeBruiseColour"] = form.cleaned_data['SearchFleshStipeBruiseColour']

    field_name = 'SearchFleshStipeCutColour'
    if field_name in form.fields:
        q_params["FleshStipeCutColour"] = form.cleaned_data['SearchFleshStipeCutColour']

    field_name = 'SearchSporeColour'
    if field_name in form.fields:
        q_params["SporeColour"] = form.cleaned_data['SearchSporeColour']

    field_name = 'SearchKingdom'
    if field_name in form.fields:
        q_params["Kingdom"] = form.cleaned_data['SearchKingdom']

    field_name = 'SearchPhyum'
    if field_name in form.fields:
        q_params["Phyum"] = form.cleaned_data['SearchPhyum']

    field_name = 'SearchSubPhyum'
    if field_name in form.fields:
        q_params["SubPhyum"] = form.cleaned_data['SearchSubPhyum']

    field_name = 'SearchClass'
    if field_name in form.fields:
        q_params["Class"] = form.cleaned_data['SearchClass']

    field_name = 'SearchSubClass'
    if field_name in form.fields:
        q_params["SubClass"] = form.cleaned_data['SearchSubClass']

    field_name = 'SearchOrder'
    if field_name in form.fields:
        q_params["Order"] = form.cleaned_data['SearchOrder']

    field_name = 'SearchFamily'
    if field_name in form.fields:
        q_params["Family"] = form.cleaned_data['SearchFamily']

    field_name = 'SearchGenus'
    if field_name in form.fields:
        q_params["Genus"] = form.cleaned_data['SearchGenus']

    field_name = 'SearchPoisonType'
    if field_name in form.fields:
        q_params["PoisonType"] = form.cleaned_data['SearchPoisonType']

    field_name = 'SearchCulinaryRating'
    if field_name in form.fields:
        q_params["CulinaryRating"] = form.cleaned_data['SearchCulinaryRating']

    field_name = 'SearchOdour'
    if field_name in form.fields:
        q_params["Odour"] = form.cleaned_data['SearchOdour']

    field_name = 'SearchTaste'
    if field_name in form.fields:
        q_params["Taste"] = form.cleaned_data['SearchTaste']

    field_name = 'SearchStatusStatusData'
    if field_name in form.fields:
        q_params["StatusStatusData"] = form.cleaned_data['SearchStatusStatusData']

    field_name = 'SearchStatusWhereFound'
    if field_name in form.fields:
        q_params["StatusWhereFound"] = form.cleaned_data['SearchStatusWhereFound']

    field_name = 'SearchStatusRecordedInUK'
    if field_name in form.fields:
        q_params["StatusRecordedInUK"] = form.cleaned_data['SearchStatusRecordedInUK']

    return q_params
