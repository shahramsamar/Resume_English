from django.db import models


FREELANCER_CHOICES = [
    ('Available', 'Available'),
    ('Unavailable', 'Unavailable'),
]
'''
"Associate's": Typically a two-year undergraduate degree.
"Bachelor's": Typically a four-year undergraduate degree.
"Master's": A graduate degree following a bachelor's.
"Doctorate": The highest level of academic degree, often involving advanced research.
"Professional": Degrees like MD (Doctor of Medicine), JD (Juris Doctor), etc.
"Certificate": Usually a shorter, specialized training program.
"Diploma": Can refer to a degree or a specific qualification in certain countries.
"High School": Represents completion of secondary education.
'''
DEGREE_CHOICES = [
    ("Associate's", "Associate's"),
    ("Bachelor's", "Bachelor's"),
    ("Master's", "Master's"),
    ("Doctorate", "Doctorate"),
    ("Professional", "Professional"),
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
    ("High School", "High School"),
]


        
class BasicInformationModel(models.Model):
        first_name = models.CharField(max_length=255)
        last_name = models.CharField(max_length=255)
        job_title = models.CharField(max_length=255)
        image = models.ImageField(upload_to='image',default='image/user.jpeg')
        birthday = models.DateField(blank=True, null=True)        
        about_me = models.TextField()
        age = models.PositiveIntegerField()
        email = models.EmailField()
        phone_number = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
        language = models.CharField(max_length=255)
        freelance = models.CharField(max_length=255, choices=FREELANCER_CHOICES,default='Unavailable')
        website = models.CharField(max_length=255)
        entertainment = models.CharField(max_length=255)
        degree = models.CharField(max_length=12, choices=DEGREE_CHOICES)  
        summary = models.TextField()
        created_date = models.DateTimeField(auto_now_add =True)
        updated_date = models.DateTimeField(auto_now=True)
        
       
        class Meta :
                ordering = ['created_date']
        
       
        def __str__(self):
                return f"{self.first_name} {self.last_name}"
       
        
class ContactModel(models.Model):
        name = models.CharField(max_length=255)
        email = models.EmailField()
        subject = models.CharField(max_length=255)
        message = models.TextField()
        created_date = models.DateTimeField(auto_now_add =True)
        updated_date = models.DateTimeField(auto_now=True)
        
        class Meta :
                ordering = ['created_date']
        
        def __str__(self):
                return self.name
class  SkillModel(models.Model):
    title = models.CharField(max_length=255)   
    level = models.PositiveBigIntegerField(default=50)
    created_date = models.DateTimeField(auto_now_add =True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta :
        ordering = ['created_date']
    def __str__(self):
        return self.title         

class  EducationModel(models.Model):
    title = models.CharField(max_length=255) 
    major = models.CharField(max_length=255) 
    location = models.CharField(max_length=255)
    from_date = models.IntegerField(blank=True, null=True)
    to_date = models.IntegerField(blank=True, null=True)
    
    class Meta :
        ordering = ['-from_date']

        
class  ProfessionalExperienceModel(models.Model):
    title = models.CharField(max_length=255) 
    compony = models.CharField(max_length=255) 
    location = models.CharField(max_length=255)
    jobـdescription = models.TextField()
    from_date = models.IntegerField(blank=True, null=True)
    to_date = models.IntegerField(blank=True, null=True)
    
    class Meta :
        ordering = ['-from_date']


