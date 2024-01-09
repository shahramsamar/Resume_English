from django.contrib import admin
from website.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'receive_date'
    empty_value_display = '-empty-'
    list_display = ('name','subject','receive_date','response','response_date')
    list_filter = ('response',)        
    ordering =['receive_date']
    search_fields =['name','subject']
    
admin.site.register(Contact,ContactAdmin)