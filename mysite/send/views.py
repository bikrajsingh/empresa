from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from .forms import ClientForm
from .models import Client
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
import ldap

from django_auth_ldap.config import LDAPSearch

# Create your views here.
def index(request):
    """if request.method == 'POST':
      message = request.POST['message']
      send_mail('ClientForm', message, settings.EMAIL_HOST_USER,['c41bsingh@gmail.com'], fail_silently=False)
    #email = EmailMessage('Subject', 'Bikrajsingh is ok', to=['c41bsingh@gmail.com'])
    #email.send()
    #ClientCreate(request, template_name= 'send/login.html')"""
    return render(request, 'send/index.html')
"""ldap_base = 'dc=preven, dc=local'
searchscope = ldap.SCOPE_SUBTREE
RetrieveAttr = ["mail", "givenname"]
query = "(cn=bikraj)"
result_id = con.search_s(ldap_base, searchscope, query, RetrieveAttr)

result =[entry for dn, entry in result_id if isinstance(entry, dict)]
print(result)
"""

def ClientCreate(request, template_name= 'send/login.html'):
    if request.method == 'GET':
      form = ClientForm(request.POST)
    else:
      form = ClientForm(request.POST)
      if form.is_valid():
        Nom = form.cleaned_data['Nom']
        oficina = form.cleaned_data['oficina']
        correu = form.cleaned_data['correu']
        missatge = form.cleaned_data['missatge']


        template = get_template('send/contact_form.txt')
        context = {
          'Nom' : Nom,
          'oficina': oficina,
          'correu': correu,
          'missatge': missatge,
        }
        content = template.render(context)
          #form.save()
        try:
          email = EmailMessage(
            "New contact form email",
            content,
            "Creative web" + '',
            ['c41bsingh@gmail.com'],
            reply_to=['c41bsingh.com'],
            headers={'Message-ID': 'foo'},
          )
          email.send()
          #message = request.POST['message']
          #send_mail('mysite', message, 'bikrajsingh@gmail.com', ['c41bsingh@gmail.com'])
        except BadHeaderError:
          return HttpResponse('INVALID')

        return redirect('hola')
    #form = ClientForm()
    return render(request, 'send/form.html', {'form': form})
