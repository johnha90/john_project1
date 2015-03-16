
#from django.http import HttpResponse
#from django.template import RequestContext, loader
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response, render, RequestContext
#from django.views.generic.base import TemplateView
from insert.models import Event,ExhibitorList
#from django.views.generic import ListView
#from forms import EventForm
#from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from .forms import abcForm
#from django.views.generic.edit import UpdateView
#from django.core.urlresolvers import reverse_lazy

#class updateEL(UpdateView)):
#	model=Event
#	fields=['name']

# Create your views here.
"""def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    template = loader.get_template('insert/index.html')
    context = RequestContext(request, {
        'latest_event_list': latest_event_list,
    })
    return HttpResponse(template.render(context))
"""

#def detail(request, event_id):
#    return HttpResponse("You're looking at event %s." % event_id)
"""
def hello(request):
	name="i am john"
	html="<html><body>Hi %s, this seems to have worked! </body></html>"%name

	return HttpResponse(html)

def hello_template(request):
	name="i am john john"
	t=get_template('template1.html')
	html=t.render(Context({'name':name}))
	return HttpResponse(html) 

def hello_template_simple(request):
	name="john john john"
	return render_to_response('template1.html',{'name':name})

class HelloTemplate(TemplateView):

	template_name='template2.html'

	def get_context_data(self, **kwargs):
		context=super(HelloTemplate,self).get_context_data(**kwargs)
		context['name']='Ah John'
		return context
"""

def event(request):
	return render_to_response('event.html',{'events':Event.objects.all(), 'exhibitor':ExhibitorList.objects.all()})
#def event(request,event_id=1):
#	return render_to_response('event.html'),{'event':Event.objects.get(id=event_id)}
def home(request):
	form = abcForm(request.POST or None)

	if form.is_valid():
		save_it=form.save(commit=False)
		save_it.save()

	return render_to_response("form.html",locals(),context_instance=RequestContext(request))

"""def input(request):
	if request.method=="POST":
		print request.POST.get("")


	return render_to_response('form.html',{event})
"""

"""class ListView(ListView):
	model=Event
	template_name='event.html'
	"""
"""
def create(request):
	if request.POST:
		form=EventForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/insert/all')

	else:
		form=EventForm()

	args={}
	args.update(csrf(request))
	args['form']=form
	return render_to_response('create_exhibitor.html',args)
	"""

"""def get_req(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = abcForm(request.POST or None)
        # check whether it's valid:
        		
        #print form
        #form.errors.as_data()
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ..self.
            # redirect to a new URL:
            
            event = form.cleaned_data['event']
            company = form.cleaned_data['company']
            zip_code = form.cleaned_data['zip_code']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            booth_no = form.cleaned_data['booth_no']
            hall_no = form.cleaned_data['hall_no']

            b=ExhibitorList(event=event,company=company,zip_code=zip_code,city=city,country=country,booth_no=booth_no,hall_no=hall_no)
            b.save()
			
			#save_it=form.save(commit=False)
			#save_it.save()
			save_it=form.save(commit=False)
			save_it.save()
        return render_to_response("form.html",locals(),context_instance=RequestContext(request))
  """


        

    # if a GET (or any other method) we'll create a blank form
    #else:
    #    form = abcForm()

   # return render(request, 'form.html', {'form':form})