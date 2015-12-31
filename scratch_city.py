# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%load_ext autoreload
%autoreload 2

# <codecell>

import sys
sys.path.append('C:\\Users\\Tyler\\.ipython\\gmail-stats')
from imaplib import IMAP4_SSL
from datetime import date,timedelta,datetime
from email.utils import parsedate, parsedate_tz
from pylab import plot_date,show,xticks,date2num
from pylab import figure
import matplotlib.pyplot as plt
import numpy as np

from gmail import *
import helpers
import math

# <codecell>

def marker_size(num_points):
    return 1./(1+ math.exp( (num_points-2700)/500))*6 +6

# <codecell>

#Customizing Variables

### HOW FAR BACK? ###
daysback = 2300
notsince = 0
since = (date.today() - timedelta(daysback)).strftime("%d-%b-%Y")
before = (date.today() - timedelta(notsince)).strftime("%d-%b-%Y")

SEARCH = '(SENTSINCE {si} SENTBEFORE {bf})'.format(si=since, bf=before)
BODY = '(BODY.PEEK[TEXT])'
ALL_HEADERS = '(BODY.PEEK[HEADER.FIELDS (DATE TO CC FROM SUBJECT)])'
DATE = '(BODY.PEEK[HEADER.FIELDS (DATE)])'

tyler = GmailAccount(username='tyleha@gmail.com',password='')
out = tyler.login()
work = GmailAccount(username='thsimulab@gmail.com', password='')
out = work.login()

# <codecell>

#LOAD GMAIL EMAILS
received = tyler.load_parse_query(SEARCH, ALL_HEADERS, 'inbox')
sent = tyler.load_parse_query(SEARCH, ALL_HEADERS, '[Gmail]/Sent Mail')
#LOAD WORK EMAILS
received.extend(work.load_parse_query(SEARCH, ALL_HEADERS, 'inbox'))
sent.extend(work.load_parse_query(SEARCH, ALL_HEADERS, '[Gmail]/Sent Mail'))

#received = helpers.load_pickle('tyler_received_Nov06')
#sent = helpers.load_pickle('tyler_sent_Nov06')

xr, yr = diurnalCompute(received)
xs, ys = diurnalCompute(sent)

# <codecell>

figure()
plot_date(xr, yr, '.', alpha=0.7, color='b', markersize=marker_size(len(xr)))
plot_date(xs, ys, '.', alpha=0.7, color='r', markersize=marker_size(len(xs)))
legend(('Received','Sent'), numpoints=1)
out = plt.setp(plt.xticks()[1], rotation=30)

# <codecell>

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

# <headingcell level=2>

# Last thing I was working on was plotting sent emails next to received by top 20 sender

# <codecell>

'''
emails_from = gmail.parse_emails('from', data_sent)

number_emails = []
for address, emails in emails_from.iteritems():
    number_emails.append((address, len(emails)))

number_emails = sorted(number_emails, key=itemgetter(1), reverse=True)
print number_emails[:10]
'''

# <codecell>

'''
fig = plt.figure()
ax = plt.subplot(111)

senders = [x[1] for x in number_emails[:20]]
ind = np.arange(len(senders))
rects = ax.bar(ind, senders, width=0.35, color='b')
rects2 = ax.bar(ind+0.35, senders, width=0.35, color='g')
'''

# <codecell>


# <codecell>

figure(figsize=(20,8))
plot_date(xd_r,yt_r,'.',alpha=.7, color='b')
figure(figsize=(20,8))
plot_date(xd_s,yt_s,'.',alpha=.7, color='r')
figure(figsize=(20,8))
plot_date(xd_r,yt_r,'.',alpha=.7, color='b')
plot_date(xd_s,yt_s,'.',alpha=.7, color='r')
xticks(rotation=30)

# <codecell>


