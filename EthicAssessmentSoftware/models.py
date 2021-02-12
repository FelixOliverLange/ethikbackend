from django.db import models

# Create your models here.
# ------- UML Layer 1

# Anwendung Class
class Anwendung(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique=True)

# ------- UML Layer 2 and 3

# Motivation class
class Motivation(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique=True)
    beschreibung = models.CharField(max_length=200, blank=True, default='')
    schutzklasse = models.CharField(max_length=25, blank=False, default='')
    prioritaet = models.IntegerField(default=1)
    ist_recht = models.BooleanField(default=False)
    anwendung = models.ForeignKey(to=Anwendung, blank=False, on_delete=models.CASCADE)

# Stakeholder class
class Stakeholder(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique=True)
    beschreibung = models.CharField(max_length=200, blank=True, default='')
    anwendung = models.ForeignKey(to=Anwendung, blank=False, on_delete=models.CASCADE)

# Konsequenz class
class Konsequenz(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique=True)
    beschreibung = models.CharField(max_length=200, blank=True, default='')
    bewertung = models.IntegerField()
    betroffener = models.ForeignKey(to=Stakeholder,on_delete=models.CASCADE)
    motivation = models.ForeignKey(to=Motivation, on_delete=models.CASCADE)

# Ansatz Class
class Ansatz(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique=True)
    beschreibung = models.CharField(max_length=200, blank=True, default='')
    adressiert = models.ForeignKey(to=Konsequenz,on_delete=models.CASCADE)
    auswirkung = models.IntegerField(default=0)
    anwendung = models.ForeignKey(to=Anwendung, blank=False, on_delete=models.CASCADE)

# Anforderung class
class Anforderung(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique=True)
    beschreibung = models.CharField(max_length=200, blank=True, default='')
    ansatz = models.ForeignKey(to=Ansatz, on_delete=models.CASCADE)