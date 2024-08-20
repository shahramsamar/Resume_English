from django.shortcuts import render
from website.forms import ContactForm
from website.models import BasicInformationModel, SkillModel, EducationModel, ProfessionalExperienceModel



def index_view(request):
    Experience = ProfessionalExperienceModel.objects.all()
    Education = EducationModel.objects.all()
    skills = SkillModel.objects.all()
    personality  = BasicInformationModel.objects.all()
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()        
    context = {"form":form,
               'personality':personality,
               'skills':skills,
               'Education':Education,
               'Experience':Experience}
    return render(request, 'website/index.html', context)