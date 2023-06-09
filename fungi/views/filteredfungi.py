# from usersettings.models import Show
from django.db.models import Q


def fungi_to_search(fungi, show_only_uk_occurences, show_macromycetes):
    fungi_to_show = fungi.objects.all()
    fungi_count = 0
    result_info = 'All Fungi'
    if show_only_uk_occurences and show_macromycetes:
        fungi_to_show = fungi.objects.filter(Q(UKSpecies__iexact="Yes") & Q(Macromycetes__iexact="Yes"))
        fungi_count = fungi.objects.filter(Q(UKSpecies__iexact="Yes") & Q(Macromycetes__iexact="Yes")).count()
        result_info = 'UK Large Fungi'

    elif show_only_uk_occurences and not show_macromycetes:
        fungi_to_show = fungi.objects.filter(Q(UKSpecies__iexact="Yes"))
        fungi_count = fungi.objects.filter(Q(UKSpecies__iexact="Yes")).count()
        result_info = 'UK Fungi'

    elif not show_only_uk_occurences and show_macromycetes:
        fungi_to_show = fungi.objects.filter(Q(Macromycetes__iexact="Yes"))
        fungi_count = fungi.objects.filter(Q(Macromycetes__iexact="Yes")).count()
        result_info = 'Large Fungi'

    else:
        if not show_only_uk_occurences and not show_macromycetes:
            fungi_to_show = fungi.objects.all()
            fungi_count = fungi.objects.all().count()
            result_info = 'All Fungi'

    return fungi_to_show, fungi_count, result_info
