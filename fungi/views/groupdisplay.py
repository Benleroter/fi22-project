from django.shortcuts import render
from django import forms
# from fungi.views.choices import *
from fungi.models import Fungi
from fungi.forms import GroupForm

# GROUP
GroupList = []
pid = Fungi.objects.order_by('Group').values('Group').distinct()
for i in pid:
    GroupList.append(i['Group'])

def group_to_display(request):
    group_selection = {}
    group_list = []
    fg = Fungi.objects.order_by('Group').values('Group').distinct()
    for f in fg:
        group_list.append(f['Group'])
    for p in group_list:
        group_selection['Group'] = forms.CharField(required=False, max_length=255, label=p, initial=False)
    dynamic_search_form = type('dynamic_search_form', (GroupForm,), group_selection)
    form = dynamic_search_form(request.POST)
    if form.is_valid():
        context = {
            'group_selection': group_selection,
        }
        return render(request, 'groups.html', context)
