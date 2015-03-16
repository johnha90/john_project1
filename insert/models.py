from django.db import models
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.event_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class ExhibitorList(models.Model):
    event = models.ForeignKey(Event)
    company = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country =models.CharField(max_length=200)
    booth_no=models.CharField(max_length=200)
    hall_no=models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.event.event_text