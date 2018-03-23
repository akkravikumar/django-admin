from django.db import models

# Create your models here.
class Dumper(models.Model):
    customerCount = models.IntegerField(blank=False, null=False)
    reportCount = models.IntegerField(blank=False, null=False)
    status = models.TextField(blank=False, null=False)
    startTime=models.TextField(blank=False, null=False)
    endTime = models.TextField(blank=True, null=True)
    consumedTime = models.TextField(blank=True, null=True)
    errorMessage = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'logger'

class Dumper_log(models.Model):
    dumper = models.ForeignKey(Dumper)
    customerName = models.TextField(blank=False, null=False)
    reportName = models.TextField(blank=False, null=False)
    status = models.TextField(blank=False, null=False)
    startTime = models.TextField(blank=False, null=False)
    endTime = models.TextField(blank=True, null=True)
    consumedTime = models.TextField(blank=True, null=True)
    errorMessage = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'logger'

class Dumper_log_error(models.Model):
    log = models.ForeignKey(Dumper_log)
    customerName = models.TextField(blank=False, null=False)
    reportName = models.TextField(blank=False, null=False)
    status = models.TextField(blank=False, null=False)
    errorMessage = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'logger'