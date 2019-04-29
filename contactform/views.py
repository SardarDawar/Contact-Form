from django.shortcuts import render,redirect

from .forms import contact

from django.conf import settings
from django.core.mail import send_mail

from django.core.mail import EmailMessage




def Contact(request):
    form = contact()
    subject = 'contact blog'
    if request.method=='POST':
        form = contact(request.POST or None)
        if form.is_valid():
            name=form.cleaned_data.get('Name')
            email=form.cleaned_data.get('Email')
            message = form.cleaned_data.get('Message')
            email_from=email
            send_mail( subject, message, email_from, recipient_list=[settings.EMAIL_HOST_USER,email_from] )
            
    return render(request,'contact.html',{'form':form})

