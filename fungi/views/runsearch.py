from fungi.models import *
from django.db.models import Q
from django.apps import apps
# from itertools import chain
import collections


def run_search(q_params):
    # FoundList = []
    # QueryComponents = {}
    qclist = []
    resultslist = []
    resultslist2 = []
    synonymlist = []
    synonymlist2 = []
    commonnameslist = []
    commonnameslist2 = []

    # SearchModels =[]
    searchterms_count = 0
    matches = []

    print('q_params =', q_params)

    for p in q_params:
        searchterms_count += 1
        # print('searchterms_count =', str(searchterms_count))

    print('q_params-runsearch', q_params)

    for i in q_params:
        if i == 'CommonName':
            commonnamedict = {}
            # commonnamedict['searchterm'] = q_params[i]
            searchterm = q_params[i]
            commonnamedict['table'] = 'Fungi'
            commonnamedict['column'] = 'CommonName'
            commonnamedict['qstr'] = '__icontains'
            commonnamedict['model'] = apps.get_model(app_label='fungi', model_name='Fungi')
            qclist.append(commonnamedict)
            name_list = commonnamedict['model'].objects.filter(Q(**{commonnamedict['column'] + commonnamedict['qstr']: searchterm}))
            for name in name_list:
                print('name = ', name)
                resultslist.append(name.id)

            othercommonnamesdict = {}
            othercommonnamesdict['table'] = 'OtherCommonNames'
            othercommonnamesdict['column'] = 'AltCommonName'
            othercommonnamesdict['qstr'] = '__icontains'
            othercommonnamesdict['model'] = apps.get_model(app_label='fungi', model_name=othercommonnamesdict['table'])
            othercommonnames_list = othercommonnamesdict['model'].objects.filter(Q(**{othercommonnamesdict['column'] + othercommonnamesdict['qstr']: searchterm}))
            for other_name in othercommonnames_list:
                if other_name.Fungi_id not in resultslist:
                    resultslist.append(other_name.Fungi_id)
                    commonnameslist.append(other_name.Fungi_id)

        elif i == "OtherCommonNames":
            othercommonnamesdict = {}
            othercommonnamesdict['searchterm'] = q_params[i]
            othercommonnamesdict['table'] = 'OtherCommonNames'
            othercommonnamesdict['column'] = 'AltCommonName'
            othercommonnamesdict['qstr'] = '__icontains'
            othercommonnamesdict['model'] = apps.get_model(app_label='fungi', model_name=othercommonnamesdict['table'])
            othercommonnames_list = othercommonnamesdict['model'].objects.filter(Q(**{othercommonnamesdict['column'] + othercommonnamesdict['qstr']: othercommonnamesdict['searchterm']}))
            for ocn in othercommonnames_list:
                resultslist.append(ocn.Fungi_id)


        elif i == "LatinName":
            latinnamedict = {}
            searchterm = q_params[i]
            latinnamedict['table'] = 'Fungi'
            latinnamedict['column'] = 'LatinName'
            latinnamedict['qstr'] = '__icontains'
            latinnamedict['model'] = apps.get_model(app_label='fungi', model_name='Fungi')
            latinname_list = latinnamedict['model'].objects.filter(Q(**{latinnamedict['column'] + latinnamedict['qstr']: searchterm}))
            for ln in latinname_list:
                resultslist.append(ln.id)

            latinsynonymsdict = {}
            latinsynonymsdict['table'] = 'LatinSynonyms'
            latinsynonymsdict['column'] = 'LatinSynonym'
            latinsynonymsdict['qstr'] = '__icontains'
            latinsynonymsdict['model'] = apps.get_model(app_label='fungi', model_name=latinsynonymsdict['table'])
            latinsynonyms_list = latinsynonymsdict['model'].objects.filter(Q(**{latinsynonymsdict['column'] + latinsynonymsdict['qstr']: searchterm}))
            for ls in latinsynonyms_list:
                if ls.Fungi_id not in resultslist:
                    resultslist.append(ls.Fungi_id)
                    synonymlist.append(ls.Fungi_id)

        elif i == "LatinSynonyms":
            latinsynonymsdict = {}
            latinsynonymsdict['searchterm'] = q_params[i]
            latinsynonymsdict['table'] = 'LatinSynonyms'
            latinsynonymsdict['column'] = 'LatinSynonym'
            latinsynonymsdict['qstr'] = '__icontains'
            latinsynonymsdict['model'] = apps.get_model(app_label='fungi', model_name=latinsynonymsdict['table'])
            latinsynonyms_list = latinsynonymsdict['model'].objects.filter(Q(**{latinsynonymsdict['column'] + latinsynonymsdict['qstr']: latinsynonymsdict['searchterm']}))
            for l in latinsynonyms_list:
                resultslist.append(l.Fungi_id)
                synonymlist.append(l.Fungi_id)



        elif i == "Group":
            groupdict = {}
            groupdict['searchterm'] = q_params[i]
            groupdict['table'] = 'Fungi'
            groupdict['column'] = 'Group'
            groupdict['qstr'] = '__icontains'
            groupdict['model'] = apps.get_model(app_label='fungi', model_name='Fungi')
            groupdict_list = groupdict['model'].objects.filter(Q(**{groupdict['column'] + groupdict['qstr']: groupdict['searchterm']}))
            for gd in groupdict_list:
                resultslist.append(gd.id)


        elif i == "HabitatAssociations":
            habitatassociationsdict = {}
            habitatassociationsdict['searchterm'] = q_params[i]
            habitatassociationsdict['table'] = 'Habitat'
            habitatassociationsdict['column'] = 'Associations'
            habitatassociationsdict['qstr'] = '__icontains'
            habitatassociationsdict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')

            qclist.append(habitatassociationsdict)
            habitat_list = habitatassociationsdict['model'].objects.filter(Q(**{habitatassociationsdict['column'] + habitatassociationsdict['qstr']: habitatassociationsdict['searchterm']}))
            for hl in habitat_list:
                resultslist.append(hl.Fungi_id)

        elif i == "HabitatPh":
            habitatphdict = {}
            habitatphdict['searchterm'] = q_params[i]
            habitatphdict['table'] = 'Habitat'
            habitatphdict['column'] = 'Ph'
            habitatphdict['qstr'] = '__icontains'
            habitatphdict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
            habitatph_list = habitatphdict['model'].objects.filter(Q(**{habitatphdict['column'] + habitatphdict['qstr']: habitatphdict['searchterm']}))
            for hph in habitatph_list:
                resultslist.append(hph.Fungi_id)

        elif i == "HabitatSoil":
            habitatsoildict = {}
            habitatsoildict['searchterm'] = q_params[i]
            habitatsoildict['table'] = 'Habitat'
            habitatsoildict['column'] = 'Soil'
            habitatsoildict['qstr'] = '__icontains'
            habitatsoildict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
            habitatsoil_list = habitatsoildict['model'].objects.filter(Q(**{habitatsoildict['column'] + habitatsoildict['qstr']: habitatsoildict['searchterm']}))
            for hsl in habitatsoil_list:
                resultslist.append(hsl.Fungi_id)

        elif i == "HabitatSubstrate":
            habitatsubstratedict = {}
            habitatsubstratedict['searchterm'] = q_params[i]
            habitatsubstratedict['table'] = 'Habitat'
            habitatsubstratedict['column'] = 'Substrate'
            habitatsubstratedict['qstr'] = '__icontains'
            habitatsubstratedict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
            habitatsubstratedict = habitatsubstratedict['model'].objects.filter(Q(**{habitatsubstratedict['column'] + habitatsubstratedict['qstr']: habitatsubstratedict['searchterm']}))
            for hss in habitatsubstratedict:
                resultslist.append(hss.Fungi_id)

        elif i == "HabitatEnvironment":
            habitatenvironmentdict = {}
            habitatenvironmentdict['searchterm'] = q_params[i]
            habitatenvironmentdict['table'] = 'Habitat'
            habitatenvironmentdict['column'] = 'Environment'
            habitatenvironmentdict['qstr'] = '__icontains'
            habitatenvironmentdict['model'] = apps.get_model(app_label='fungi', model_name='Habitat')
            habitatenvironmentdict = habitatenvironmentdict['model'].objects.filter(Q(**{habitatenvironmentdict['column'] + habitatenvironmentdict['qstr']: habitatenvironmentdict['searchterm']}))
            for he in habitatenvironmentdict:
                resultslist.append(he.Fungi_id)

        elif i == "Season":
            seasondict = {}
            seasondict['searchterm'] = q_params[i]
            seasondict['table'] = 'Seasons'
            seasondict['column'] = 'Season'
            seasondict['qstr'] = '__icontains'
            seasondict['model'] = apps.get_model(app_label='fungi', model_name='Seasons')
            qclist.append(seasondict)
            season_list = seasondict['model'].objects.filter(Q(**{seasondict['column'] + seasondict['qstr']: seasondict['searchterm']}))
            for sl in season_list:
                resultslist.append(sl.Fungi_id)

        elif i == "CapColour":
            capcolourdict = {}
            capcolourdict['searchterm'] = q_params[i]
            capcolourdict['table'] = 'FruitingBody'
            capcolourdict['column'] = 'Colour'
            capcolourdict['qstr'] = '__icontains'
            capcolourdict['model'] = apps.get_model(app_label='fungi', model_name=capcolourdict['table'])
            capcolour_list = capcolourdict['model'].objects.filter(Q(**{capcolourdict['column'] + capcolourdict['qstr']: capcolourdict['searchterm']}))
            for cc in capcolour_list:
                resultslist.append(cc.Fungi_id)

        elif i == "CapShape":
            capshapedict = {}
            capshapedict['searchterm'] = q_params[i]
            capshapedict['table'] = 'FruitingBody'
            capshapedict['column'] = 'Shape'
            capshapedict['qstr'] = '__icontains'
            capshapedict['model'] = apps.get_model(app_label='fungi', model_name=capshapedict['table'])
            capshape_list = capshapedict['model'].objects.filter(Q(**{capshapedict['column'] + capshapedict['qstr']: capshapedict['searchterm']}))
            for cs in capshape_list:
                resultslist.append(cs.Fungi_id)

        elif i == "CapRim":
            caprimdict = {}
            caprimdict['searchterm'] = q_params[i]
            caprimdict['table'] = 'FruitingBody'
            caprimdict['column'] = 'Rim'
            caprimdict['qstr'] = '__icontains'
            caprimdict['model'] = apps.get_model(app_label='fungi', model_name=caprimdict['table'])
            caprim_list = caprimdict['model'].objects.filter(Q(**{caprimdict['column'] + caprimdict['qstr']: caprimdict['searchterm']}))
            for cr in caprim_list:
                resultslist.append(cr.Fungi_id)

        elif i == "CapTexture":
            captexturedict = {}
            captexturedict['searchterm'] = q_params[i]
            captexturedict['table'] = 'FruitingBody'
            captexturedict['column'] = 'CapTexture'
            captexturedict['qstr'] = '__icontains'
            captexturedict['model'] = apps.get_model(app_label='fungi', model_name=captexturedict['table'])
            captexture_list = captexturedict['model'].objects.filter(Q(**{captexturedict['column'] + captexturedict['qstr']: captexturedict['searchterm']}))
            for ct in captexture_list:
                resultslist.append(ct.Fungi_id)

        elif i == "CapBruiseColour":
            capbruisecolourdict = {}
            capbruisecolourdict['searchterm'] = q_params[i]
            capbruisecolourdict['table'] = 'FruitingBody'
            capbruisecolourdict['column'] = 'BruiseColour'
            capbruisecolourdict['qstr'] = '__icontains'
            capbruisecolourdict['model'] = apps.get_model(app_label='fungi', model_name=capbruisecolourdict['table'])

            qclist.append(capbruisecolourdict)
            capbruisecolour_list = capbruisecolourdict['model'].objects.filter(Q(**{capbruisecolourdict['column'] + capbruisecolourdict['qstr']: capbruisecolourdict['searchterm']}))
            for cbc in capbruisecolour_list:
                resultslist.append(cbc.Fungi_id)

        elif i == "CapCutColour":
            capcutcolourdict = {}
            capcutcolourdict['searchterm'] = q_params[i]
            capcutcolourdict['table'] = 'FruitingBody'
            capcutcolourdict['column'] = 'CutColour'
            capcutcolourdict['qstr'] = '__icontains'
            capcutcolourdict['model'] = apps.get_model(app_label='fungi', model_name=capcutcolourdict['table'])

            qclist.append(capcutcolourdict)
            capcutcolour_list = capcutcolourdict['model'].objects.filter(Q(**{capcutcolourdict['column'] + capcutcolourdict['qstr']: capcutcolourdict['searchterm']}))
            for ccc in capcutcolour_list:
                resultslist.append(ccc.Fungi_id)

        elif i == "CapWidth":
            capwidthdict = {}
            capwidthdict['searchterm'] = q_params[i]
            capwidthdict['table'] = 'FruitingBody'
            capwidthdict['column1'] = 'WidthMin'
            capwidthdict['column2'] = 'WidthMax'
            capwidthdict['qstr1'] = '__lte'
            capwidthdict['qstr2'] = '__gte'
            capwidthdict['model'] = apps.get_model(app_label='fungi', model_name=capwidthdict['table'])
            capwidth_list = capwidthdict['model'].objects.filter(Q(**{capwidthdict['column1'] + capwidthdict['qstr1']: capwidthdict['searchterm']}) & Q(**{capwidthdict['column2'] + capwidthdict['qstr2']: capwidthdict['searchterm']}))
            for cw in capwidth_list:
                resultslist.append(cw.Fungi_id)

        elif i == "StipeColour":
            stipecolourdict = {}
            stipecolourdict['searchterm'] = q_params[i]
            stipecolourdict['table'] = 'Stipe'
            stipecolourdict['column'] = 'Colour'
            stipecolourdict['qstr'] = '__icontains'
            stipecolourdict['model'] = apps.get_model(app_label='fungi', model_name=stipecolourdict['table'])

            qclist.append(stipecolourdict)
            stipecolour_list = stipecolourdict['model'].objects.filter(Q(**{stipecolourdict['column'] + stipecolourdict['qstr']: stipecolourdict['searchterm']}))
            for sc in stipecolour_list:
                resultslist.append(sc.Fungi_id)

        elif i == "StipeBruiseColour":
            stipebruisecolourdict = {}
            stipebruisecolourdict['searchterm'] = q_params[i]
            stipebruisecolourdict['table'] = 'Stipe'
            stipebruisecolourdict['column'] = 'BruiseColour'
            stipebruisecolourdict['qstr'] = '__icontains'
            stipebruisecolourdict['model'] = apps.get_model(app_label='fungi', model_name=stipebruisecolourdict['table'])

            qclist.append(stipebruisecolourdict)
            stipebruisecolour_list = stipebruisecolourdict['model'].objects.filter(Q(**{stipebruisecolourdict['column'] + stipebruisecolourdict['qstr']: stipebruisecolourdict['searchterm']}))
            for sbc in stipebruisecolour_list:
                resultslist.append(sbc.Fungi_id)

        elif i == "StipeCutColour":
            stipecutcolourdict = {}
            stipecutcolourdict['searchterm'] = q_params[i]
            stipecutcolourdict['table'] = 'Stipe'
            stipecutcolourdict['column'] = 'CutColour'
            stipecutcolourdict['qstr'] = '__icontains'
            stipecutcolourdict['model'] = apps.get_model(app_label='fungi', model_name=stipecutcolourdict['table'])

            qclist.append(stipecutcolourdict)
            stipecutcolour_list = stipecutcolourdict['model'].objects.filter(Q(**{stipecutcolourdict['column'] + stipecutcolourdict['qstr']: stipecutcolourdict['searchterm']}))
            for scc in stipecutcolour_list:
                resultslist.append(scc.Fungi_id)

        elif i == "StipeLength":
            stipelengthdict = {}
            stipelengthdict['searchterm'] = q_params[i]
            stipelengthdict['table'] = 'Stipe'
            stipelengthdict['column1'] = 'LengthMin'
            stipelengthdict['column2'] = 'LengthMax'
            stipelengthdict['qstr1'] = '__lte'
            stipelengthdict['qstr2'] = '__gte'
            stipelengthdict['model'] = apps.get_model(app_label='fungi', model_name=stipelengthdict['table'])
            qclist.append(stipelengthdict)
            stipelength_list = stipelengthdict['model'].objects.filter(
                Q(**{stipelengthdict['column1'] + stipelengthdict['qstr1']: stipelengthdict['searchterm']}) & Q(**{stipelengthdict['column2'] + stipelengthdict['qstr2']: stipelengthdict['searchterm']}))
            for sl in stipelength_list:
                resultslist.append(sl.Fungi_id)

        elif i == "StipeThickness":
            stipethicknessdict = {}
            stipethicknessdict['searchterm'] = q_params[i]
            stipethicknessdict['table'] = 'Stipe'
            stipethicknessdict['column1'] = 'ThicknessMin'
            stipethicknessdict['column2'] = 'ThicknessMax'
            stipethicknessdict['qstr1'] = '__lte'
            stipethicknessdict['qstr2'] = '__gte'
            stipethicknessdict['model'] = apps.get_model(app_label='fungi', model_name=stipethicknessdict['table'])
            qclist.append(stipethicknessdict)
            stipethickness_list = stipethicknessdict['model'].objects.filter(
                Q(**{stipethicknessdict['column1'] + stipethicknessdict['qstr1']: stipethicknessdict['searchterm']}) & Q(**{stipethicknessdict['column2'] + stipethicknessdict['qstr2']: stipethicknessdict['searchterm']}))
            for st in stipethickness_list:
                resultslist.append(st.Fungi_id)

        elif i == "StipeShape":
            stipedescriptiondict = {}
            stipedescriptiondict['searchterm'] = q_params[i]
            stipedescriptiondict['table'] = 'Stipe'
            stipedescriptiondict['column'] = 'Shape'
            stipedescriptiondict['qstr'] = '__icontains'
            stipedescriptiondict['model'] = apps.get_model(app_label='fungi', model_name=stipedescriptiondict['table'])
            stipedescription_list = stipedescriptiondict['model'].objects.filter(Q(**{stipedescriptiondict['column'] + stipedescriptiondict['qstr']: stipedescriptiondict['searchterm']}))
            for sd in stipedescription_list:
                resultslist.append(sd.Fungi_id)

        elif i == "StipeReticulationPresent":
            stipereticulationpresentdict = {}
            stipereticulationpresentdict['searchterm'] = q_params[i]
            stipereticulationpresentdict['table'] = 'Stipe'
            stipereticulationpresentdict['column'] = 'ReticulationPresent'
            stipereticulationpresentdict['qstr'] = '__icontains'
            stipereticulationpresentdict['model'] = apps.get_model(app_label='fungi', model_name=stipereticulationpresentdict['table'])
            stipereticulationpresent_list = stipereticulationpresentdict['model'].objects.filter(Q(**{stipereticulationpresentdict['column'] + stipereticulationpresentdict['qstr']: stipereticulationpresentdict['searchterm']}))
            for srp in stipereticulationpresent_list:
                resultslist.append(srp.Fungi_id)

        elif i == "StipeReticulation":
            stipereticulationdict = {}
            stipereticulationdict['searchterm'] = q_params[i]
            stipereticulationdict['table'] = 'Stipe'
            stipereticulationdict['column'] = 'Reticulation'
            stipereticulationdict['qstr'] = '__icontains'
            stipereticulationdict['model'] = apps.get_model(app_label='fungi', model_name=stipereticulationdict['table'])
            stipereticulation_list = stipereticulationdict['model'].objects.filter(Q(**{stipereticulationdict['column'] + stipereticulationdict['qstr']: stipereticulationdict['searchterm']}))
            for sr in stipereticulation_list:
                resultslist.append(sr.Fungi_id)


        elif i == "StipeBase":
            stipebasedict = {}
            stipebasedict['searchterm'] = q_params[i]
            stipebasedict['table'] = 'Stipe'
            stipebasedict['column'] = 'Base'
            stipebasedict['qstr'] = '__icontains'
            stipebasedict['model'] = apps.get_model(app_label='fungi', model_name=stipebasedict['table'])
            stipebase_list = stipebasedict['model'].objects.filter(Q(**{stipebasedict['column'] + stipebasedict['qstr']: stipebasedict['searchterm']}))
            for sb in stipebase_list:
                resultslist.append(sb.Fungi_id)

        elif i == "StipeTexture":
            stipetexturedict = {}
            stipetexturedict['searchterm'] = q_params[i]
            stipetexturedict['table'] = 'Stipe'
            stipetexturedict['column'] = 'Texture'
            stipetexturedict['qstr'] = '__icontains'
            stipetexturedict['model'] = apps.get_model(app_label='fungi', model_name=stipetexturedict['table'])
            stipetexture_list = stipetexturedict['model'].objects.filter(Q(**{stipetexturedict['column'] + stipetexturedict['qstr']: stipetexturedict['searchterm']}))
            for stx in stipetexture_list:
                resultslist.append(stx.Fungi_id)

        elif i == "StipeRing":
            stiperingdict = {}
            stiperingdict['searchterm'] = q_params[i]
            stiperingdict['table'] = 'Stipe'
            stiperingdict['column'] = 'Ring'
            stiperingdict['qstr'] = '__icontains'
            stiperingdict['model'] = apps.get_model(app_label='fungi', model_name=stiperingdict['table'])
            stipering_list = stiperingdict['model'].objects.filter(Q(**{stiperingdict['column'] + stiperingdict['qstr']: stiperingdict['searchterm']}))
            for sr in stipering_list:
                resultslist.append(sr.Fungi_id)

        elif i == "PoresPresent":
            porespresentdict = {}
            porespresentdict['searchterm'] = q_params[i]
            porespresentdict['table'] = 'PoresAndTubes'
            porespresentdict['column'] = 'PoresPresent'
            porespresentdict['qstr'] = '__iexact'
            porespresentdict['model'] = apps.get_model(app_label='fungi', model_name=porespresentdict['table'])
            porespresent_list = porespresentdict['model'].objects.filter(Q(**{porespresentdict['column'] + porespresentdict['qstr']: porespresentdict['searchterm']}))
            for pp in porespresent_list:
                resultslist.append(pp.Fungi_id)

        elif i == "PoreColour":
            porescolourdict = {}
            porescolourdict['searchterm'] = q_params[i]
            porescolourdict['table'] = 'PoresAndTubes'
            porescolourdict['column'] = 'PoreColour'
            porescolourdict['qstr'] = '__icontains'
            porescolourdict['model'] = apps.get_model(app_label='fungi', model_name=porescolourdict['table'])
            porescolour_list = porescolourdict['model'].objects.filter(Q(**{porescolourdict['column'] + porescolourdict['qstr']: porescolourdict['searchterm']}))
            for pc in porescolour_list:
                resultslist.append(pc.Fungi_id)

        elif i == "PoreShape":
            poresshapedict = {}
            poresshapedict['searchterm'] = q_params[i]
            poresshapedict['table'] = 'PoresAndTubes'
            poresshapedict['column'] = 'PoreShape'
            poresshapedict['qstr'] = '__icontains'
            poresshapedict['model'] = apps.get_model(app_label='fungi', model_name=poresshapedict['table'])
            poresshape_list = poresshapedict['model'].objects.filter(Q(**{poresshapedict['column'] + poresshapedict['qstr']: poresshapedict['searchterm']}))
            for ps in poresshape_list:
                resultslist.append(ps.Fungi_id)

        elif i == "PoreBruiseColour":
            poresbruisecolourdict = {}
            poresbruisecolourdict['searchterm'] = q_params[i]
            poresbruisecolourdict['table'] = 'PoresAndTubes'
            poresbruisecolourdict['column'] = 'PoreBruiseColour'
            poresbruisecolourdict['qstr'] = '__icontains'
            poresbruisecolourdict['model'] = apps.get_model(app_label='fungi', model_name=poresbruisecolourdict['table'])
            poresbruisecolour_list = poresbruisecolourdict['model'].objects.filter(Q(**{poresbruisecolourdict['column'] + poresbruisecolourdict['qstr']: poresbruisecolourdict['searchterm']}))
            for pbc in poresbruisecolour_list:
                resultslist.append(pbc.Fungi_id)

        elif i == "TubeColour":
            tubecolourdict = {}
            tubecolourdict['searchterm'] = q_params[i]
            tubecolourdict['table'] = 'PoresAndTubes'
            tubecolourdict['column'] = 'TubeColour'
            tubecolourdict['qstr'] = '__icontains'
            tubecolourdict['model'] = apps.get_model(app_label='fungi', model_name=tubecolourdict['table'])
            tubecolour_list = tubecolourdict['model'].objects.filter(Q(**{tubecolourdict['column'] + tubecolourdict['qstr']: tubecolourdict['searchterm']}))
            for tc in tubecolour_list:
                resultslist.append(tc.Fungi_id)

        elif i == "TubeShape":
            tubeshapedict = {}
            tubeshapedict['searchterm'] = q_params[i]
            tubeshapedict['table'] = 'PoresAndTubes'
            tubeshapedict['column'] = 'TubeShape'
            tubeshapedict['qstr'] = '__icontains'
            tubeshapedict['model'] = apps.get_model(app_label='fungi', model_name=tubeshapedict['table'])
            tubeshape_list = tubeshapedict['model'].objects.filter(Q(**{tubeshapedict['column'] + tubeshapedict['qstr']: tubeshapedict['searchterm']}))
            for ts in tubeshape_list:
                resultslist.append(ts.Fungi_id)

        elif i == "TubeBruiseColour":
            tubebruisecolour = {}
            tubebruisecolour['searchterm'] = q_params[i]
            tubebruisecolour['table'] = 'PoresAndTubes'
            tubebruisecolour['column'] = 'TubeBruiseColour'
            tubebruisecolour['qstr'] = '__icontains'
            tubebruisecolour['model'] = apps.get_model(app_label='fungi', model_name=tubebruisecolour['table'])
            tubebruisecolour_list = tubebruisecolour['model'].objects.filter(Q(**{tubebruisecolour['column'] + tubebruisecolour['qstr']: tubebruisecolour['searchterm']}))
            for tbc in tubebruisecolour_list:
                resultslist.append(tbc.Fungi_id)

        elif i == "PoreMilk":
            poremilkdict = {}
            poremilkdict['searchterm'] = q_params[i]
            poremilkdict['table'] = 'PoresAndTubes'
            poremilkdict['column'] = 'Milk'
            poremilkdict['qstr'] = '__icontains'
            poremilkdict['model'] = apps.get_model(app_label='fungi', model_name=poremilkdict['table'])
            poremilk_list = poremilkdict['model'].objects.filter(Q(**{poremilkdict['column'] + poremilkdict['qstr']: poremilkdict['searchterm']}))
            for pm in poremilk_list:
                resultslist.append(pm.Fungi_id)

        elif i == "GillsPresent":
            gillspresentdict = {}
            gillspresentdict['searchterm'] = q_params[i]
            gillspresentdict['table'] = 'Gills'
            gillspresentdict['column'] = 'GillsPresent'
            gillspresentdict['qstr'] = '__iexact'
            gillspresentdict['model'] = apps.get_model(app_label='fungi', model_name=gillspresentdict['table'])
            gillspresent_list = gillspresentdict['model'].objects.filter(Q(**{gillspresentdict['column'] + gillspresentdict['qstr']: gillspresentdict['searchterm']}))
            for gp in gillspresent_list:
                resultslist.append(gp.Fungi_id)

        elif i == "GillsColour":
            gillscolourdict = {}
            gillscolourdict['searchterm'] = q_params[i]
            gillscolourdict['table'] = 'Gills'
            gillscolourdict['column'] = 'Colour'
            gillscolourdict['qstr'] = '__icontains'
            gillscolourdict['model'] = apps.get_model(app_label='fungi', model_name=gillscolourdict['table'])
            gillscolour_list = gillscolourdict['model'].objects.filter(Q(**{gillscolourdict['column'] + gillscolourdict['qstr']: gillscolourdict['searchterm']}))
            for gc in gillscolour_list:
                resultslist.append(gc.Fungi_id)

        elif i == "GillsBruiseColour":
            gillsbruisecolourdict = {}
            gillsbruisecolourdict['searchterm'] = q_params[i]
            gillsbruisecolourdict['table'] = 'Gills'
            gillsbruisecolourdict['column'] = 'BruiseColour'
            gillsbruisecolourdict['qstr'] = '__icontains'
            gillsbruisecolourdict['model'] = apps.get_model(app_label='fungi', model_name=gillsbruisecolourdict['table'])
            gillsbruisecolour_list = gillsbruisecolourdict['model'].objects.filter(Q(**{gillsbruisecolourdict['column'] + gillsbruisecolourdict['qstr']: gillsbruisecolourdict['searchterm']}))
            for gbc in gillsbruisecolour_list:
                resultslist.append(gbc.Fungi_id)

        elif i == "GillsCutColour":
            gillscutcolourdict = {}
            gillscutcolourdict['searchterm'] = q_params[i]
            gillscutcolourdict['table'] = 'Gills'
            gillscutcolourdict['column'] = 'CutColour'
            gillscutcolourdict['qstr'] = '__icontains'
            gillscutcolourdict['model'] = apps.get_model(app_label='fungi', model_name=gillscutcolourdict['table'])
            gillscutcolour_list = gillscutcolourdict['model'].objects.filter(Q(**{gillscutcolourdict['column'] + gillscutcolourdict['qstr']: gillscutcolourdict['searchterm']}))
            for gcc in gillscutcolour_list:
                resultslist.append(gcc.Fungi_id)

        elif i == "GillsAttachment":
            gillsattachmentdict = {}
            gillsattachmentdict['searchterm'] = q_params[i]
            gillsattachmentdict['table'] = 'Gills'
            gillsattachmentdict['column'] = 'Attachment'
            gillsattachmentdict['qstr'] = '__icontains'
            gillsattachmentdict['model'] = apps.get_model(app_label='fungi', model_name=gillsattachmentdict['table'])
            gillsattachment_list = gillsattachmentdict['model'].objects.filter(Q(**{gillsattachmentdict['column'] + gillsattachmentdict['qstr']: gillsattachmentdict['searchterm']}))
            for ga in gillsattachment_list:
                resultslist.append(ga.Fungi_id)

        elif i == "GillsArrangement":
            gillsarrangementdict = {}
            gillsarrangementdict['searchterm'] = q_params[i]
            gillsarrangementdict['table'] = 'Gills'
            gillsarrangementdict['column'] = 'Arrangement'
            gillsarrangementdict['qstr'] = '__icontains'
            gillsarrangementdict['model'] = apps.get_model(app_label='fungi', model_name=gillsarrangementdict['table'])
            gillsarrangement_list = gillsarrangementdict['model'].objects.filter(Q(**{gillsarrangementdict['column'] + gillsarrangementdict['qstr']: gillsarrangementdict['searchterm']}))
            for ga in gillsarrangement_list:
                resultslist.append(ga.Fungi_id)

        elif i == "GillsMilk":
            gillsmilkdict = {}
            gillsmilkdict['searchterm'] = q_params[i]
            gillsmilkdict['table'] = 'Gills'
            gillsmilkdict['column'] = 'Milk'
            gillsmilkdict['qstr'] = '__icontains'
            gillsmilkdict['model'] = apps.get_model(app_label='fungi', model_name=gillsmilkdict['table'])
            gillsmilk_list = gillsmilkdict['model'].objects.filter(Q(**{gillsmilkdict['column'] + gillsmilkdict['qstr']: gillsmilkdict['searchterm']}))
            for gm in gillsmilk_list:
                resultslist.append(gm.Fungi_id)

        elif i == "FleshCapColour":
            fleshcapcolourdict = {}
            fleshcapcolourdict['searchterm'] = q_params[i]
            fleshcapcolourdict['table'] = 'Flesh'
            fleshcapcolourdict['column'] = 'FleshCapColour'
            fleshcapcolourdict['qstr'] = '__icontains'
            fleshcapcolourdict['model'] = apps.get_model(app_label='fungi', model_name=fleshcapcolourdict['table'])
            fleshcapcolour_list = fleshcapcolourdict['model'].objects.filter(Q(**{fleshcapcolourdict['column'] + fleshcapcolourdict['qstr']: fleshcapcolourdict['searchterm']}))
            for fcc in fleshcapcolour_list:
                resultslist.append(fcc.Fungi_id)

        elif i == "FleshCapBruiseColour":
            fleshcapbruisedolourdict = {}
            fleshcapbruisedolourdict['searchterm'] = q_params[i]
            fleshcapbruisedolourdict['table'] = 'Flesh'
            fleshcapbruisedolourdict['column'] = 'FleshCapBruiseColour'
            fleshcapbruisedolourdict['qstr'] = '__icontains'
            fleshcapbruisedolourdict['model'] = apps.get_model(app_label='fungi', model_name=fleshcapbruisedolourdict['table'])
            fleshcapbruisecolour_list = fleshcapbruisedolourdict['model'].objects.filter(Q(**{fleshcapbruisedolourdict['column'] + fleshcapbruisedolourdict['qstr']: fleshcapbruisedolourdict['searchterm']}))
            for fcbc in fleshcapbruisecolour_list:
                resultslist.append(fcbc.Fungi_id)

        elif i == "FleshCapCutColour":
            fleshcapcutcolourdict = {}
            fleshcapcutcolourdict['searchterm'] = q_params[i]
            fleshcapcutcolourdict['table'] = 'Flesh'
            fleshcapcutcolourdict['column'] = 'FleshCapCutColour'
            fleshcapcutcolourdict['qstr'] = '__icontains'
            fleshcapcutcolourdict['model'] = apps.get_model(app_label='fungi', model_name=fleshcapcutcolourdict['table'])
            fleshcapcutcolour_list = fleshcapcutcolourdict['model'].objects.filter(Q(**{fleshcapcutcolourdict['column'] + fleshcapcutcolourdict['qstr']: fleshcapcutcolourdict['searchterm']}))
            for fccc in fleshcapcutcolour_list:
                resultslist.append(fccc.Fungi_id)

        elif i == "FleshStipeColour":
            fleshstipecolourdict = {}
            fleshstipecolourdict['searchterm'] = q_params[i]
            fleshstipecolourdict['table'] = 'Flesh'
            fleshstipecolourdict['column'] = 'FleshStipeColour'
            fleshstipecolourdict['qstr'] = '__icontains'
            fleshstipecolourdict['model'] = apps.get_model(app_label='fungi', model_name=fleshstipecolourdict['table'])
            fleshstipecolour_list = fleshstipecolourdict['model'].objects.filter(Q(**{fleshstipecolourdict['column'] + fleshstipecolourdict['qstr']: fleshstipecolourdict['searchterm']}))
            for fsc in fleshstipecolour_list:
                resultslist.append(fsc.Fungi_id)

        elif i == "FleshStipeBruiseColour":
            fleshstipebruisecolourdict = {}
            fleshstipebruisecolourdict['searchterm'] = q_params[i]
            fleshstipebruisecolourdict['table'] = 'Flesh'
            fleshstipebruisecolourdict['column'] = 'FleshStipeBruiseColour'
            fleshstipebruisecolourdict['qstr'] = '__icontains'
            fleshstipebruisecolourdict['model'] = apps.get_model(app_label='fungi', model_name=fleshstipebruisecolourdict['table'])
            fleshstipebruisecolour_list = fleshstipebruisecolourdict['model'].objects.filter(Q(**{fleshstipebruisecolourdict['column'] + fleshstipebruisecolourdict['qstr']: fleshstipebruisecolourdict['searchterm']}))
            for fsbc in fleshstipebruisecolour_list:
                resultslist.append(fsbc.Fungi_id)

        elif i == "FleshStipeCutColour":
            fleshstipecutcolourdict = {}
            fleshstipecutcolourdict['searchterm'] = q_params[i]
            fleshstipecutcolourdict['table'] = 'Flesh'
            fleshstipecutcolourdict['column'] = 'FleshStipeCutColour'
            fleshstipecutcolourdict['qstr'] = '__icontains'
            fleshstipecutcolourdict['model'] = apps.get_model(app_label='fungi', model_name=fleshstipecutcolourdict['table'])
            fleshstipecutcolour_list = fleshstipecutcolourdict['model'].objects.filter(Q(**{fleshstipecutcolourdict['column'] + fleshstipecutcolourdict['qstr']: fleshstipecutcolourdict['searchterm']}))
            for fscc in fleshstipecutcolour_list:
                resultslist.append(fscc.Fungi_id)

        elif i == "SporeColour":
            spore_colour_dict = {}
            spore_colour_dict['searchterm'] = q_params[i]
            spore_colour_dict['table'] = 'Spores'
            spore_colour_dict['column'] = 'Colour'
            spore_colour_dict['qstr'] = '__icontains'
            spore_colour_dict['model'] = apps.get_model(app_label='fungi', model_name=spore_colour_dict['table'])
            sporecolour_list = spore_colour_dict['model'].objects.filter(Q(**{spore_colour_dict['column'] + spore_colour_dict['qstr']: spore_colour_dict['searchterm']}))
            for scl in sporecolour_list:
                resultslist.append(scl.Fungi_id)

        elif i == "Kingdom":
            kingdomdict = {}
            kingdomdict['searchterm'] = q_params[i]
            kingdomdict['table'] = 'Classification'
            kingdomdict['column'] = 'Kingdom'
            kingdomdict['qstr'] = '__icontains'
            kingdomdict['model'] = apps.get_model(app_label='fungi', model_name=kingdomdict['table'])
            kingdom_list = kingdomdict['model'].objects.filter(Q(**{kingdomdict['column'] + kingdomdict['qstr']: kingdomdict['searchterm']}))
            for k in kingdom_list:
                resultslist.append(k.Fungi_id)

        elif i == "Phyum":
            phyumdict = {}
            phyumdict['searchterm'] = q_params[i]
            phyumdict['table'] = 'Classification'
            phyumdict['column'] = 'Phyum'
            phyumdict['qstr'] = '__icontains'
            phyumdict['model'] = apps.get_model(app_label='fungi', model_name=phyumdict['table'])
            phyum_list = phyumdict['model'].objects.filter(Q(**{phyumdict['column'] + phyumdict['qstr']: phyumdict['searchterm']}))
            for pl in phyum_list:
                resultslist.append(pl.Fungi_id)

        elif i == "SubPhyum":
            subphyumdict = {}
            subphyumdict['searchterm'] = q_params[i]
            subphyumdict['table'] = 'Classification'
            subphyumdict['column'] = 'SubPhyum'
            subphyumdict['qstr'] = '__icontains'
            subphyumdict['model'] = apps.get_model(app_label='fungi', model_name=subphyumdict['table'])
            subphyum_list = subphyumdict['model'].objects.filter(Q(**{subphyumdict['column'] + subphyumdict['qstr']: subphyumdict['searchterm']}))
            for sp in subphyum_list:
                resultslist.append(sp.Fungi_id)

        elif i == "Class":
            classdict = {}
            classdict['searchterm'] = q_params[i]
            classdict['table'] = 'Classification'
            classdict['column'] = 'Class'
            classdict['qstr'] = '__icontains'
            classdict['model'] = apps.get_model(app_label='fungi', model_name=classdict['table'])
            class_list = classdict['model'].objects.filter(Q(**{classdict['column'] + classdict['qstr']: classdict['searchterm']}))
            for cl in class_list:
                resultslist.append(cl.Fungi_id)

        elif i == "SubClass":
            subclassdict = {}
            subclassdict['searchterm'] = q_params[i]
            subclassdict['table'] = 'Classification'
            subclassdict['column'] = 'SubClass'
            subclassdict['qstr'] = '__icontains'
            subclassdict['model'] = apps.get_model(app_label='fungi', model_name=subclassdict['table'])
            subclass_list = subclassdict['model'].objects.filter(Q(**{subclassdict['column'] + subclassdict['qstr']: subclassdict['searchterm']}))
            for scl in subclass_list:
                resultslist.append(scl.Fungi_id)

        elif i == "Order":
            orderdict = {}
            orderdict['searchterm'] = q_params[i]
            orderdict['table'] = 'Classification'
            orderdict['column'] = 'Order'
            orderdict['qstr'] = '__icontains'
            orderdict['model'] = apps.get_model(app_label='fungi', model_name=orderdict['table'])
            order_list = orderdict['model'].objects.filter(Q(**{orderdict['column'] + orderdict['qstr']: orderdict['searchterm']}))
            for ol in order_list:
                resultslist.append(ol.Fungi_id)

        elif i == "Family":
            familydict = {}
            familydict['searchterm'] = q_params[i]
            familydict['table'] = 'Classification'
            familydict['column'] = 'Family'
            familydict['qstr'] = '__icontains'
            familydict['model'] = apps.get_model(app_label='fungi', model_name=familydict['table'])
            family_list = familydict['model'].objects.filter(Q(**{familydict['column'] + familydict['qstr']: familydict['searchterm']}))
            for fl in family_list:
                resultslist.append(fl.Fungi_id)

        elif i == "Genus":
            genusdict = {}
            genusdict['searchterm'] = q_params[i]
            genusdict['table'] = 'Classification'
            genusdict['column'] = 'Genus'
            genusdict['qstr'] = '__icontains'
            genusdict['model'] = apps.get_model(app_label='fungi', model_name=genusdict['table'])
            genus_list = genusdict['model'].objects.filter(Q(**{genusdict['column'] + genusdict['qstr']: genusdict['searchterm']}))
            for gl in genus_list:
                resultslist.append(gl.Fungi_id)


        elif i == "PoisonType":
            poisontypedict = {}
            poisontypedict['searchterm'] = q_params[i]
            poisontypedict['table'] = 'Cuisine'
            poisontypedict['column'] = 'PoisonType'
            poisontypedict['qstr'] = '__icontains'
            poisontypedict['model'] = apps.get_model(app_label='fungi', model_name=poisontypedict['table'])
            poisontype_list = poisontypedict['model'].objects.filter(Q(**{poisontypedict['column'] + poisontypedict['qstr']: poisontypedict['searchterm']}))
            for pt in poisontype_list:
                resultslist.append(pt.Fungi_id)

        elif i == "CulinaryRating":
            culinaryratingdict = {}
            culinaryratingdict['searchterm'] = q_params[i]
            culinaryratingdict['table'] = 'Cuisine'
            culinaryratingdict['column'] = 'CulinaryRating'
            culinaryratingdict['qstr'] = '__icontains'
            culinaryratingdict['model'] = apps.get_model(app_label='fungi', model_name=culinaryratingdict['table'])
            culinaryrating_list = culinaryratingdict['model'].objects.filter(Q(**{culinaryratingdict['column'] + culinaryratingdict['qstr']: culinaryratingdict['searchterm']}))
            for cr in culinaryrating_list:
                resultslist.append(cr.Fungi_id)

        elif i == "Odour":
            odourdict = {}
            odourdict['searchterm'] = q_params[i]
            odourdict['table'] = 'Cuisine'
            odourdict['column'] = 'Odour'
            odourdict['qstr'] = '__icontains'
            odourdict['model'] = apps.get_model(app_label='fungi', model_name=odourdict['table'])
            odour_list = odourdict['model'].objects.filter(Q(**{odourdict['column'] + odourdict['qstr']: odourdict['searchterm']}))
            for odl in odour_list:
                resultslist.append(odl.Fungi_id)

        elif i == "Taste":
            tastedict = {}
            tastedict['searchterm'] = q_params[i]
            tastedict['table'] = 'Cuisine'
            tastedict['column'] = 'Taste'
            tastedict['qstr'] = '__icontains'
            tastedict['model'] = apps.get_model(app_label='fungi', model_name=tastedict['table'])
            taste_list = tastedict['model'].objects.filter(Q(**{tastedict['column'] + tastedict['qstr']: tastedict['searchterm']}))
            for tl in taste_list:
                resultslist.append(tl.Fungi_id)

        elif i == "StatusStatusData":
            statusdatadict = {}
            statusdatadict['searchterm'] = q_params[i]
            statusdatadict['table'] = 'Status'
            statusdatadict['column'] = 'StatusData'
            statusdatadict['qstr'] = '__icontains'
            statusdatadict['model'] = apps.get_model(app_label='fungi', model_name=statusdatadict['table'])
            statusdata_list = statusdatadict['model'].objects.filter(Q(**{statusdatadict['column'] + statusdatadict['qstr']: statusdatadict['searchterm']}))
            for sdl in statusdata_list:
                resultslist.append(sdl.Fungi_id)

        elif i == "StatusWhereFound":
            statuswherefounddict = {}
            statuswherefounddict['searchterm'] = q_params[i]
            statuswherefounddict['table'] = 'Status'
            statuswherefounddict['column'] = 'WhereFound'
            statuswherefounddict['qstr'] = '__icontains'
            statuswherefounddict['model'] = apps.get_model(app_label='fungi', model_name=statuswherefounddict['table'])
            statuswherefound_list = statuswherefounddict['model'].objects.filter(Q(**{statuswherefounddict['column'] + statuswherefounddict['qstr']: statuswherefounddict['searchterm']}))
            for swf in statuswherefound_list:
                resultslist.append(swf.Fungi_id)

        # remove duplicate fungi from Results list
        for rs_item in resultslist:
            if rs_item not in resultslist2:
                resultslist2.append(rs_item)

        for sl_item in synonymlist:
            if sl_item not in synonymlist2:
                synonymlist2.append(sl_item)

        for cn_item in commonnameslist:
            if cn_item not in commonnameslist2:
                commonnameslist2.append(cn_item)

        # resultslist = []
        resultslist = resultslist2
        synonymlist = synonymlist2
        commonnameslist = commonnameslist2

        fid = collections.Counter(resultslist)
        print('FiD = ', fid)

        for match, count in sorted(fid.items()):
            if count == searchterms_count:
                m = Fungi.objects.get(id=match)
                matches.append(m)

        matches.sort(key=lambda c: c.LatinName, reverse=False)

    return matches, synonymlist, commonnameslist
