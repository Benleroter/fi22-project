from django.shortcuts import render
from fungi.views.filteredfungi import fungi_to_search
from usersettings.models import Show
from django.views.generic import ListView, CreateView, DetailView, FormView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import UpdateView
from fungi.forms import *
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from fungi.models import FungiNotes
from django.contrib.auth.models import User


class FunginoteCreate(CreateView):
    model = FungiNotes
    template_name = 'fungi_note_create.html'
    form_class = NotesCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        f = self.get_object(queryset=Fungi.objects.all())
        self.object.Fungi_id = f.id
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = self.request.user
        f = self.get_object(queryset=Fungi.objects.all())
        context["Fungi_Id"] = f.id
        if f.CommonName == "Common Name":
            context["Fungi_CommonName"] = ""
        else:
            context["Fungi_CommonName"] = f.CommonName
        context["Fungi_LatinName"] = f.LatinName
        context["Fungi_note"] = True
        print('context = ', context)
        return context

    def get_initial(self, *args, **kwargs):
        initial = super(FunginoteCreate, self).get_initial(**kwargs)
        initial['Fungi'] = self.get_object(queryset=Fungi.objects.all())
        initial['User'] = self.request.user
        return initial

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(FunginoteCreate, self).get_form_kwargs(*args)#**kwargs)
        kwargs['User'] = self.request.user
        return kwargs


class FunginoteDelete(DeleteView):
    model = FungiNotes
    template_name = 'fungi_note_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = self.request.user
        f = self.get_object(queryset=FungiNotes.objects.all())
        context["Fungi_Id"] = f.Fungi.id
        if f.Fungi.CommonName == "Common Name":
            context["Fungi_CommonName"] = ""
        else:
            context["Fungi_CommonName"] = f.Fungi.CommonName
        context["Fungi_LatinName"] = f.Fungi.LatinName
        context["Fungi_note"] = True
        return context

    def get_success_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FunginoteEdit(UpdateView):
    model = FungiNotes
    template_name = 'fungi_note_edit.html'
    fields = ('Note', 'MonthFound', 'WhereFound', 'Environment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user = self.request.user
        f = self.get_object(queryset=FungiNotes.objects.all())
        context["Fungi_Id"] = f.Fungi.id
        if f.Fungi.CommonName == "Common Name":
            context["Fungi_CommonName"] = ""
        else:
            context["Fungi_CommonName"] = f.Fungi.CommonName
        context["Fungi_LatinName"] = f.Fungi.LatinName
        context["Fungi_note"] = True
        return context


def home(request):
    if request.user.is_authenticated:
        uid = request.user
    else:
        uid = User.objects.get(username='GuestUser')

    context = {
        'fungis': Fungi.objects.all(),
    }
    return render(request, 'home.html', context)


def links(request):
    return render(request, 'links.html')


def all_sources(request):
    sources = NetLinks.objects.order_by().values('Website').distinct()
    print('sourcesquery', sources.query)

    context = {
        'sources': NetLinks.objects.order_by('Website').values('Website').distinct()
    }
    return render(request, 'sources.html', context)


def all_groups(request):
    groups = Fungi.objects.order_by('Group').values('Group').distinct()
    context = {
        'groups': Fungi.objects.order_by('Group').values('Group').distinct()
    }
    return render(request, 'groups.html', context)


def all_fungi(request):
    if request.user.is_authenticated:
        uid = request.user
        usershowsettings = Show.objects.get(user_id=request.user)
    else:
        uid = User.objects.get(username='GuestUser')
        usershowsettings = Show.objects.get(user_id=uid)

    # Show or don't show non-UK Species and/or Macromycetes
    fungi_to_render = fungi_to_search(Fungi, usershowsettings.ShowOnlyUKOccurences, usershowsettings.ShowMacromycetes)
    print('FUNGI', Fungi)
    context = {
        'fungis': fungi_to_render[0],
        'fungicount': fungi_to_render[1],
        'ResultText': fungi_to_render[2]
    }
    return render(request, 'allfungi.html', context)


def show_glossary(request):
    glossary = Glossary.objects.all()
    context = {
        'Glossary': glossary
    }
    # print('Glossary context:', context)
    return render(request, 'glossary.html', context)


def show_sources_list(request):
    # sourcename = NetLinks.objects.filter(Website=).distinct()
    sourcename = NetLinks.objects.order_by('Website').values('Website').distinct()

    context = {
        'SourceName': sourcename
    }
    return render(request, 'sources.html', context)


class GlossaryEntry(DetailView):
    model = Glossary
    template_name = 'glossarydetail.html'


class ShowFungiEntry(DetailView):
    model = Fungi
    template_name = 'fungi_detail.html'


class ShowSources(ListView):
    model = DetailSources
    template_name = 'sources.html'

    def get_context_data(self, **kwargs):
        sources = super(ShowSources, self).get_context_data(**kwargs)
        return sources


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def index(request, fungi_id):
    fungi = Fungi.objects.get(pk=fungi_id)
    language_formset = inlineformset_factory(Fungi, LatinSynonyms, can_delete=False, extra=0, labels=None, fields=('LatinSynonym',))

    if request.method == 'POST':
        formset = language_formset(request.POST, instance=fungi)
        if formset.is_valid():
            formset.save()
            return redirect('index', fungi_id=Fungi.id)
    formset = language_formset(instance=fungi)
    return render(request, 'index.html', {'formset': formset})


class FungiEditView(UpdateView):
    model = Fungi
    template_name = 'fungi_edit.html'
    fields = ['CommonName', 'LatinName', 'Group', 'UKSpecies', 'Macromycetes', 'Comments']


class FungiCreateView(CreateView):
    model = Fungi
    template_name = 'fungi_create.html'
    fields = ['CommonName', 'LatinName', 'Group', 'UKSpecies', 'Macromycetes', 'Comments']

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The Fungi has been added'
        )

        return super().form_valid(form)


class GlossaryTermView(CreateView):
    model = Glossary
    template_name = 'glossary_terms.html'
    fields = '__all__'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The new term has been added'
        )

        return super().form_valid(form)


class FungiLatinSynomymsView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_latinsynonyms.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiLatinSynomymsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiHabitatView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_habitat.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiHabitatFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiFruitingBodyView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_fruiting_body.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCapFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiStipeView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_stipe.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiStipeFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiCuisineView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_cuisine.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCuisineFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiFleshView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_flesh.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiFleshFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiSimilarView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_similar.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSimilarFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiCommonNamesView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_commonnames.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCommonNamesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiSeasonsView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_seasons.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSeasonsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiSporesView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_spores.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiSporesFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiStatusView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_status.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiStatusFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})

        # return HttpResponseRedirect(self.get_success_url())


class FungiPoresView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_pores.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiPoresFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiGillsView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_gills.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiGillsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiCommentsView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_comments.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiCommentsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiTaxonomyView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_taxonomy.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiTaxonomyFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiLinksView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_netlinks.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiNetLinksFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class FungiRefsView(SingleObjectMixin, FormView):
    model = Fungi
    template_name = 'fungi_refs.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Fungi.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return FungiRefsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # return reverse('FungiDetail-Page', kwargs={'pk': self.object.pk})
        return reverse('FungiDetail-Page', kwargs={'slug': self.object.slug})


class GlossaryFormView(FormView):
    template_name = 'glossary_terms.html'
    form_class = GlossaryFormset
    success_url = '/'

    def form_valid(self, form):
        form.save()

        return HttpResponseRedirect(self.get_success_url())
