from django.contrib import admin
from . models import Career, Home, About, Skills, Education, Experience, UploadedPDF, Portfolio, ContactInfo, Contact, ContactMessage

# Register your models here.

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
     pass

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
     filter_horizontal = ("careers",)

admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(UploadedPDF)
admin.site.register(Portfolio)
admin.site.register(ContactMessage)

# Contact
class ContactInline(admin.TabularInline):
    model = ContactInfo
    extra = 1

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     inlines = [
        ContactInline,
    ]