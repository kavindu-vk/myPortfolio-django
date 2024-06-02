from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from . models import Career, Home, About, Skills, Education, Experience, UploadedPDF, Portfolio, ContactInfo, Contact, ContactMessage

# Create your views here.
def index(request):

    careers = Career.objects.all()

    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')

    skills = Skills.objects.all()

    education = Education.objects.all()

    experience = Experience.objects.all()

    upload_pdf = UploadedPDF.objects.latest('updated')

    portfolios = Portfolio.objects.all()

    contact = Contact.objects.latest('updated')

    contactInfo = ContactInfo.objects.filter(contacts=contact)

    context = {'careers': careers, 'home':home, 'about':about, 'skills':skills, 'education':education, 'experience':experience, 'upload_pdf':upload_pdf, 'portfolios':portfolios, 'contactInfo':contactInfo, 'contact':contact}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # send mail
            send_mail(
                subject,
                f"Message from: {name}\nEmail: {email}\n\n{message}",
                'kavinduranasingha57@gmail.com',
                ['kavinduranasingha57@gmail.com'],
                fail_silently=False,
            )
            contact_message = ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        
    else:
        form = ContactForm()
        return render(request, 'index.html', {'form': form})