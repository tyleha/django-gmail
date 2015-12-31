import sys

from imaplib import IMAP4_SSL
from datetime import date,timedelta,datetime
from email.utils import parsedate, parsedate_tz
from pylab import plot_date,show,xticks,date2num
from pylab import figure

import numpy as np

from gmail import *
import helpers
import math

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
import django


def marker_size(num_points):
    return 1./(1+ math.exp( (num_points-2700)/500))*6 +6


def load_and_plot_diurnal(address, password, daysback):
	address=address+'@gmail.com'
	#print address, password
	#Customizing Variables

	### HOW FAR BACK? ###
	daysback = int(daysback)
	notsince = 0
	since = (date.today() - timedelta(daysback)).strftime("%d-%b-%Y")
	before = (date.today() - timedelta(notsince)).strftime("%d-%b-%Y")

	SEARCH = '(SENTSINCE {si} SENTBEFORE {bf})'.format(si=since, bf=before)
	BODY = '(BODY.PEEK[TEXT])'
	ALL_HEADERS = '(BODY.PEEK[HEADER.FIELDS (DATE TO CC FROM SUBJECT)])'
	DATE = '(BODY.PEEK[HEADER.FIELDS (DATE)])'

	tyler = GmailAccount(username=address,password=password)
	out = tyler.login()



	#LOAD GMAIL EMAILS
	received = tyler.load_parse_query(SEARCH, ALL_HEADERS, 'inbox')
	#print 'loaded received...'
	sent = tyler.load_parse_query(SEARCH, ALL_HEADERS, '[Gmail]/Sent Mail')
	#print 'loaded received and sent mail!'

	xr, yr = diurnalCompute(received)
	xs, ys = diurnalCompute(sent)

	fig=Figure(figsize=(14,8))
	ax=fig.add_subplot(111)

	p1, = ax.plot_date(xr, yr, '.', alpha=0.5, color='b', markersize=marker_size(len(xr)))
	p2, = ax.plot_date(xs, ys, '.', alpha=0.7, color='r', markersize=marker_size(len(xr)))
	fig.autofmt_xdate()

	fig.legend((p1, p2,), ('Received','Sent'), 'upper center', numpoints=1, markerscale=4, fancybox=True)
	ax.set_xlabel("Specific Date")
	ax.set_ylabel("Time Of Day")

	fig.tight_layout(pad=2)
	#legend(('Received','Sent'), numpoints=1)
	#ax.title("Received data for %s las %s days"%(address, str(daysback)))

	#ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))


	'''
	fig = figure()
	plot_date(xr, yr, '.', alpha=0.7, color='b', markersize=marker_size(len(xr)))
	#plot_date(xs, ys, '.', alpha=0.7, color='r', markersize=marker_size(len(xs)))
	legend(('Received','Sent'), numpoints=1)
	out = plt.setp(plt.xticks()[1], rotation=30)
	'''


	canvas=FigureCanvas(fig)
	response=django.http.HttpResponse(content_type='image/png')
	canvas.print_png(response)

	return response


	'''
	figure()
	subplot(211)
	plot_date(xr, yr, '.', alpha=0.7, color='b')
	title('Received Mail')

	subplot(212)
	plot_date(xs, ys, '.', alpha=0.7, color='r', markersize=7)
	title('Sent Mail')
	xlabel('Date')
	ylabel('Time of Day')
	out = plt.setp(plt.xticks()[1], rotation=30)
	'''


