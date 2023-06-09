from django.shortcuts import render
from usersettings.models import ShowSearchFields
from fungi.views.FieldsToShow import fields_to_show
from fungi.forms import UserSearchForm
from fungi.views.getparamsfromform import get_params_from_form
from fungi.views.editedQparams import clean_q_params
from fungi.views.runsearch import run_search
import copy
import re


def search(request):
    user_search_fields = ShowSearchFields.objects.get(user_id=request.user)
    #print('user_id = ', request.user)
    #print('user_search_fields = ', user_search_fields)
    if request.method == 'POST':
        fields_to_display = fields_to_show(user_search_fields)
        print('fieldsToDisplay = ', fields_to_display)
        dynamic_search_form = type('DynamicSearchForm', (UserSearchForm,), fields_to_display)
        form = dynamic_search_form(request.POST)
        if form.is_valid():
            q_params = get_params_from_form(form)
            q_params = clean_q_params(q_params)
            for key, value in q_params.items():
                print('key = ', key)
            print('q_params_A = ', q_params)
            #print('q_params_A = ', q_params['CommonName'])
            fungi_found = run_search(q_params)
            print('fungi_found = ', fungi_found)
            fungi_found_count = len(fungi_found[0])
            if fungi_found_count == 0:
                q_params2 = copy.deepcopy(q_params)
                for key, value in q_params2.items():
                    res = key
                    s = re.sub(r"(\w)([A-Z])", r"\1 \2", res)
                    new_key = s
                    old_key = res
                    q_params[new_key] = q_params.pop(old_key)
                context = {
                    'SearchTerms': q_params,
                    'SearchTermsCount': len(q_params)
                }
                return render(request, 'searchresultszero.html', context)

            print('fungi_found[0] = ', fungi_found[0])
            print('fungi_found[1] = ', fungi_found[1])
            print('fungi_found[2] = ', fungi_found[2])
            print('fungi_found_count = ', str(fungi_found_count))

            search_term = ""

            for key, value in q_params.items():
                if key == 'LatinName':
                    search_term = value

                if key == 'CommonName':
                    search_term = value

            context = {
                'search_fungi_results': fungi_found[0],
                'synonymlist': fungi_found[1],
                'commonnameslist': fungi_found[2],
                'resultscount': fungi_found_count,
                'SearchTerms': search_term
            }

            return render(request, 'search_results.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        fields_to_display = fields_to_show(user_search_fields)
        dynamic_search_form = type('DynamicSearchForm', (UserSearchForm,), fields_to_display)
        form = dynamic_search_form(request.POST)

    return render(request, 'searchform.html', {'form': form})
