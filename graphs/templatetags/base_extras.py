from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, urls):
	#if request.path in ( reverse(url) for url in urls.split() ):
	try:
		#print request.path
		#print reverse(urls)
		if reverse(urls) in request.path:# and request.path not '/':
			return "active"
	except Exception as e:
		print e
		#print 'urls: ' + repr(urls)
		#print 'Request was: ' + request
		#return ""

	return ""