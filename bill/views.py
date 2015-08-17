from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Person
from .models import Bill
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BillForm
from django.views.decorators.cache import cache_page
import StringIO
from cgi import escape
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

class IndexView(generic.ListView):
    template_name = 'bill/index.html'
    context_object_name = 'flat_user_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Person.objects.all()

class DetailView(generic.DetailView):
    model = Person
    template_name = 'bill/detail.html'

import cStringIO as StringIO
import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request, bill_id):
    #Retrieve data or whatever you need
    try:
        billObj = get_object_or_404(Bill, pk=bill_id)
    except:
        return HttpResponse('Bill id is<pre>%s</pre>' % escape(bill_id))
    return render_to_pdf(
            'bill/pdf_view.html',
            {
            'pagesize':'A4',
            'bill': billObj,
            })

def mail_view(request):
    plaintext = get_template('email.txt')
    htmly     = get_template('email.html')

    d = Context({ 'username': username })

    subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BillForm()

    return render(request, 'bill/name.html', {'form': form})

def printBill(request, person_id):
    try:
        flat_user = Person.objects.get(pk=person_id)
    except:
        flat_user= None

    try:
        bill = get_object_or_404(Bill, user=user)
    except:
        bill = None
    if bill == None:
        bill = Bill(user=flat_user)

	bill.due_date = "2015-08-10"
	bill.month = "July"
    bill.statement_date = "2015-08-09"
    bill.sinking_fund = request.POST['sink']
    bill.repair_and_maintainance = request.POST['repair']
    bill.water_charges = request.POST['water_fund']
    bill.electricity_charges = request.POST['electricity_charge']
    bill.service_charges= request.POST['service_charge']
    bill.interest = request.POST['interest']
    bill.penalty = request.POST['penalty']
    bill.adjustments = request.POST['adjustments']
    bill.unpaid_due = 0
    bill.total_charges = request.POST['total']
    bill.payble_amt = request.POST['gross']
    bill.save()

    return render(request, 'bill/print.html', {'bill': bill})
