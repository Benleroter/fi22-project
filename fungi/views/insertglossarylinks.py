from fungi.models import Glossary
from django.urls import reverse


def insertglossarylinks(sectiontext):
    glossary = Glossary.objects.all()
    sorteditemsdict = {}
    itemlist = []
    alreadyinlist = []
    allitems = []
    termfound = False
    #print('seciontext', sectiontext)
    # loop through Glossary, if glossary term in text from DB get start/end indexes of term in text
    splittext = sectiontext.split()
    gt = "Term not found"
    #print('Glossary:', glossary )
    try:
        for glossaryterm in glossary:
            gt = glossaryterm.Term
            if gt in sectiontext:
                try:
                    idx = splittext.index(gt + ',')
                except:
                    idx = splittext.index(gt)
                termfound = True
                pathandtext = [reverse('glossary_entry', args=[gt]), splittext[idx]]
                sublist = [idx, pathandtext]
                # print('pathandtext = ', pathandtext)
                itemlist.append(sublist)

        for glossarytermlc in glossary:
            gtlc = glossarytermlc.term_lower_case
            if gtlc in sectiontext:
                try:
                    idx = splittext.index(gtlc + ',')
                except:
                    idx = splittext.index(gtlc)
                termfound = True
                pathandtext = [reverse('glossary_entry', args=[gtlc]), splittext[idx]]
                sublist = [idx, pathandtext]
                # print('pathandtext = ', pathandtext)
                itemlist.append(sublist)

    except Exception as e:
        print('gt = ', gt)

    sorteditemlist = sorted(itemlist)

    for items in splittext:
        allitems.append(splittext.index(items))

    for items in splittext:
        for items3 in sorteditemlist:
            if splittext.index(items) == items3[0]:
                alreadyinlist.append(splittext.index(items))

    tobeadded = [x for x in allitems if x not in alreadyinlist]

    for items in tobeadded:
        p = splittext[items]
        sublist = [items, p]
        itemlist.append(sublist)

    sorteditemlist = sorted(itemlist)

    for items in sorteditemlist:
        if items[0] in alreadyinlist:
            sorteditemsdict['link' + str(items[0])] = items[1]
        else:
            sorteditemsdict['item' + str(items[0])] = items[1]

    if not termfound:
        sorteditemsdict = sectiontext

    return [sorteditemsdict, termfound]
