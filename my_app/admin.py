from django.contrib import admin
from .models import Sport,Athlete,Medal,Event,Result,HistoricalData

admin.site.register(Sport)
admin.site.register(Athlete)
admin.site.register(Medal)
admin.site.register(Event)
admin.site.register(Result)
admin.site.register(HistoricalData)


