from django.db import models
from django.conf import settings as djangoSetting

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    startDate = models.DateTimeField(db_index=True)
    endDate = models.DateTimeField(db_index=True)
    allDay = models.BooleanField()
    rRule = models.CharField(max_length=50)
    desc = models.TextField(blank=True)
    creator = models.ForeignKey(
            djangoSetting.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            verbose_name="creator",
            related_name='creator')
    end_recurring_period = models.DateTimeField(
            null=True, blank=True, db_index=True, 
            help_text="This date is ignored for one time only events.") 
    
    def __str__(self):
        return self.title
