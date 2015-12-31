from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from graphs.models import EmailAccount
import graphs.plots as plots

def frontpage(request):
	return render_to_response('frontpage.html', context_instance=RequestContext(request))

def credentials(request):
	return render_to_response('credential_form.html', context_instance=RequestContext(request))

def diurnal(request):

	cred = EmailAccount()
	cred.address = request.POST.get('email')
	cred.password = request.POST.get('pw')
	daysback = request.POST.get('daysback')

	return render_to_response('diurnal.html', {'email':cred, 'daysback':daysback}, 
							context_instance=RequestContext(request))


def diurnal_plot(request, address=None, password=None, daysback=60):
	return plots.load_and_plot_diurnal(address, password, daysback)


def argpassing(request, property):
	return HttpResponse(property)

def simple(request, address=None, password=None):
	#print request.PATH

	import random
	import django
	import datetime

	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	from matplotlib.figure import Figure
	from matplotlib.dates import DateFormatter

	print address, password

	fig=Figure(figsize=(20,12))
	ax=fig.add_subplot(111)
	x=[]
	y=[]
	now=datetime.datetime.now()
	delta=datetime.timedelta(days=1)
	for i in range(10):
		x.append(now)
		now+=delta
		y.append(random.randint(0, 1000))
	ax.plot_date(x, y, '-')
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()

	canvas=FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response




def current_datetime(request):
	now = datetime.datetime.now()
	#html = "<html><body>The time is: %s.</body></html>"%now
	return render_to_response('current_datetime.html', {'current_date': now}, 
				context_instance=RequestContext(request))


#############################################################
def stub(request, *args, **kwargs):
    return HttpResponse('stub view', mimetype="text/plain")



def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	later = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>The current time plus %s hours is: %s.</body></html>"%(offset, later)
	return HttpResponse(html)	

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)