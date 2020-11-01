from django.db import models
from django.conf import settings as djangoSetting

class Event(models.Model):
    title = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    # For Individual Events
    start = models.DateTimeField(db_index=True)
    end = models.DateTimeField(db_index=True)
    # For Recurring Events like club time (Not Individual)
    startTime = models.TimeField(null=True, blank=True)
    endTime = models.TimeField(null=True, blank=True)
    startRecur = models.DateTimeField(db_index=False, null=True, blank=True)
    endRecur = models.DateTimeField(db_index=False, null=True, blank=True)
    daysOfWeek = models.JSONField(null=True, blank=True) 
    groupId = models.CharField(max_length=50, blank=True);
    # ETC
    allDay = models.BooleanField(default=False)
    color = models.CharField(max_length=7, default='#3E80BD');
    desc = models.TextField(blank=True)
    creator = models.ForeignKey(
            djangoSetting.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            null=True,
            blank=True,
            to_field="username",
            verbose_name="creator",
            related_name='creator')
    
    def __str__(self):
        return self.title
