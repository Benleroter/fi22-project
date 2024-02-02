from django.contrib.auth.models import User
import PIL.Image
from django.urls import reverse
from django.utils.text import slugify
from fungi.choices import *
#from django.contrib.gis.db import models
from django.db import models
from django.utils import timezone
from crum import get_current_user  # pip3 install django-crum


class Fungi(models.Model):
    CommonName = models.CharField(max_length=255, blank=False, null=False, default='Common Name')
    LatinName = models.CharField(max_length=255, blank=False, null=False, default='Latin Name')
    # UKSpecies = models.CharField(max_length=20, choices=UKSpeciesChoices, blank=True, null=True, default='Yes', verbose_name='Recorded in UK')
    UKSpecies = models.CharField(max_length=20, blank=True, null=True, default='Yes', verbose_name='Recorded in UK')
    # Macromycetes = models.CharField(max_length=8, choices=MacromycetesChoices, blank=True, null=True, default='Yes')
    Macromycetes = models.CharField(max_length=8, blank=True, null=True, default='Yes')
    Group = models.CharField(max_length=255, blank=True, null=True, default='not yet assigned')
    Comments = models.CharField(max_length=1024, blank=True, null=True, default='NoData')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Fungi'
        verbose_name = "Fungi"
        verbose_name_plural = "Fungi"
        app_label = "fungi"
        ordering = ["id"]

    def __str__(self):
        return self.CommonName + ", " + self.LatinName + ', ID:' + str(self.id)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})

    # Following  overides save() to create all child records with default data
    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            # print('self.id', self.id)
            OtherCommonNames.objects.create(Fungi=self)
            LatinSynonyms.objects.create(Fungi=self)
            FruitingBody.objects.create(Fungi=self)
            Stipe.objects.create(Fungi=self)
            PoresAndTubes.objects.create(Fungi=self)
            Gills.objects.create(Fungi=self)
            Spores.objects.create(Fungi=self)
            Picture.objects.create(Fungi=self)
            Habitat.objects.create(Fungi=self)
            Cuisine.objects.create(Fungi=self)
            Flesh.objects.create(Fungi=self)
            Classification.objects.create(Fungi=self)
            Seasons.objects.create(Fungi=self)
            NetLinks.objects.create(Fungi=self)
            SimilarFungi.objects.create(Fungi=self)
            Status.objects.create(Fungi=self)
            FungiComments.objects.create(Fungi=self)
            DetailSources.objects.create(Fungi=self)

            if not self.slug:
                self.slug = slugify(self.id)

            return super().save(*args, **kwargs)


class FungiNotes(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_notes')
    User = models.ForeignKey(User, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='FungiNotes_User')
    Note = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    NoteUser = models.IntegerField(default=1, blank=True, null=True)
    NoteDate = models.DateField(default=timezone.now, blank=True, null=True, verbose_name='Note Date')
    MonthFound = models.CharField(max_length=255, choices=MonthFoundChoices, blank=True, verbose_name='Month Found', null=True, default='NoData')
    WhereFound = models.CharField(max_length=2048, blank=True, verbose_name='Where Found', null=True, default='NoData')
    Environment = models.CharField(max_length=2048, blank=True, verbose_name='Environment Notes', null=True, default='NoData')
    NoteCount = models.IntegerField(default=1)
    created_by = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    modified = models.DateField(auto_now=True)
    modified_by = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'FungiNotes'
        verbose_name = "Fungi Note"
        verbose_name_plural = "Fungi Notes"
        ordering = ['NoteUser']
        app_label = "fungi"

    def __str__(self):
        return str(self.Note)+', '+str(self.id) + ', ' + str(self.User) + ', ' + self.Fungi.CommonName + ', ' + str(self.Fungi.id) + ', ' + self.MonthFound + ', ' + str(self.NoteUser)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        user = get_current_user()  # https://django-crum.readthedocs.io/en/latest/  -  method to get current user details in models with request.  Use "get_current user" - see  MIDDLEWARE in settings
        # self.Fungi = 1
        if user and not user.pk:
            user = None
            # print('QQQQQQQQQQQQQQQQQ')
        if not self.pk:
            # print('YYYYYYYYYYYYYYYYYYY')
            self.created_by = user.username
            self.NoteUser = user.id
            self.User = user

        self.modified_by = user.username
        # print('JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ')
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})

