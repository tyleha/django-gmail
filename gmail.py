# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from imaplib import IMAP4_SSL
from datetime import date,timedelta,datetime
from time import mktime
from email.utils import parsedate, parsedate_tz
import email
from pylab import plot_date,show,xticks,date2num
from pylab import figure,hist,num2date
from matplotlib.dates import DateFormatter

from operator import itemgetter
from email.parser import HeaderParser
from pylab import plot_date

# <codecell>

class GmailAccount(object):
    def __init__(self, username=None, password=None, folder=None):
        self.username = username
        self.password = password
        self.folder = folder
        
    def login(self):
        self.conn = IMAP4_SSL('imap.gmail.com')
        response = self.conn.login(self.username, self.password)
        return response
    
    def search(self, query, folder=None, readonly=False):
        ff = self.folder if self.folder else folder
        self.conn.select(ff, readonly)
        resp, data = self.conn.uid('search', None, query)
        return data
    
    def fetch(self, ids, query):
        resp, data = self.conn.uid('fetch', ids[0].replace(' ',','), query)
        return data
    
    def fetch_and_parse(self, ids, query):
        data = self.fetch(ids, query)
        parser = HeaderParser()
        emails = []
        
        for email in data:
            if len(email) < 2: continue
            emails.append(parser.parsestr(email[1])  )
            
        return emails
    
    def load_parse_query(self, search_query, fetch_query, folder=None, readonly=False):
        '''Perform search and fetch on an imap Gmail account. After fetching relevant info
from fetch query, parse into a dict-like email object, return list of emails.'''
        ids = self.search(search_query, folder, readonly)
        data= self.fetch_and_parse(ids, fetch_query)
        return data

# <codecell>

def get_all_recips(parsed):
    
    if parsed['To'] and parsed['cc']:
        return parsed['To']+', '+parsed['cc']
    elif parsed['To']:
        return parsed['To']
    elif parsed['cc']:
        return parsed['cc']
    else: return None
    
def grab_email(string):
    '''assumes format 'First Last <some@thing.com>' '''
    return string.split('<')[-1][:-1]

# <codecell>

def parse_from(email_dict, metadata):
    address = metadata.get('From').split('<')[-1][:-1] 
    if address == None: return email_dict
    email_dict.setdefault(address, []).append(metadata)
    
def parse_to(email_dict, metadata):
    addressees = get_all_recips(metadata)
    if addressees == None: return email_dict
    #for each recipient in either the to or cc field:
    for to in addressees.split(','):
        email_dict.setdefault(grab_email(to), []).append(metadata)
    return email_dict

# <codecell>

def parse_emails(fromorto, listofemails):
    '''Input: list of emails parsed by HeaderParser, must contain To, From, or CC. 
Returns a dictionary of email address with key of a HeaderParser object that
contains all fields in the header, in a dictionary-like object.'''
    email_dict = {}
    
    for email in listofemails:
        try:
            #Parse the email from the address line 'Tyler <tlh@what.com>'
            if fromorto.lower() == 'from':
                email_dict = parse_from(email_dict, email)
            elif fromorto.lower() == 'to':
                email_dict = parse_to(email_dict, email)
            else: raise ValueError, 'Please decide if should be organized by to or from.'
            
        except Exception as e:
            print email
            print e
        
    return email_dict
        

# <codecell>

def diurnalCompute(emails, PLOT=False):
    '''Diurnal plot of all emails, with years on x axis and time of day on y axis.
Input must be a list of emails of class HeaderParser, with the key 'Date' containing
the date.
Outputs the (year,month,day), (Hour, minute second) '''
    xday = []
    ytime = []
    #for i in range(len(headers)): 
    for email in emails:
        try:
            date = email['Date']
            _temp = date.split(',')
            _temp[0] = _temp[0].strip()
            email = ', '.join(_temp)
            
            timestamp = mktime(parsedate(date))
            mailstamp = datetime.fromtimestamp(timestamp)
            xday.append(mailstamp)
            # Time the email is arrived
            # Note that years, month and day are not important here.
            y = datetime(2010,10,14, 
                mailstamp.hour, mailstamp.minute, mailstamp.second)
            ytime.append(y)
        
        except Exception as e:
            print email
            print e
            #return headers[i]
    #figure(figsize=(20,8))
    #plot_date(xday,ytime,'.',alpha=.7)
    #xticks(rotation=30)
    if PLOT:
        diurnalPlot(xday, ytime)
        
    return xday, ytime

# <codecell>

def diurnalPlot(x, y, color='b'):
    figure()
    plot_date(x, y, '.', alpha=.7, color=color)

# <codecell>

def dailyDistributioPlot(ytime):
    """ draw the histogram of the daily distribution """
    # converting dates to numbers
    numtime = [date2num(t) for t in ytime] 
    # plotting the histogram
    ax = figure().gca()
    _, _, patches = hist(numtime, bins=24,alpha=.5)
    # adding the labels for the x axis
    tks = [num2date(p.get_x()) for p in patches] 
    xticks(tks,rotation=75)
    # formatting the dates on the x axis
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

# <codecell>


# <codecell>


