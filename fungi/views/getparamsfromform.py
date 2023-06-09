def get_params_from_form(form):
    q_params = {}
    field_name = 'CommonName'
    if field_name in form.fields:
        q_params["CommonName"] = form.cleaned_data['CommonName']
        # print('q_params2: ', q_params)

    field_name = 'OtherCommonNames'
    if field_name in form.fields:
        q_params["OtherCommonNames"] = form.cleaned_data['OtherCommonNames']

    field_name = 'LatinName'
    if field_name in form.fields:
        q_params["LatinName"] = form.cleaned_data['LatinName']
        # q_params["LatinSynonyms"] = form.cleaned_data['LatinName']

    field_name = 'LatinSynonyms'
    if field_name in form.fields:
        q_params["LatinSynonyms"] = form.cleaned_data['LatinSynonyms']

    field_name = 'Group'
    if field_name in form.fields:
        q_params["Group"] = form.cleaned_data['Group']
        # print('q_params2: ', q_params)

    field_name = 'HabitatAssociations'
    if field_name in form.fields:
        q_params["HabitatAssociations"] = form.cleaned_data['HabitatAssociations']

    field_name = 'HabitatPh'
    if field_name in form.fields:
        q_params["HabitatPh"] = form.cleaned_data['HabitatPh']

    field_name = 'HabitatSubstrate'
    if field_name in form.fields:
        q_params["HabitatSubstrate"] = form.cleaned_data['HabitatSubstrate']

    field_name = 'HabitatEnvironment'
    if field_name in form.fields:
        q_params["HabitatEnvironment"] = form.cleaned_data['HabitatEnvironment']

    field_name = 'HabitatSoil'
    if field_name in form.fields:
        q_params["HabitatSoil"] = form.cleaned_data['HabitatSoil']

    field_name = 'MonthFound'
    if field_name in form.fields:
        q_params["Season"] = form.cleaned_data['MonthFound']

    field_name = 'CapColour'
    if field_name in form.fields:
        q_params["CapColour"] = form.cleaned_data['CapColour']

    field_name = 'CapShape'
    if field_name in form.fields:
        q_params["CapShape"] = form.cleaned_data['CapShape']

    field_name = 'CapRim'
    if field_name in form.fields:
        q_params["CapRim"] = form.cleaned_data['CapRim']

    field_name = 'CapTexture'
    if field_name in form.fields:
        q_params["CapTexture"] = form.cleaned_data['CapTexture']

    field_name = 'CapBruiseColour'
    if field_name in form.fields:
        q_params["CapBruiseColour"] = form.cleaned_data['CapBruiseColour']

    field_name = 'CapCutColour'
    if field_name in form.fields:
        q_params["CapCutColour"] = form.cleaned_data['CapCutColour']

    field_name = 'CapWidth'
    if field_name in form.fields:
        q_params["CapWidth"] = form.cleaned_data['CapWidth']

    field_name = 'StipeColour'
    if field_name in form.fields:
        q_params["StipeColour"] = form.cleaned_data['StipeColour']

    field_name = 'StipeBruiseColour'
    if field_name in form.fields:
        q_params["StipeBruiseColour"] = form.cleaned_data['StipeBruiseColour']

    field_name = 'StipeCutColour'
    if field_name in form.fields:
        q_params["StipeCutColour"] = form.cleaned_data['StipeCutColour']

    field_name = 'StipeLength'
    if field_name in form.fields:
        q_params["StipeLength"] = form.cleaned_data['StipeLength']

    field_name = 'StipeThickness'
    if field_name in form.fields:
        q_params["StipeThickness"] = form.cleaned_data['StipeThickness']

    field_name = 'StipeShape'
    if field_name in form.fields:
        q_params["StipeShape"] = form.cleaned_data['StipeShape']

    field_name = 'StipeReticulationPresent'
    if field_name in form.fields:
        q_params["StipeReticulationPresent"] = form.cleaned_data['StipeReticulationPresent']

    field_name = 'StipeReticulation'
    if field_name in form.fields:
        q_params["StipeReticulation"] = form.cleaned_data['StipeReticulation']

    field_name = 'StipeBase'
    if field_name in form.fields:
        q_params["StipeBase"] = form.cleaned_data['StipeBase']

    field_name = 'StipeTexture'
    if field_name in form.fields:
        q_params["StipeTexture"] = form.cleaned_data['StipeTexture']

    field_name = 'StipeRing'
    if field_name in form.fields:
        q_params["StipeRing"] = form.cleaned_data['StipeRing']

    field_name = 'PoresPresent'
    if field_name in form.fields:
        q_params["PoresPresent"] = form.cleaned_data['PoresPresent']

    field_name = 'PoreColour'
    if field_name in form.fields:
        q_params["PoreColour"] = form.cleaned_data['PoreColour']

    field_name = 'PoreShape'
    if field_name in form.fields:
        q_params["PoreShape"] = form.cleaned_data['PoreShape']

    field_name = 'PoreBruiseColour'
    if field_name in form.fields:
        q_params["PoreBruiseColour"] = form.cleaned_data['PoreBruiseColour']

    field_name = 'TubeColour'
    if field_name in form.fields:
        q_params["TubeColour"] = form.cleaned_data['TubeColour']

    field_name = 'TubeShape'
    if field_name in form.fields:
        q_params["TubeShape"] = form.cleaned_data['TubeShape']

    field_name = 'TubeBruiseColour'
    if field_name in form.fields:
        q_params["TubeBruiseColour"] = form.cleaned_data['TubeBruiseColour']

    field_name = 'PoreMilk'
    if field_name in form.fields:
        q_params["PoreMilk"] = form.cleaned_data['PoreMilk']

    field_name = 'GillsPresent'
    if field_name in form.fields:
        q_params["GillsPresent"] = form.cleaned_data['GillsPresent']

    field_name = 'GillsColour'
    if field_name in form.fields:
        q_params["GillsColour"] = form.cleaned_data['GillsColour']

    field_name = 'GillsBruiseColour'
    if field_name in form.fields:
        q_params["GillsBruiseColour"] = form.cleaned_data['GillsBruiseColour']

    field_name = 'GillsCutColour'
    if field_name in form.fields:
        q_params["GillsCutColour"] = form.cleaned_data['GillsCutColour']

    field_name = 'GillsAttachment'
    if field_name in form.fields:
        q_params["GillsAttachment"] = form.cleaned_data['GillsAttachment']

    field_name = 'GillsArrangement'
    if field_name in form.fields:
        q_params["GillsArrangement"] = form.cleaned_data['GillsArrangement']

    field_name = 'GillsMilk'
    if field_name in form.fields:
        q_params["GillsMilk"] = form.cleaned_data['GillsMilk']

    field_name = 'FleshCapColour'
    if field_name in form.fields:
        q_params["FleshCapColour"] = form.cleaned_data['FleshCapColour']

    field_name = 'FleshCapBruiseColour'
    if field_name in form.fields:
        q_params["FleshCapBruiseColour"] = form.cleaned_data['FleshCapBruiseColour']

    field_name = 'FleshCapCutColour'
    if field_name in form.fields:
        q_params["FleshCapCutColour"] = form.cleaned_data['FleshCapCutColour']

    field_name = 'FleshStipeColour'
    if field_name in form.fields:
        q_params["FleshStipeColour"] = form.cleaned_data['FleshStipeColour']

    field_name = 'FleshStipeBruiseColour'
    if field_name in form.fields:
        q_params["FleshStipeBruiseColour"] = form.cleaned_data['FleshStipeBruiseColour']

    field_name = 'FleshStipeCutColour'
    if field_name in form.fields:
        q_params["FleshStipeCutColour"] = form.cleaned_data['FleshStipeCutColour']

    field_name = 'SporeColour'
    if field_name in form.fields:
        q_params["SporeColour"] = form.cleaned_data['SporeColour']

    field_name = 'Kingdom'
    if field_name in form.fields:
        q_params["Kingdom"] = form.cleaned_data['Kingdom']

    field_name = 'Phyum'
    if field_name in form.fields:
        q_params["Phyum"] = form.cleaned_data['Phyum']

    field_name = 'SubPhyum'
    if field_name in form.fields:
        q_params["SubPhyum"] = form.cleaned_data['SubPhyum']

    field_name = 'Class'
    if field_name in form.fields:
        q_params["Class"] = form.cleaned_data['Class']

    field_name = 'SubClass'
    if field_name in form.fields:
        q_params["SubClass"] = form.cleaned_data['SubClass']

    field_name = 'Order'
    if field_name in form.fields:
        q_params["Order"] = form.cleaned_data['Order']

    field_name = 'Family'
    if field_name in form.fields:
        q_params["Family"] = form.cleaned_data['Family']

    field_name = 'Genus'
    if field_name in form.fields:
        q_params["Genus"] = form.cleaned_data['Genus']

    field_name = 'PoisonType'
    if field_name in form.fields:
        q_params["PoisonType"] = form.cleaned_data['PoisonType']

    field_name = 'CulinaryRating'
    if field_name in form.fields:
        q_params["CulinaryRating"] = form.cleaned_data['CulinaryRating']

    field_name = 'Odour'
    if field_name in form.fields:
        q_params["Odour"] = form.cleaned_data['Odour']

    field_name = 'Taste'
    if field_name in form.fields:
        q_params["Taste"] = form.cleaned_data['Taste']

    field_name = 'StatusStatusData'
    if field_name in form.fields:
        q_params["StatusStatusData"] = form.cleaned_data['StatusStatusData']

    field_name = 'StatusWhereFound'
    if field_name in form.fields:
        q_params["StatusWhereFound"] = form.cleaned_data['StatusWhereFound']

    field_name = 'StatusRecordedInUK'
    if field_name in form.fields:
        q_params["StatusRecordedInUK"] = form.cleaned_data['StatusRecordedInUK']

    return q_params
