'''
Views for Dr Suess signup newsletter app
'''

from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext

from whomail import forms

def index(request):
	'''Signup newsletter view used to validate an email address and add to DB.
	'''

	context =  dict()

	if request.method == 'POST':
		form=forms.SubscriberForm(request.POST)
		if form.is_valid():
			form.save()
			context['success'] = True

		else:
			context['form_errors'] = form.errors

	# Always send a new form
	context['form'] = forms.SubscriberForm()

	return render_to_response('index.html',
							  context,
							  context_instance=RequestContext(request)
	)