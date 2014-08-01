from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from demoapp.forms import ContactForm
from demoapp.tasks import sendmail, compare, exito, carulla, oxxo, olimpica, jumbo
from celery import chord
from django.template.response import TemplateResponse

class HomePageView(TemplateView):
    template_name = 'demoapp/index.html'
    def dispatch(self, *args, **kwargs):
        return super(HomePageView, self).dispatch(*args, **kwargs)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            sendmail.delay(subject,email,message)
            return HttpResponse('Thanks!!')
    else:
        form = ContactForm()
    return render(request, 'demoapp/contact_form.html', {'form': form})

def quote(request):
    callback = compare.s()
    header = [exito.s(), carulla.s(), oxxo.s(), olimpica.s(), jumbo.s( )]
    result = chord(header)(callback)
    data = result.get()
    return HttpResponse("Best price: " + str(data['value']) + " from: " + data['provider'])
    
def quotertc(request):
    callback = compare.s()
    header = [exito.s(), carulla.s(), oxxo.s(), olimpica.s(), jumbo.s( )]
    result = chord(header)(callback)
    return render(request, 'demoapp/quote.html', locals())
