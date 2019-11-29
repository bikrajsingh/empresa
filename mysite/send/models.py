from django.db import models

#from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Client(models.Model):
    Nom = models.CharField(max_length=100)
    oficina = models.CharField(max_length=120)
    correu = models.CharField(max_length=120)
    missatge = models.TextField()

    def __unicode__(self):
        return u"%s" % self.nif

    def get_absolute_url(self):
        return reverse('send:client_detail', kwargs={'pk': self.pk})
