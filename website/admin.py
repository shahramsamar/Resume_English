from django.contrib import admin
from website.models import Contact, BasicInformationModel

# Register your models here.

class BasicInformationAdmin(admin.ModelAdmin):
        list_display = ('id','age')

    
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # empty_value_display = '-empty-'
    list_display = ('name','email','created_date')
    list_filter = ('email',)        
    # ordering =['receive_date']
    search_fields =['name','message']
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(BasicInformationModel)