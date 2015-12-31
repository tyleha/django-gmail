gmail-stats
===========

*Producing useful and enlightening metrics for analyzing your email*


## Overview
Leveraging the power of numpy and matplotlib with the Django framework, the intention of gmail-stats is to build a website to analyze the massive amount of human data contained in an email IMAP archive. Email serves as our daily diary of activity, business, friends and family - all logged for posterity in our gmail somewhere. But how to say something useful about that trove of data? How do we mine it? 

The idea for gmail-stats came from [Stephen Wolfram's blog](http://blog.stephenwolfram.com/2012/03/the-personal-analytics-of-my-life/) in March 2012. Wolfram has meticulously logged pretty much any metric you can think of relating to his daily life, and the kind of broad truths he is able to glean from that data is truly amazing. I was inspired to do the same, but probably just form my email (I don't feel like logging every phone call, dinner, or stride I take).

## Goals
1.  Use Python whenever possible
2.  Interface with a Gmail account to provide access to email headers over any time span
3.  Provide a number of ways to slice and dice email data:
    -  Diurnal plots of each email sent/received
    -  Histograms of frequently contacted, frequently responded
    -  Most active time periods (week, month, year, custom)
    -  Area plot of contact frequency
    -  Domain contact frequency histogram
4.  Allow users to interact through the site using Google auth (OAuth) and save custom edit many plots to their liking
5.  Allow users to save custom plots for later access/comparison

## Outcomes
1.  Implemented the Gmail header fetching/parsing alsmost no problem. I have extensive experience with numpy/matplotlib, so got my graphs up and running quickly.
2.  When fiddling with Django, had to really go back through lecture notes and carefully understand the relationship between views/models/urls. I got it now. One issue I had was how to pass variables into views through the template...got it now, but took a bit of time.
3.  Got matplotlib plots to display as PNGs. Can't use Matplotlib's awesome tkinter dynamic plotting abilities in webpages though. Need javascripting.

## Planned Features and Shortcomings
1.  OAuth login. Nobody will (or should) trust a site that asks for your google username and password. 
2.  Expedite gmail fetching using python threading
3.  Store gmail headers locally for a time to allow users to build many different graphs without constantly re-fetching gmail data
4.  Javascript plotting of data instead of matlab. 
5.  User customization of graphs in real-time (zoom, custom date ranges, color schemes)
6.  Expand to other IMAP domains (yahoo, hotmail, etc)
7.  Produce front page examples of what the plots should look like so that non-gmail users (or just prospective users) can get an idea of what the site can do
8.  Save generated images in Postgre for later access
9.  Keep bootstrap-ifying the place! Colors! Dropdown navs! Tables! Sidebars!
