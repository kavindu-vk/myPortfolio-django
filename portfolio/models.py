from django.db import models

# Create your models here.

class Career(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Home section
class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting = models.CharField(max_length=20)
    careers = models.ManyToManyField(Career)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# About Section
class About(models.Model):
    heading = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

class Skills(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)

    def __str__(self):
        return self.skill_name
    

class Education(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    date_range = models.CharField(max_length=20, help_text='Format: "YYYY-YYYY"', default='2016-2023')
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200, default='Todfod University')
    description = models.TextField(blank=False, default='Your default value goes here')

    def __str__(self):
        return f"{self.title} ({self.date_range})"

class Experience(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    date_range = models.CharField(max_length=20, help_text='Format: "YYYY-YYYY"', default='2016-2023')
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200, default='The Webshala')
    description = models.TextField(blank=False, default='Your default value goes here')

    def __str__(self):
        return f"{self.title} ({self.date_range})"
    

class UploadedPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pdf_file.name


# PORTFOLIO SECTION
class Portfolio(models.Model):
    portfolio_img = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False, default='Your default value goes here')
    created = models.DateTimeField(auto_now_add=True, null=True)
    technology_used = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="Front-end")
    View_Online = models.URLField(max_length=200, default="https://www.youtube.com")

    def __str__(self):
        return f'Portfolio {self.id}'
    

# CONTACT SECTION
class Contact(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class ContactInfo(models.Model):
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email