from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
# Create your views here.

# TODO: Kan nog niet checken of de content etc daadwerkelijk aankomt
## contact us is nagebouwd uit de hellowebapp.com 
#https://hellowebapp.com/news/tutorial-setting-up-a-contact-form-with-django/
# http://stackoverflow.com/questions/28400943/python-django-e-mail-form-example
# 
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_subject = request.POST.get('contact_subject', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('contact/contact_template.txt')
            context = Context({'contact_name': contact_name,'contact_email': contact_email,'contact_subject' : contact_subject,'form_content': form_content,})
            content = template.render(context)

            # TODO: CHANGE WEBSITE AND E-MAIL
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['wittebroodalex@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/contact/')
    
    return render(request, 'contact/contact.html', {
        'form': form_class,
    })

## ALTERNATIEVE MANIER?? 
 # if request.method == 'GET':
 #        form = ContactForm()
 #    else:
 #        form = ContactForm(request.POST)
 #        if form.is_valid():
 #    		name = form.cleaned_data['contact_name']
 #        	subject = form.cleaned_data['contact_subject']
 #        	from_email = form.cleaned_data['contact_email']
 #        	message = form.cleaned_data['content']
 #        	try:
 #        	    send_mail(name, subject, message, from_email, ['wittebroodalex@gmail.com'])
 #        	except BadHeaderError:
 #        	    return HttpResponse('Invalid header found.')
 #        	return redirect('thanks')
	# return render(request, "contact/contact.html", {'form': form})

