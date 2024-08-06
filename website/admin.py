from django.contrib import admin
from website.models import ContactModel, BasicInformationModel, SkillModel, EducationModel

class EducationModelAdmin(admin.ModelAdmin):
    list_display =('id','title','location','from_date','until_date')
    
class SkillModelAdmin(admin.ModelAdmin):
    list_display =('id','title','level','created_date','updated_date')


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
admin.site.register( EducationModel,EducationModelAdmin)

