from django.views.generic import DetailView
from usersettings.models import Show
from fungi.models import *
from django.contrib.auth.models import User  # AnonymousUser
from fungi.views.insertglossarylinks import insertglossarylinks
from fungi.views.insertfunginamelinks import insertfunginamelinks
from django.db.models import Q


class FungiDetail(DetailView):
    model = Fungi
    template_name = 'fungi_detail.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(FungiDetail, self).get_context_data(**kwargs)
        currentfungi = context['fungi']

        def data_present(fungi_attribute):
            dp = 'True'
            context_var = [f for f in fungi_attribute._meta.get_fields() if f.name not in ['id', 'DataPresent', 'Fungi', 'slug']]
            for c in context_var:
                field_value = getattr(fungi_attribute, c.name, None)
                if field_value is None:
                    field_value = 'NoData'
                if field_value == 'NoData' or field_value == 0.00 or field_value == 'no comments' or field_value == 'NoData' or field_value == 0 or field_value == '0':
                    dp = False
                else:
                    dp = 'True'
                    break
            return dp

        # retrieving user id's to get filter preferences
        if self.request.user.is_authenticated:
            currentuser = self.request.user
            # uid = request.user
            print('uid-0', currentuser)
            usershowsettings = Show.objects.get(user_id=currentuser.id)
        else:
            currentuser = User.objects.get(username='GuestUser')
            print('uid-1', currentuser)
            usershowsettings = Show.objects.get(user_id=currentuser.id)

        # LINKS
        retrievedobjects = NetLinks.objects.filter(Fungi_id=self.object).distinct().order_by('OrderToDisplay')
        if retrievedobjects:
            context['NetLinks'] = retrievedobjects

        # PERSONAL NOTES
        pid = FungiNotes.objects.filter(Fungi_id=self.object).first()
        currentuser = self.request.user
        print('currentuser = ', currentuser.username)
        print('currentuser = ', currentuser.id)

        if pid is not None and usershowsettings.ShowFungiNotes:
            print('AAAA')
            if self.request.user.is_superuser:
                print('BBBB')
                retrievedobjects = FungiNotes.objects.filter(Fungi_id=self.object, )
                #'print('retrievedobjects-A1 = ', retrievedobjects)
                countera = 1
                for count in retrievedobjects:
                    count.NoteCount = countera
                    countera += 1
                #print('retrievedobjects-A2= ', retrievedobjects)
            else:
                print('CCCC')
                retrievedobjects = FungiNotes.objects.filter(Q(NoteUser=currentuser.id) & Q(Fungi_id=self.object.id))
                #print('retrievedobjects-B1a = ', retrievedobjects)
                # retrievedobjects = FungiNotes.objects.filter(NoteUser=currentuser.id)
                # print('retrievedobjects-B1b = ', retrievedobjects)
                counterb = 1
                for count in retrievedobjects:
                    count.NoteCount = counterb
                    counterb += 1
                #print('retrievedobjects-B2 = ', retrievedobjects)

            if retrievedobjects:
                context['FungiNotesFlag'] = 'Yes'
                context['data_to_display'] = True
                context['Notes'] = retrievedobjects

        # PICTURES
        retrievedobjects = Picture.objects.get(Fungi_id=self.object)
        context['Picture'] = retrievedobjects

        # HABITAT
        habitat_sources_list = []
        pid = Habitat.objects.get(Fungi_id=self.object)
        if data_present(pid):
            # data_to_display = False
            context['ShowHabitatFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowHabitat:
                retrievedobjects = Habitat.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    #print('self.object', self.object)
                    #print('self.DetailSources.objects', i.Detail)
                    if i.Detail == "Habitat":
                        habitat_sources_list.append(i.Source)
                        #print('self.object', self.object)
                        #print('self.DetailSources.objects', i.Detail)
                    #print('Habitat_sources', habitat_sources_list)
                context['Habitat_Sources_List'] = habitat_sources_list

                if retrievedobjects.Associations == 'NoData':
                    context['Associations'] = retrievedobjects.Associations
                else:
                    context['Associations'] = insertglossarylinks(retrievedobjects.Associations)[0]
                    context['AssociationsLinks'] = insertglossarylinks(retrievedobjects.Associations)[1]

                if retrievedobjects.Ph == 'NoData':
                    context['Ph'] = retrievedobjects.Ph
                else:
                    context['Ph'] = insertglossarylinks(retrievedobjects.Ph)[0]
                    context['PhLinks'] = insertglossarylinks(retrievedobjects.Ph)[1]

                context['Ph'] = retrievedobjects.Ph

                if retrievedobjects.Soil == 'NoData':
                    context['Soil'] = retrievedobjects.Soil
                else:
                    context['Soil'] = insertglossarylinks(retrievedobjects.Soil)[0]
                    context['SoilLinks'] = insertglossarylinks(retrievedobjects.Soil)[1]

                if retrievedobjects.Substrate == 'NoData':
                    context['Substrate'] = retrievedobjects.Substrate
                else:
                    context['Substrate'] = insertglossarylinks(retrievedobjects.Substrate)[0]
                    context['SubstrateLinks'] = insertglossarylinks(retrievedobjects.Substrate)[1]

                if retrievedobjects.Environment == 'NoData':
                    context['Environment'] = retrievedobjects.Environment
                else:
                    context['Environment'] = insertglossarylinks(retrievedobjects.Environment)[0]
                    context['EnvironmentLinks'] = insertglossarylinks(retrievedobjects.Environment)[1]

                if retrievedobjects.Comments == 'no comments':
                    context['HabitatComments'] = retrievedobjects.Comments
                else:
                    context['HabitatComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                    context['HabitatCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowHabitatFlag'] = 'Yes'
                context['data_to_display'] = True
            else:
                context['ShowHabitatFlag'] = 'No'

            # print('context....Associations::::',  context['Associations'])

        # FUNGI COMMENTS
        fungicommentssourceslist = []
        pid = FungiComments.objects.get(Fungi_id=self.object)
        if data_present(pid):
            context['FungiCommentsFlag'] = 'Yes'
            if usershowsettings.ShowFungiComments:
                retrievedobjects = FungiComments.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Comments":
                        fungicommentssourceslist.append(i.Source)
                context['FungiCommentsSourcesList'] = fungicommentssourceslist

                if retrievedobjects.Comments == 'no comments':
                    context['FungiComments'] = retrievedobjects.Comments
                else:
                    context['FungiComments'] = insertfunginamelinks(retrievedobjects.Comments)[0]
                    # print('TEST', insertfunginamelinks(retrievedobjects.Comments)[0] )
                    context['FungiCommentsLinks'] = insertfunginamelinks(retrievedobjects.Comments)[1]

                    # print('FungiComments', context['FungiComments'])
                    # print('FungiCommentsLinks', context['FungiCommentsLinks'])

                context['FungiCommentsFlag'] = 'Yes'
                context['data_to_display'] = True
            else:
                context['FungiCommentsFlag'] = 'No'
        else:
            context['FungiCommentsFlag'] = 'No'

        # DETAILSOURCES
        pid = DetailSources.objects.filter(Fungi_id=self.object).first()
        # If DetailSources have all been deleted need default 'NoData' record in DB
        if pid is None:
            DetailSources.objects.create(Fungi=currentfungi)
            pid = DetailSources.objects.filter(Fungi_id=self.object).first()

        if data_present(pid):
            context['DetailSourcesFlag'] = 'Yes'
            if usershowsettings.DetailSources:
                retrievedobjects = DetailSources.objects.filter(Fungi_id=self.object)
                context['refcount'] = retrievedobjects.count
                context['DetailSourcesFlag'] = 'Yes'
                context['data_to_display'] = 'True'
            else:
                context['DetailSourcesFlag'] = 'No'
        else:
            context['DetailSourcesFlag'] = 'No'

        # COMMONNAMES
        othercommonnamessourceslist = []
        pid = OtherCommonNames.objects.filter(Fungi_id=self.object).first()
        # If Common Names have all been deleted need default 'NoData' record in DB
        if pid is None:
            print('pid == None:')
            OtherCommonNames.objects.create(Fungi=currentfungi)
            pid = OtherCommonNames.objects.filter(Fungi_id=self.object).first()

        # print('pid, OtherCommonNames: ', pid)
        if data_present(pid):
            context['ShowCommonNameFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowOtherCommonNames:
                retrievedobjects = OtherCommonNames.objects.filter(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "OtherCommonNames":
                        othercommonnamessourceslist.append(i.Source)
                context['OtherCommonNamesSourcesList'] = othercommonnamessourceslist
                # print('OtherCommonNames, retrievedobjects', retrievedobjects)
                if retrievedobjects:
                    context['OtherCommonNames'] = retrievedobjects
                    context['ShowCommonNameFlag'] = 'Yes'
                else:
                    context['ShowCommonNameFlag'] = 'No'
        else:
            context['ShowCommonNameFlag'] = 'No'

        # GROUP
        grouplist = []
        pid = Fungi.objects.order_by('Group').values('Group').distinct()
        for i in pid:
            # print('i',i['Group'])
            grouplist.append(i['Group'])

        # SIMILARTO
        similarfungisourceslist = []
        pid = SimilarFungi.objects.filter(Fungi_id=self.object).first()
        # If Similar Fungi have all been deleted need default 'NoData' record in DB
        if pid is None:
            pid = SimilarFungi(Fungi_id=currentfungi.id, slug=currentfungi.id, SFid=0, SimilarFungiName='NoData')
            pid.save()
            # print('pid2 =', pid)
        if data_present(pid):
            context['ShowSimilarFungiFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowSimilarFungi:
                retrievedobjects = SimilarFungi.objects.filter(Fungi_id=self.object).distinct()
                # print('SimilarFungi: retrievedobjects',retrievedobjects)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "SimilarFungi":
                        similarfungisourceslist.append(i.Source)
                        # print('i.Source', i.Source)
                        # print('i.Source-iii', i)
                context['SimilarFungiSourcesList'] = similarfungisourceslist
                # print('LatinSynonymsSourcesList-9999', similarfungisourceslist)
                context['SimilarFungiNames'] = retrievedobjects
                # print('retrievedobjects-9999', retrievedobjects)
                context['ShowSimilarFungiFlag'] = 'Yes'
            else:
                context['ShowSimilarFungiFlag'] = 'No'
        else:
            context['ShowSimilarFungiFlag'] = 'No'

        # LATIN SYNONYMS
        latinsynonymssourceslist = []
        pid = LatinSynonyms.objects.filter(Fungi_id=self.object).first()
        # If Latin Synonyms have all been deleted need default 'NoData' record in DB
        if pid is None:
            LatinSynonyms.objects.create(Fungi=currentfungi)
            pid = LatinSynonyms.objects.filter(Fungi_id=self.object).first()

        if data_present(pid):
            context['ShowLatinSynonymsFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowLatinSynonyms:
                retrievedobjects = LatinSynonyms.objects.filter(Fungi_id=self.object).distinct()
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "LatinSynonyms":
                        latinsynonymssourceslist.append(i.Source)
                context['LatinSynonymsSourcesList'] = latinsynonymssourceslist
                context['LatinSynonyms'] = retrievedobjects
                context['ShowLatinSynonymsFlag'] = 'Yes'
            else:
                context['ShowLatinSynonymsFlag'] = 'No'
        else:
            context['ShowLatinSynonymsFlag'] = 'No'

        # CLASSIFICATION
        classificationsourceslist = []
        pid = Classification.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(Classification.objects.get(Fungi_id= self.object)):
            context['ShowClassificationFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowClassification:
                retrievedobjects = Classification.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Classification":
                        classificationsourceslist.append(i.Source)
                context['ClassificationSourcesList'] = classificationsourceslist
                # print('ClassificationSourcesList-9999', ClassificationSourcesList)
                context['Kingdom'] = retrievedobjects.Kingdom
                context['Phyum'] = retrievedobjects.Phyum
                context['SubPhyum'] = retrievedobjects.SubPhyum
                context['Class'] = retrievedobjects.Class
                context['SubClass'] = retrievedobjects.SubClass
                context['Order'] = retrievedobjects.Order
                context['Family'] = retrievedobjects.Family
                context['Genus'] = retrievedobjects.Genus

                context['ShowClassificationFlag'] = 'Yes'
            else:
                context['ShowClassificationFlag'] = 'No'
        else:
            context['ShowClassificationFlag'] = 'No'

        # FRUITINGBODY
        fruitingbodysourceslist = []
        pid = FruitingBody.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            context['ShowFruitingBodyFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowFruitingBody:
                retrievedobjects = FruitingBody.objects.get(Fungi_id=self.object)

                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "FruitingBody":
                        fruitingbodysourceslist.append(i.Source)
                context['FruitingBodySourcesList'] = fruitingbodysourceslist

                if retrievedobjects.Colour is not None:
                    if retrievedobjects.Colour == 'NoData':
                        context['CapColour'] = retrievedobjects.Colour
                    else:
                        context['CapColour'] = insertglossarylinks(retrievedobjects.Colour)[0]
                        context['CapColourLinks'] = insertglossarylinks(retrievedobjects.Colour)[1]

                if retrievedobjects.Shape is not None:
                    if retrievedobjects.Shape == 'NoData':
                        context['CapShape'] = retrievedobjects.Shape
                    else:
                        context['CapShape'] = insertglossarylinks(retrievedobjects.Shape)[0]
                        context['CapShapeLinks'] = insertglossarylinks(retrievedobjects.Shape)[1]

                if retrievedobjects.Rim is not None:
                    if retrievedobjects.Rim == 'NoData':
                        context['CapRim'] = retrievedobjects.Rim
                    else:
                        context['CapRim'] = insertglossarylinks(retrievedobjects.Rim)[0]
                        context['CapRimLinks'] = insertglossarylinks(retrievedobjects.Rim)[1]

                if retrievedobjects.CapTexture is not None:
                    if retrievedobjects.CapTexture == 'NoData':
                        context['CapTexture'] = retrievedobjects.CapTexture
                    else:
                        context['CapTexture'] = insertglossarylinks(retrievedobjects.CapTexture)[0]
                        context['CapTextureLinks'] = insertglossarylinks(retrievedobjects.CapTexture)[1]

                if retrievedobjects.BruiseColour is not None:
                    if retrievedobjects.BruiseColour == 'NoData':
                        context['CapBruiseColour'] = retrievedobjects.BruiseColour
                    else:
                        context['CapBruiseColour'] = insertglossarylinks(retrievedobjects.BruiseColour)[0]
                        context['CapBruiseColourLinks'] = insertglossarylinks(retrievedobjects.BruiseColour)[1]

                if retrievedobjects.CutColour is not None:
                    if retrievedobjects.CutColour == 'NoData':
                        context['CapCutColour'] = retrievedobjects.CutColour
                    else:
                        context['CapCutColour'] = insertglossarylinks(retrievedobjects.CutColour)[0]
                        context['CapCutColourLinks'] = insertglossarylinks(retrievedobjects.CutColour)[1]

                if float(retrievedobjects.WidthMin) > 0.00 and float(retrievedobjects.WidthMax) > 0.00:
                    context['CapWidthMin'] = float(retrievedobjects.WidthMin)
                    context['CapWidthMax'] = float(retrievedobjects.WidthMax)
                if float(retrievedobjects.WidthMin) == 0.00 and float(retrievedobjects.WidthMax) == 0.00:
                    context['CapWidthMin'] = float(retrievedobjects.WidthMin)
                    context['CapWidthMax'] = float(retrievedobjects.WidthMax)
                if float(retrievedobjects.WidthMin) == 0.00 and float(retrievedobjects.WidthMax) > 0.00:
                    context['CapWidthMin'] = "up to"
                    context['CapWidthMax'] = float(retrievedobjects.WidthMax)

                if retrievedobjects.Comments is not None:
                    if retrievedobjects.Comments == 'no comments':
                        context['CapComments'] = retrievedobjects.Comments
                    else:
                        context['CapComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                        context['CapCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowFruitingBodyFlag'] = 'Yes'
            else:
                context['ShowFruitingBodyFlag'] = 'No'
        else:
            context['ShowFruitingBodyFlag'] = 'No'

        # STIPE
        stipesourceslist = []
        pid = Stipe.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(Stipe.objects.get(Fungi_id= self.object)):
            context['ShowStipeFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowStipe:
                retrievedobjects = Stipe.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Stipe":
                        stipesourceslist.append(i.Source)
                context['StipeSourcesList'] = stipesourceslist
                # print('StipeSourcesList-9999', StipeSourcesList)
                # print('Stipe, retrievedobjects', retrievedobjects)

                if retrievedobjects.Colour is not None:
                    if retrievedobjects.Colour == 'NoData':
                        context['StipeColour'] = retrievedobjects.Colour
                    else:
                        context['StipeColour'] = insertglossarylinks(retrievedobjects.Colour)[0]
                        context['StipeColourLinks'] = insertglossarylinks(retrievedobjects.Colour)[1]

                if retrievedobjects.Texture is not None:
                    if retrievedobjects.Texture == 'NoData':
                        context['StipeTexture'] = retrievedobjects.Texture
                    else:
                        context['StipeTexture'] = insertglossarylinks(retrievedobjects.Texture)[0]
                        context['StipeTextureLinks'] = insertglossarylinks(retrievedobjects.Texture)[1]

                if retrievedobjects.BruiseColour is not None:
                    if retrievedobjects.BruiseColour == 'NoData':
                        context['StipeBruiseColour'] = retrievedobjects.BruiseColour
                    else:
                        context['StipeBruiseColour'] = insertglossarylinks(retrievedobjects.BruiseColour)[0]
                        context['StipeBruiseColourLinks'] = insertglossarylinks(retrievedobjects.BruiseColour)[1]

                if retrievedobjects.BruiseColour is not None:
                    if retrievedobjects.CutColour == 'NoData':
                        context['StipeCutColour'] = retrievedobjects.CutColour
                    else:
                        context['StipeCutColour'] = insertglossarylinks(retrievedobjects.CutColour)[0]
                        context['StipeCutColourLinks'] = insertglossarylinks(retrievedobjects.CutColour)[1]

                if float(retrievedobjects.ThicknessMin) > 0.00 and float(retrievedobjects.ThicknessMax) > 0.00:
                    context['StipeThicknessMin'] = float(retrievedobjects.ThicknessMin)
                    context['StipeThicknessMax'] = float(retrievedobjects.ThicknessMax)
                if float(retrievedobjects.ThicknessMin) == 0.00 and float(retrievedobjects.ThicknessMax) > 0.00:
                    context['StipeThicknessMin'] = "up to"
                    context['StipeThicknessMax'] = float(retrievedobjects.ThicknessMax)
                if float(retrievedobjects.ThicknessMin) == 0.00 and float(retrievedobjects.ThicknessMax) == 0.00:
                    context['StipeThicknessMin'] = float(retrievedobjects.ThicknessMin)
                    context['StipeThicknessMax'] = float(retrievedobjects.ThicknessMax)

                if retrievedobjects.LengthMin > 0.00 and retrievedobjects.LengthMax > 0.00:
                    context['StipeLengthMin'] = round(retrievedobjects.LengthMin, 2)
                    context['StipeLengthMax'] = round(retrievedobjects.LengthMax, 2)
                if retrievedobjects.LengthMin == 0.00 and retrievedobjects.LengthMax == 0.00:
                    context['StipeLengthMin'] = round(retrievedobjects.LengthMin, 2)
                    context['StipeLengthMax'] = round(retrievedobjects.LengthMax, 2)
                if retrievedobjects.LengthMin == 0.00 and retrievedobjects.LengthMax > 0.00:
                    context['StipeLengthMin'] = "up to"
                    context['StipeLengthMax'] = float(retrievedobjects.LengthMax)

                if retrievedobjects.Shape is not None:
                    if retrievedobjects.Shape == 'NoData':
                        context['Shape'] = retrievedobjects.Shape
                    else:
                        context['Shape'] = insertglossarylinks(retrievedobjects.Shape)[0]
                        context['ShapeLinks'] = insertglossarylinks(retrievedobjects.Shape)[1]

                if retrievedobjects.Ring is not None:
                    if retrievedobjects.Ring == 'NoData':
                        context['StipeRing'] = retrievedobjects.Ring
                    else:
                        context['StipeRing'] = insertglossarylinks(retrievedobjects.Ring)[0]
                        context['StipeRingLinks'] = insertglossarylinks(retrievedobjects.Ring)[1]

                if retrievedobjects.RingDescription is not None:
                    if retrievedobjects.RingDescription == 'NoData':
                        context['RingDescription'] = retrievedobjects.RingDescription
                    else:
                        context['RingDescription'] = insertglossarylinks(retrievedobjects.RingDescription)[0]
                        context['RingDescriptionLinks'] = insertglossarylinks(retrievedobjects.RingDescription)[1]

                if retrievedobjects.ReticulationPresent is not None:
                    if retrievedobjects.ReticulationPresent == 'NoData':
                        context['ReticulationPresent'] = retrievedobjects.ReticulationPresent
                    else:
                        context['ReticulationPresent'] = insertglossarylinks(retrievedobjects.ReticulationPresent)[0]
                        context['ReticulationPresentLinks'] = insertglossarylinks(retrievedobjects.ReticulationPresent)[1]

                if retrievedobjects.Reticulation is not None:
                    if retrievedobjects.Reticulation == 'NoData':
                        context['Reticulation'] = retrievedobjects.Reticulation
                    else:
                        context['Reticulation'] = insertglossarylinks(retrievedobjects.Reticulation)[0]
                        context['ReticulationLinks'] = insertglossarylinks(retrievedobjects.Reticulation)[1]

                if retrievedobjects.Base is not None:
                    if retrievedobjects.Base == 'NoData':
                        context['Base'] = retrievedobjects.Base
                    else:
                        context['Base'] = insertglossarylinks(retrievedobjects.Base)[0]
                        context['BaseLinks'] = insertglossarylinks(retrievedobjects.Base)[1]

                if retrievedobjects.Volva is not None:
                    if retrievedobjects.Volva == 'NoData':
                        context['Volva'] = retrievedobjects.Volva
                    else:
                        context['Volva'] = insertglossarylinks(retrievedobjects.Volva)[0]
                        context['VolvaLinks'] = insertglossarylinks(retrievedobjects.Volva)[1]

                if retrievedobjects.Comments is not None:
                    if retrievedobjects.Comments == 'no comments':
                        context['StipeComments'] = retrievedobjects.Comments
                    else:
                        context['StipeComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                        context['StipeCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowStipeFlag'] = 'Yes'
            else:
                context['ShowStipeFlag'] = 'No'
        else:
            context['ShowStipeFlag'] = 'No'

        # PORES
        poresandtubessourceslist = []
        pid = PoresAndTubes.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(PoresAndTubes.objects.get(Fungi_id= self.object)):
            context['ShowPoresAndTubesFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowPoresAndTubes:
                retrievedobjects = PoresAndTubes.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "PoresAndTubes":
                        poresandtubessourceslist.append(i.Source)
                context['PoresAndTubesSourcesList'] = poresandtubessourceslist
                # print('PoresAndTubesSourcesList-9999', PoresAndTubesSourcesList)
                context['PoresPresent'] = retrievedobjects.PoresPresent

                if retrievedobjects.PoreColour == 'NoData':
                    context['PoreColour'] = retrievedobjects.PoreColour
                else:
                    context['PoreColour'] = insertglossarylinks(retrievedobjects.PoreColour)[0]
                    context['PoreColourLinks'] = insertglossarylinks(retrievedobjects.PoreColour)[1]

                if retrievedobjects.PoreShape == 'NoData':
                    context['PoreShape'] = retrievedobjects.PoreShape
                else:
                    context['PoreShape'] = insertglossarylinks(retrievedobjects.PoreShape)[0]
                    context['PoreShapeLinks'] = insertglossarylinks(retrievedobjects.PoreShape)[1]

                if retrievedobjects.PoreBruiseColour == 'NoData':
                    context['PoreBruiseColour'] = retrievedobjects.PoreBruiseColour
                else:
                    context['PoreBruiseColour'] = insertglossarylinks(retrievedobjects.PoreBruiseColour)[0]
                    context['PoreBruiseColourLinks'] = insertglossarylinks(retrievedobjects.PoreBruiseColour)[1]

                if retrievedobjects.TubeColour == 'NoData':
                    context['TubeColour'] = retrievedobjects.TubeColour
                else:
                    context['TubeColour'] = insertglossarylinks(retrievedobjects.TubeColour)[0]
                    context['TubeColourLinks'] = insertglossarylinks(retrievedobjects.TubeColour)[1]

                if retrievedobjects.TubeShape == 'NoData':
                    context['TubeShape'] = retrievedobjects.TubeShape
                else:
                    context['TubeShape'] = insertglossarylinks(retrievedobjects.TubeShape)[0]
                    context['TubeShapeLinks'] = insertglossarylinks(retrievedobjects.TubeShape)[1]

                if retrievedobjects.TubeBruiseColour == 'NoData':
                    context['TubeBruiseColour'] = retrievedobjects.TubeBruiseColour
                else:
                    context['TubeBruiseColour'] = insertglossarylinks(retrievedobjects.TubeBruiseColour)[0]
                    context['TubeBruiseColourLinks'] = insertglossarylinks(retrievedobjects.TubeBruiseColour)[1]

                context['PoreMilk'] = retrievedobjects.Milk

                if retrievedobjects.Comments == 'no comments':
                    context['PoreComments'] = retrievedobjects.Comments
                else:
                    context['PoreComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                    context['PoreCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowPoresAndTubesFlag'] = 'Yes'
            else:
                context['ShowPoresAndTubesFlag'] = 'No'
        else:
            context['ShowPoresAndTubesFlag'] = 'No'

        # GILLS
        gillssourceslist = []
        pid = Gills.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(Gills.objects.get(Fungi_id= self.object)):
            context['ShowGillsFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowGills:
                retrievedobjects = Gills.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Gills":
                        gillssourceslist.append(i.Source)
                context['GillsSourcesList'] = gillssourceslist

                if retrievedobjects.Colour == 'NoData':
                    context['GillsColour'] = retrievedobjects.Colour
                else:
                    context['GillsColour'] = insertglossarylinks(retrievedobjects.Colour)[0]
                    context['GillsColourLinks'] = insertglossarylinks(retrievedobjects.Colour)[1]

                context['GillsPresent'] = retrievedobjects.GillsPresent

                if retrievedobjects.BruiseColour == 'NoData':
                    context['GillsBruiseColour'] = retrievedobjects.BruiseColour
                else:
                    context['GillsBruiseColour'] = insertglossarylinks(retrievedobjects.BruiseColour)[0]
                    context['GillsBruiseColourLinks'] = insertglossarylinks(retrievedobjects.BruiseColour)[1]

                if retrievedobjects.CutColour == 'NoData':
                    context['GillsCutColour'] = retrievedobjects.CutColour
                else:
                    context['GillsCutColour'] = insertglossarylinks(retrievedobjects.CutColour)[0]
                    context['GillsCutColourLinks'] = insertglossarylinks(retrievedobjects.CutColour)[1]

                if retrievedobjects.Attachment == 'NoData':
                    context['GillsAttachment'] = retrievedobjects.Attachment
                else:
                    context['GillsAttachment'] = insertglossarylinks(retrievedobjects.Attachment)[0]
                    context['GillsAttachmentLinks'] = insertglossarylinks(retrievedobjects.Attachment)[1]

                if retrievedobjects.Arrangement == 'NoData':
                    context['GillsArrangement'] = retrievedobjects.Arrangement
                else:
                    context['GillsArrangement'] = insertglossarylinks(retrievedobjects.Arrangement)[0]
                    context['GillsArrangementLinks'] = insertglossarylinks(retrievedobjects.Arrangement)[1]

                context['GillsMilk'] = retrievedobjects.Milk

                if retrievedobjects.Comments == 'no comments':
                    context['GillsComments'] = retrievedobjects.Comments
                else:
                    context['GillsComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                    context['GillsCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowGillsFlag'] = 'Yes'
            else:
                context['ShowGillsFlag'] = 'No'
        else:
            context['ShowGillsFlag'] = 'No'

        # SPORES
        sporessourceslist = []
        pid = Spores.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(Spores.objects.get(Fungi_id= self.object)):
            context['ShowSporesFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowSpores:
                retrievedobjects = Spores.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Spores":
                        sporessourceslist.append(i.Source)
                context['SporesSourcesList'] = sporessourceslist
                # print('SporesSourcesList-9999', SporesSourcesList)

                if retrievedobjects.Colour == 'NoData':
                    context['SporesColour'] = retrievedobjects.Colour
                else:
                    context['SporesColour'] = insertglossarylinks(retrievedobjects.Colour)[0]
                    context['SporesColourLinks'] = insertglossarylinks(retrievedobjects.Colour)[1]

                if retrievedobjects.Comments == 'no comments':
                    context['SporesComments'] = retrievedobjects.Comments
                else:
                    context['SporesComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                    context['SporesCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowSporesFlag'] = 'Yes'
            else:
                context['ShowSporesFlag'] = 'No'
        else:
            context['ShowSporesFlag'] = 'No'

        # FLESH
        fleshsourceslist = []
        pid = Flesh.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(Flesh.objects.get(Fungi_id= self.object)):
            context['ShowFleshFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowFlesh:
                retrievedobjects = Flesh.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Flesh":
                        fleshsourceslist.append(i.Source)
                        # print('SOURCE',i.Source)
                context['FleshSourcesList'] = fleshsourceslist

                if retrievedobjects.FleshCapColour == 'NoData':
                    context['FleshCapColour'] = retrievedobjects.FleshCapColour
                else:
                    context['FleshCapColour'] = insertglossarylinks(retrievedobjects.FleshCapColour)[0]
                    context['FleshCapColourLinks'] = insertglossarylinks(retrievedobjects.FleshCapColour)[1]

                if retrievedobjects.FleshCapBruiseColour == 'NoData':
                    context['FleshCapBruiseColour'] = retrievedobjects.FleshCapBruiseColour
                else:
                    context['FleshCapBruiseColour'] = insertglossarylinks(retrievedobjects.FleshCapBruiseColour)[0]
                    context['FleshCapBruiseColourLinks'] = insertglossarylinks(retrievedobjects.FleshCapBruiseColour)[1]

                if retrievedobjects.FleshCapCutColour == 'NoData':
                    context['FleshCapCutColour'] = retrievedobjects.FleshCapCutColour
                else:
                    context['FleshCapCutColour'] = insertglossarylinks(retrievedobjects.FleshCapCutColour)[0]
                    context['FleshCapCutColourLinks'] = insertglossarylinks(retrievedobjects.FleshCapCutColour)[1]

                if retrievedobjects.FleshStipeColour == 'NoData':
                    context['FleshStipeColour'] = retrievedobjects.FleshStipeColour
                else:
                    context['FleshStipeColour'] = insertglossarylinks(retrievedobjects.FleshStipeColour)[0]
                    context['FleshStipeColourLinks'] = insertglossarylinks(retrievedobjects.FleshStipeColour)[1]

                if retrievedobjects.FleshStipeBruiseColour == 'NoData':
                    context['FleshStipeBruiseColour'] = retrievedobjects.FleshStipeBruiseColour
                else:
                    context['FleshStipeBruiseColour'] = insertglossarylinks(retrievedobjects.FleshStipeBruiseColour)[0]
                    context['FleshStipeBruiseColourLinks'] = insertglossarylinks(retrievedobjects.FleshStipeBruiseColour)[1]

                if retrievedobjects.FleshStipeCutColour == 'NoData':
                    context['FleshStipeCutColour'] = retrievedobjects.FleshStipeCutColour
                else:
                    context['FleshStipeCutColour'] = insertglossarylinks(retrievedobjects.FleshStipeCutColour)[0]
                    context['FleshStipeCutColourLinks'] = insertglossarylinks(retrievedobjects.FleshStipeCutColour)[1]

                if retrievedobjects.Comments == 'no comments':
                    context['FleshComments'] = retrievedobjects.Comments
                else:
                    context['FleshComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                    context['FleshCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]

                context['ShowFleshFlag'] = 'Yes'
            else:
                context['ShowFleshFlag'] = 'No'
        else:
            context['ShowFleshFlag'] = 'No'

        # STATUS
        statussourceslist = []
        pid = Status.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            # if DataPresent(Status.objects.get(Fungi_id= self.object)):
            context['ShowStatusFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowStatus:
                retrievedobjects = Status.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Status":
                        statussourceslist.append(i.Source)
                context['StatusSourcesList'] = statussourceslist
                context['StatusData'] = retrievedobjects.StatusData
                context['WhereFound'] = retrievedobjects.WhereFound
                context['StatusComments'] = retrievedobjects.StatusComments
                context['ShowStatusFlag'] = 'Yes'

            else:
                context['ShowStatusFlag'] = 'No'
        else:
            context['ShowStatusFlag'] = 'No'

        # SEASON
        seasonssourceslist = []
        pid = Seasons.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            context['ShowSeasonFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowSeasons:
                retrievedobjects = Seasons.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Seasons":
                        seasonssourceslist.append(i.Source)
                context['SeasonsSourcesList'] = seasonssourceslist
                # print('SeasonsSourcesList-9999', SeasonsSourcesList)
                if retrievedobjects.Season != 'NoData' and retrievedobjects.Season != 'All Year':
                    print('SEASON = ', retrievedobjects.Season)
                    from_month = retrievedobjects.Season[0:retrievedobjects.Season.index(',')]
                    to_month = retrievedobjects.Season[(retrievedobjects.Season.rfind(',')) + 1:len(retrievedobjects.Season)]
                    fruitingseason = from_month + ' - ' + to_month
                    context['FruitingSeason'] = fruitingseason
                    context['SeasonComments'] = retrievedobjects.Comments
                    context['ShowSeasonFlag'] = 'Yes'
                elif  retrievedobjects.Season == 'All Year':
                    fruitingseason = 'All Year'
                    context['FruitingSeason'] = fruitingseason
                    context['SeasonComments'] = retrievedobjects.Comments
                    context['ShowSeasonFlag'] = 'Yes'
            else:
                context['ShowSeasonFlag'] = 'No'
        else:
            context['ShowSeasonFlag'] = 'No'

        # CUISINE
        cuisinesourceslist = []
        pid = Cuisine.objects.filter(Fungi_id=self.object).first()
        if data_present(pid):
            context['ShowCuisineFlag'] = 'Yes'
            context['data_to_display'] = True
            if usershowsettings.ShowCuisine:
                retrievedobjects = Cuisine.objects.get(Fungi_id=self.object)
                for i in DetailSources.objects.filter(Fungi_id=self.object):
                    if i.Detail == "Cuisine":
                        cuisinesourceslist.append(i.Source)
                context['CuisineSourcesList'] = cuisinesourceslist
                # print('CuisineSourcesList-9999', CuisineSourcesList)
                # context['FleshComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                context['PoisonType'] = retrievedobjects.PoisonType
                context['CulinaryRating'] = retrievedobjects.CulinaryRating
                context['Odour'] = retrievedobjects.Odour
                context['Taste'] = retrievedobjects.Taste
                context['CuisineComments'] = insertglossarylinks(retrievedobjects.Comments)[0]
                context['CuisineCommentsLinks'] = insertglossarylinks(retrievedobjects.Comments)[1]
                context['ShowCuisineFlag'] = 'Yes'
            else:
                context['ShowCuisineFlag'] = 'No'
        else:
            context['ShowCuisineFlag'] = 'No'

        # print('context....Associations::::', context['Associations'])
        # print('context....Substrate::::', context['Substrate'])
        if currentuser.is_superuser:
            # print('User is superuser')
            context['data_to_display'] = True

        return context
