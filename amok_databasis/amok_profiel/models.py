from django.db import models
from django.utils.timezone import now
# Create your models here.
class adres(models.Model):
    class Meta:
        verbose_name = "Adres"
        verbose_name_plural = "Adresse"
    adres = models.TextField()
    dorp = models.CharField(max_length=300)
    provinsie = models.CharField(max_length=300)
    poskode = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.adres} {self.provinsie}'

class profiel(models.Model):
    titels = (
        ("Mev.", "Mev"),
        ("Mnr.", "Mnr."),
        ("Rev.", "Rev.")
    )
    
    geslag = (
        ("Manlik", "Manlik"),
        ("Vroulik", "Vroulik")
    )
    
    huwelikstatus = (
        ("Ongetroud", "Ongetroud"),
        ("Getroud", "Getroud")
    )
    
    class Meta:
        verbose_name =  "Amok Profiel"
        verbose_name_plural = "Amok Profiele"
    
    idnommer = models.CharField(max_length=13)
    title = models.CharField(max_length=10, choices=titels)
    vollename = models.CharField(max_length=500)
    van = models.CharField(max_length=500)
    noemnaam = models.CharField(max_length=500)
    geboortedatum = models.DateField()
    epos = models.EmailField()
    geslag = models.CharField(max_length=10, choices=geslag, default="Manlik")
    huwelikstatus = models.CharField(max_length=10, choices=huwelikstatus, default="Getroud")
    huistaal = models.CharField(max_length=20)
    ras = models.CharField(max_length=20)
    adres = models.ForeignKey(adres, on_delete=models.DO_NOTHING, null=True, default=None)
    skepdatum = models.DateTimeField(default=now,auto_created=True)
    foto = models.ImageField(null=True, default=None, upload_to='static/profiele')
    #hier kort nog 'n verbintenis veld
    
    def __str__(self) -> str:
        return f'{self.idnommer}'
    
class voertuig(models.Model):
    
    class Meta:
        verbose_name = "Voertuig"
        verbose_name_plural = "Voertuie"
    
    fabrikaat = models.CharField(max_length=300)
    reeks = models.CharField(max_length=300)
    kleur = models.CharField(max_length=50)
    jaar_model = models.CharField(max_length=50)
    registrasie = models.CharField(max_length=10)
    nota = models.TextField(max_length=800)
    
    def __str__(self) -> str:
        return f'{self.registrasie} {self.fabrikaat}'
    
    

    
