from fungi.models import Fungi
from django.urls import reverse


def insertfunginamelinks(sectiontext):
    funginames = Fungi.objects.all()
    sorteditemsdict = {}
    fungifoundlist = []
    itemlist = []
    alreadyinlist = []
    alreadyinlisttext = []
    allitems = []
    allitemstext = []
    fungifound = False
    splittext = sectiontext.split()
    fungifound_just_name = []

    for fn in funginames:
        if fn.CommonName in sectiontext:
            ff = Fungi.objects.get(CommonName=fn.CommonName)
            fungifoundlist.append(ff)
            fungifound_just_name.append(fn.CommonName)
            fungifound = True

    # Un-splits fungi names in Split Text, thus ['Death', 'Cap'] becomes ['Death Cap']
    try:
        if fungifound:
            for fungi in fungifoundlist:
                fcn = fungi.CommonName
                if fcn in sectiontext:
                    fcn_split = fcn.split()
                    #print('fcn_split = ', fcn_split)
                    for i in range(len(splittext)):
                        if splittext[i] == fcn_split[0]:
                            splittext[i] = fcn
                    for partname in fcn_split:
                        for SplitTextItem in splittext:
                            if SplitTextItem == partname:
                                splittext.remove(partname)

            # Can't work ou what I was trying to achieve here so have commented out!
            # splittexttemp = splittext
            # for stitem in reversed(splittext):
            #     idx9 = splittext.index(stitem)
            #     if splittexttemp[idx9][0:-1] in splittext[idx9 - 1]:
            #         splittexttemp[idx9] = splittext[idx9][-1]
            # splittext = splittexttemp

    except Exception as e:
        print(fcn + ' ERROR- first loop')

    # Creates list of paths with relevant fungi adding ',' or '.' if in orginal variable: sectiontext
    try:
        for fungi in fungifoundlist:
            fid = fungi.id
            if fungi.CommonName + ',' in sectiontext:
                #print('fungi.CommonName = ', fungi.CommonName)
                commonname = fungi.CommonName + ','
                pathandtext = [reverse('FungiDetail-Page', args=[fid]), commonname]
            elif fungi.CommonName + '.' in sectiontext:
                commonname = fungi.CommonName + '.'
                pathandtext = [reverse('FungiDetail-Page', args=[fid]), commonname]
            else:
                pathandtext = [reverse('FungiDetail-Page', args=[fid]), fungi.CommonName]
            idx = splittext.index(fungi.CommonName)
            sublist = [idx, pathandtext]
            itemlist.append(sublist)

    except ValueError as ve:
        print(fungi.CommonName + ' ERROR - second loop')

    sorteditemlist = sorted(itemlist)

    try:
        count = 0
        for items in splittext:
            allitems.append(count)
            count += 1
            allitemstext.append(items)
    except Exception as e:
        print('ERROR - THIRD LOOP')

    #print('splittext: ',splittext)
    for items in splittext:
        for items3 in sorteditemlist:
            if splittext.index(items) == items3[0]:
                alreadyinlist.append(splittext.index(items))
               # print('alreadyinlist: ', alreadyinlist)
                alreadyinlisttext.append(items3)
                #print('alreadyinlisttext: ', alreadyinlisttext)

    for u in allitems:
        if splittext[u] == ',' or splittext[u] == '.':
            allitems.remove(u)

    tobeadded = [x for x in allitems if x not in alreadyinlist]

    for items in tobeadded:
        p = splittext[items]
        sublist = [items, p]
        itemlist.append(sublist)

    sorteditemlist = sorted(itemlist)
    #print('sorteditemlist: ', sorteditemlist)

    # Creates dictionnary of text  items and links to pass to template
    for items in sorteditemlist:
        if items[0] in alreadyinlist:
            sorteditemsdict['link' + str(items[0])] = items[1]
        else:
            sorteditemsdict['item' + str(items[0])] = items[1]

    if not fungifound:
        sorteditemsdict = sectiontext

    #print('sorteditemsdict = ', sorteditemsdict)

    return [sorteditemsdict, fungifound]
