from django.db import models
from django.utils import timezone 
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)


    def get_duration(visit):
      if visit.leaved_at:
        return (localtime(visit.leaved_at) - localtime(visit.entered_at)).total_seconds()
      else:
        return (timezone.now() - localtime(visit.entered_at)).total_seconds()


    def format_duration(visit):
      time_duration = visit.get_duration()
      return f"{int(time_duration // 3600)}ч {int(time_duration % 3600 / 60)}мин"


    def is_visit_long(visit):
       duration = visit.get_duration()
       return duration > 3600
       
  
      
    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
