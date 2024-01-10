from django.contrib import admin
from website.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    # empty_value_display = '-empty-'
    list_display = ('name','email','create_date')
    list_filter = ('email',)        
    # ordering =['receive_date']
    search_fields =['name','message']
    
admin.site.register(Contact,ContactAdmin)