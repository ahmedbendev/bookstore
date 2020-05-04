from django.db import models
from django.contrib.auth.models import User
from store.models import Usedbook
from django.utils import timezone
from django.db.models import Count
from django.urls import reverse

class Offre(models.Model):
    content = models.TextField()
    userdemandeur = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "offreuserdemandeur")
    useroffreur = models.ForeignKey(User , on_delete = models.CASCADE , related_name = "offreuseroffreur")
    usedbookoffer = models.ForeignKey(Usedbook , on_delete = models.CASCADE , related_name = "offreusedbookoffer")
    usedbookdemandeur = models.ForeignKey(Usedbook , on_delete = models.CASCADE , related_name = "offreusedbookdemandeur")
    state = models.CharField(max_length = 100 , default="waiting for response")
    offre_pub_date = models.DateTimeField(default = timezone.now)
    offre_aprove_date = models.DateTimeField(null = True)
    offre_refuse_date = models.DateTimeField(null = True)
    offre_done_date = models.DateTimeField(null = True)

    def __str__(self):
        return str(self.pk)
    def get_absolute_url(self):
        return reverse('offer-detail', kwargs={'pk':self.pk})
    def aprove(self):
        self.state = "approved"
        self.offre_aprove_date = timezone.now()
        self.save()
    def refuse(self):
        self.state = "refuse"
        self.offre_refuse_dat = timezone.now()
        self.save()
    def done(self):
        self.state = "done"
        self.offre_done_date = timezone.now()
        self.save()
