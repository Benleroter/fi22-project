from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FungiForm(forms.ModelForm):
    class Meta:
        model = Fungi
        fields = '__all__'


class NotesCreateForm(forms.ModelForm):
    class Meta:
        model = FungiNotes
        # fields = ('User','Fungi','Note', 'MonthFound', 'WhereFound', 'Environment')
        fields = ('Note', 'MonthFound', 'WhereFound', 'Environment')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('User')
        self.fungi = Fungi.CommonName
        super(NotesCreateForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if FungiNotes.objects.filter(user=self.user, title=title).exists():
            raise forms.ValidationError("You have already written a book with same title.")
        return title

FungiNotesFormset3 = inlineformset_factory(
    Fungi,
    FungiNotes,
    extra=1,
    labels='',
    can_delete=True,
    exclude=('Fungi', 'slug', 'NoteCount', 'NoteUser'),
    # formset = NotesForm3
)

FungiNotesFormset = inlineformset_factory(
    Fungi,
    FungiNotes,
    extra=1,
    labels='',
    can_delete=True,
    exclude=('slug', 'NoteCount'),
    # formset = NotesForm
)

FungiNetLinksFormset = inlineformset_factory(
    Fungi,
    NetLinks,
    extra=1,
    labels='',
    can_delete=True,
    fields=('Website', 'Websiteurl')
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserSearchForm(forms.Form):
    pass

class GroupForm(forms.Form):
    pass

FungiFormset = modelformset_factory(
    Fungi,
    extra=1,
    labels='',
    can_delete=False,
    fields='__all__'
)

FungiHabitatFormset = inlineformset_factory(
    Fungi,
    Habitat,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiCapFormset = inlineformset_factory(
    Fungi,
    FruitingBody,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiStipeFormset = inlineformset_factory(
    Fungi,
    Stipe,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiCuisineFormset = inlineformset_factory(
    Fungi,
    Cuisine,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiFleshFormset = inlineformset_factory(
    Fungi,
    Flesh,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiSeasonsFormset = inlineformset_factory(
    Fungi,
    Seasons,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiSporesFormset = inlineformset_factory(
    Fungi,
    Spores,
    extra=0,
    labels='',
    can_delete=False,
    # fields=('Colour','Comments')
    exclude=('slug',)
)

FungiStatusFormset = inlineformset_factory(
    Fungi,
    Status,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiPoresFormset = inlineformset_factory(
    Fungi,
    PoresAndTubes,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiGillsFormset = inlineformset_factory(
    Fungi,
    Gills,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiCommentsFormset = inlineformset_factory(
    Fungi,
    FungiComments,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiTaxonomyFormset = inlineformset_factory(
    Fungi,
    Classification,
    extra=0,
    labels='',
    can_delete=False,
    # fields='__all__'
    exclude=('slug',)
)

FungiRefsFormset = inlineformset_factory(
    Fungi,
    DetailSources,
    extra=1,
    labels='',
    can_delete=True,
    fields='__all__'
)

# FungiRefsDeleteFormset = inlineformset_factory(
#     Fungi,
#     DetailSources,
#     extra=0,
#     labels='',
#     can_delete=True,
#     fields='__all__'
# )

FungiLatinSynomymsFormset = inlineformset_factory(
    Fungi,
    LatinSynonyms,
    extra=1,
    labels='',
    can_delete=True,
    fields=('LatinSynonym', 'LatinSynonymSource')
)

# FungiLatinSynomymsDeleteFormset = inlineformset_factory(
#     Fungi,
#     LatinSynonyms,
#     extra=0,
#     labels='',
#     can_delete=True,
#     fields=('LatinSynonym',)
# )

FungiSimilarFormset = inlineformset_factory(
    Fungi,
    SimilarFungi,
    extra=1,
    labels='',
    can_delete=True,
    # fields=('SimilarFungiName2',)
    fields=('SFid',)
)

# FungiNetLinksDeleteFormset = inlineformset_factory(
#     Fungi,
#     NetLinks,
#     extra=0,
#     labels='',
#     can_delete=True,
#     fields=('Website', 'Websiteurl')
# )

FungiCommonNamesFormset = inlineformset_factory(
    Fungi,
    OtherCommonNames,
    extra=1,
    labels='',
    can_delete=True,
    fields=('AltCommonName',)
)

# FungiCommonNamesDeleteFormset = inlineformset_factory(
#     Fungi,
#     OtherCommonNames,
#     extra=0,
#     labels='',
#     can_delete=True,
#     fields=('AltCommonName',)
# )

# class FungiForm(forms.ModelForm):
#     class Meta:
#         model = Fungi
#         fields = "__all__"
GlossaryFormset = modelformset_factory(
    Glossary,
    extra=1,
    labels='',
    can_delete=True,
    exclude=('slug',)
    # fields='__all__'
)
