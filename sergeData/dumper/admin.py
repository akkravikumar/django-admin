from django.contrib import admin
from .models import Dumper, Dumper_log, Dumper_log_error
import datetime

class DumperLogErrorInline(admin.TabularInline):
    model = Dumper_log_error

class DumperAdmin(admin.ModelAdmin):
    list_display = ('customerCount', 'reportCount', 'status', 'startTime', 'endTime', 'consumedTime', 'errorMessage')
    list_filter = ['status']

class DumperLogAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'reportName', 'status', 'startTime', 'endTime', 'errorMessage')
    search_fields = ('customerName', 'reportName', 'errorMessage', )
    list_filter = ['customerName','startTime']
    inlines = [DumperLogErrorInline	,]

class DumperLogErrorAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'reportName', 'status', 'errorMessage')
    list_filter = ['customerName']
    # inlines = [DumperLogErrorInline	,]

admin.site.register(Dumper, DumperAdmin)
admin.site.register(Dumper_log, DumperLogAdmin)
admin.site.register(Dumper_log_error, DumperLogErrorAdmin)