class DetailSources(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_detail_sources')
    Source = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    # Detail = models.CharField(max_length=255, choices=ReferenceSourceDetailChoices, blank=True, null=True, default='NoData')
    Detail = models.CharField(max_length=255, blank=True, null=True, default='NoData')

    class Meta:
        managed = True
        db_table = 'DetailSource'
        verbose_name = "DetailSources"
        verbose_name_plural = "DetailSources"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ', ' + self.Source + ', ' + self.Detail


def fungi_choices():
    fungi_list = []
    data = ("0", "NoData")
    fungi_list.append(data)
    f_choices = Fungi.objects.all().distinct()
    for i in f_choices:
        if i.CommonName != 'Common Name':
            data = (i.id, i.CommonName)
        else:
            data = (i.id, i.LatinName)

        fungi_list.append(data)
    sorted_fungi_list = sorted(fungi_list, key=lambda x: (x[1], x[0]))

    return sorted_fungi_list


class SimilarFungi(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_similar')
    slug = models.SlugField(null=True)
    SFid = models.IntegerField(choices=fungi_choices(), blank=True, null=True, verbose_name='Choose similar fungi from drop down list', default=0)
    SimilarFungiName = models.CharField(max_length=255, blank=True, null=True, verbose_name='Similar Fungi Name', default='NoData')

    class Meta:
        managed = True
        db_table = 'SimilarFungi'
        verbose_name = "SimilarFungi"
        verbose_name_plural = "SimilarFungi"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return str('A:' + str(self.Fungi.id) +
                   ', B:' + self.Fungi.CommonName +
                   ', C:' + str(self.slug) +
                   ', D:' + str(self.SFid) +
                   ', E:' + self.SimilarFungiName)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        if self.SFid != 0:
            f = Fungi.objects.get(id=self.SFid)
            if f.CommonName != "Common Name":
                self.SimilarFungiName = f.CommonName
            else:
                self.SimilarFungiName = f.LatinName
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class LatinSynonyms(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_latinnname')
    LatinSynonym = models.CharField(max_length=255, blank=True, null=True, verbose_name='Synonym', default='NoData')
    LatinSynonymSource = models.CharField(max_length=255, blank=True, null=True, verbose_name='Source', default='NoData')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'LatinSynonyms'
        verbose_name = "Latin Synonym"
        verbose_name_plural = "Latin Synonyms"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ', ' + self.LatinSynonym

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class FungiComments(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_comments')
    Comments = models.CharField(max_length=5000, blank=True, null=False, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'FungiComments'
        verbose_name = 'FungiComments'
        verbose_name_plural = 'FungiComments'
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):

        return self.Fungi.CommonName + ', Comments: ' + self.Comments

    def save(self, *args, **kwargs):
        if  self.Comments == "":
            self.Comments = "no comments"
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Seasons(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_seasons')
    Season = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Seasons'
        verbose_name = 'Seasons'
        verbose_name_plural = 'Seasons'
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ", " + self.Season

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Habitat(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_habitat')
    Associations = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    # Ph = models.CharField(max_length=255, choices=choices2.PhTypeChoices, blank=True, null=True, default='NoData')
    Ph = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Soil = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Substrate = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Environment = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Habitat'
        verbose_name = "Habitat"
        verbose_name_plural = "Habitats"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        # return self.Fungi.CommonName + ", " + self.Associations + ', ' + "Fungi_ID:" + str(self.Fungi.id)
        return str('A:' + str(self.Fungi.id) +
                   ', B:' + self.Fungi.CommonName +
                   ', C:' + self.Associations +
                   ', D:' + self.Ph +
                   ', E:' + self.Soil +
                   ', F:' + self.Substrate +
                   ', G:' + self.Environment +
                   ', H:' + self.Comments +
                   ', I:' + self.slug)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class FruitingBody(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_fruitingbody')
    Colour = models.CharField(max_length=1028, blank=True, default='NoData', null=True)
    Shape = models.CharField(max_length=2048, blank=True, default='NoData', null=True)
    Rim = models.CharField(max_length=2048, blank=True, default='NoData', null=True)
    CapTexture = models.CharField(max_length=2048, blank=True, default='NoData', null=True)
    BruiseColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
    CutColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
    WidthMin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
    WidthMax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
    Comments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'FruitingBody'
        verbose_name = "FruitingBody"
        verbose_name_plural = "FruitingBodies"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return str(self.Fungi) + ', WidthMin:' + str(self.WidthMin) + ', WidthMax:' + str(self.WidthMax) + ', colour: ' + self.Colour + ', id:' + str(self.Fungi.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Stipe(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_Stipe')
    Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    BruiseColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
    CutColour = models.CharField(max_length=255, blank=True, default='NoData', null=True)
    LengthMin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
    LengthMax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)  #
    ThicknessMin = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
    ThicknessMax = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0.00, null=True)
    Shape = models.CharField(max_length=2048, blank=True, default='NoData', null=True)
    ReticulationPresent = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Reticulation = models.CharField(max_length=5000, blank=True, null=True, default='NoData')
    Base = models.CharField(max_length=2048, blank=True, null=True, default='NoData')
    Texture = models.CharField(max_length=2048, blank=True, null=True, default='NoData')
    Ring = models.CharField(max_length=20, blank=True, null=True, default='NoData')
    # Ring = models.CharField(max_length=20, choices=RingPresentChoices, blank=True, null=True, default='NoData')
    RingDescription = models.CharField(max_length=2048, blank=True, null=True, default='NoData')
    slug = models.SlugField(null=True)
    # Volva = models.CharField(max_length=20, choices=VolvaChoices, blank=True, null=True, default='NoData')
    Volva = models.CharField(max_length=20, blank=True, null=True, default='NoData')

    Comments = models.CharField(max_length=2048, blank=True, null=True, default='no comments')

    class Meta:
        managed = True
        db_table = 'Stipe'
        verbose_name = "Stipe"
        verbose_name_plural = "Stipes"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        #return str(self.Fungi) + ', LM:' + str(self.LengthMax)
        return str(self.Fungi)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class PoresAndTubes(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_pores')
    #PoresPresent = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    PoresPresent = models.CharField(max_length=20, choices=PoresPresentChoices, blank=True, null=True, default='No')
    PoreColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    PoreShape = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    PoreBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    TubeColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    TubeShape = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    TubeBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    # Milk = models.CharField(max_length=20, choices=MilkPresentChoices, blank=True, null=True, default='NoData')
    PoreMilk = models.CharField(max_length=20, blank=True, null=True, default='NoData')
    Comments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'PoresAndTubes'
        verbose_name = "Pores and Tubes"
        verbose_name_plural = "Pores and Tubes"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return  str(self.Fungi)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Gills(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_gills')
    #GillsData = models.BooleanField(default=False)
    GillsPresent = models.CharField(max_length=20, choices=GillsPresentChoices, blank=True, null=True, default='No')
    GillColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    GillBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    GillCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    GillAttachment = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    GillArrangement = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    # Milk = models.CharField(max_length=20, choices=MilkPresentChoices, blank=True, null=True, default='NoData')
    GillMilk = models.CharField(max_length=20, blank=True, null=True, default='NoData')
    GillComments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Gills'
        verbose_name = "Gills"
        verbose_name_plural = "Gills"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
      #  return self.Fungi.CommonName
        return self.Fungi.CommonName + ', GillColour:' + self.GillColour  + ', GillAttachment:'+ self.GillAttachment

        #return self.Fungi.CommonName + ', ' + self.LatinSynonym
        #return str(self.Fungi)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})

class Spores(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_spores')
    Colour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Comments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Spores'
        verbose_name = "Spores"
        verbose_name_plural = "Spores"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ", spore print colour: " + self.Colour

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Flesh(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_flesh')
    FleshCapColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    FleshCapBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    FleshCapCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    FleshStipeColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    FleshStipeBruiseColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    FleshStipeCutColour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Comments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Flesh'
        verbose_name = 'Flesh'
        verbose_name_plural = 'Flesh'
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})





class NetLinks(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_netlinks')
    Website = models.CharField(max_length=255, verbose_name='Site Name', blank=True, null=True, default='NoData')
    Websiteurl = models.CharField(max_length=255, verbose_name='URL', blank=True, null=True, default='NoData')
    OrderToDisplay = models.IntegerField(blank=True, null=True, default=50)

    class Meta:
        managed = True
        db_table = 'NetLinks'
        verbose_name = "NetLinks"
        verbose_name_plural = "NetLinks"
        ordering = ['Website']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ', ' + self.Fungi.LatinName + ', ' + self.Website


class OtherCommonNames(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_commonname')
    AltCommonName = models.CharField(max_length=255, blank=True, verbose_name='', null=True, default='NoData')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'OtherCommonNames'
        verbose_name = "Other Common Name"
        verbose_name_plural = "Other Common Names"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ', ' + self.AltCommonName

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Classification(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_taxonomy')
    Kingdom = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    Phyum = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    SubPhyum = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    Class = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    SubClass = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    Order = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    Family = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    Genus = models.CharField(max_length=255, blank=False, null=False, default='NoData')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Classification'
        verbose_name = "Classification"
        verbose_name_plural = "Classification"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ", " + self.Fungi.LatinName + ", " + self.Phyum + ", " + self.Class + ", " + self.Order + ", " + self.Family + ", " + self.Genus

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Cuisine(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_cuisine')
    PoisonType = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    CulinaryRating = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Odour = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Taste = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    Comments = models.CharField(max_length=5000, blank=True, null=True, default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Cuisine'
        verbose_name = 'Cuisine'
        verbose_name_plural = 'Cuisine'
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ", " + "Culinary rating: " + self.CulinaryRating

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Picture(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_picture')
    image = models.ImageField(default='default.jpg', upload_to='images')

    class Meta:
        managed = True
        db_table = 'Pictures'
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ', ' + self.image.path

    def save(self, *args, **kwargs):
        super(Picture, self).save(*args, **kwargs)

        # fp = open("/pdf-ex/downloadwin7.png","rb")
        # img = PIL.Image.open(fp)
        # img.show()

        # image=PIL.Image.open('/home/pi/Desktop/scene.jpg')   #use this
        # img = Image.open(self.image.path)

        img = PIL.Image.open(self.image.path)

        # if img.height > 20 or img.width > 20:
        output_size = (350, 350)
        img.thumbnail(output_size)
        img.save(self.image.path)


class Status(models.Model):
    Fungi = models.ForeignKey(Fungi, max_length=255, blank=False, null=False, on_delete=models.CASCADE, related_name='fungi_Status')
    StatusData = models.CharField(max_length=255, blank=True, null=True, verbose_name='Status', default='NoData')
    WhereFound = models.CharField(max_length=255, blank=True, null=True, verbose_name='Where found', default='NoData')
    StatusComments = models.CharField(max_length=5000, blank=True, null=True, verbose_name='Comments', default='no comments')
    slug = models.SlugField(null=True)

    class Meta:
        managed = True
        db_table = 'Status'
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['Fungi']
        app_label = "fungi"

    def __str__(self):
        return self.Fungi.CommonName + ', status: ' + self.StatusData + ', Mainly found in: ' + self.WhereFound

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Fungi_id)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('FungiDetail-Page', kwargs={'slug': self.slug})


class Glossary(models.Model):
    Term = models.CharField(max_length=50, blank=True, null=True, default='NoData')
    term_lower_case = models.CharField(max_length=50, blank=True, null=True, verbose_name='term lc', default='NoData')
    Meaning = models.CharField(max_length=255, blank=True, null=True, default='NoData')
    slug = models.SlugField(null=True)
    Source = models.CharField(max_length=255, blank=True, null=True, default='NoData')

    class Meta:
        managed = True
        db_table = 'Glossary'
        verbose_name = 'Glossary'
        verbose_name_plural = 'Glossary'
        ordering = ['Term']
        app_label = "fungi"

    def __str__(self):
        return 'Term: ' + self.Term + ', Meaning: ' + self.Meaning + ', slug:' + self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Term)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('glossary_entry', kwargs={'slug': self.slug})  # new

