from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from index.form import ContactForm
from products.models import Product, Discount


# Create your views here.
def index(request):
    context = {
        'title': "Famms",
        'products': Product.objects.all()[:8],
        'discounts': Discount.objects.all()[:2]
    }
    return render(request, 'index.html', context)


def contact(request):
    context={}
    if request.method =='POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           send_message(form.cleaned_data['name'],
                        form.cleaned_data['email'],
                        form.cleaned_data['subject'],
                        form.cleaned_data['message'])
           context = {'success':1}
    else:
        form = ContactForm()
    context['form'] = form


    return render(request, 'contact.html', context=context)


def send_message(name, email, subject, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name':name, 'email': email, 'subject': subject, 'message':message}
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content,from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
