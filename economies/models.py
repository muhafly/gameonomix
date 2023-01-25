from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    read_code = models.CharField(max_length=120)
    update_code = models.CharField(max_length=120)
    start_time = models.DateTimeField()  
    end_time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class EconomicModel(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    economic_model = models.JSONField(blank=True, null=True)
    economic_model_raw_data = models.JSONField(blank=True, null=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.economic_model