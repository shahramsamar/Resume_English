from django.contrib import admin
from website.models import ContactModel, BasicInformationModel, SkillModel

# Register your models here.
class SkillModelAdmin(admin.ModelAdmin):
    list_display =('id','title','level')


class BasicInformationAdmin(admin.ModelAdmin):
        list_display = ('email','created_date')

    
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # empty_value_display = '-empty-'
    list_display = ('name','email','created_date')
    list_filter = ('email',)        
    # ordering =['receive_date']
    search_fields =['name','message']
    
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(BasicInformationModel, BasicInformationAdmin)
admin.site.register(SkillModel, SkillModelAdmin)
