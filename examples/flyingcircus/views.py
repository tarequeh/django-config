from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def index(request):
    return render_to_response('flyingcircus/index.html', {
        'settings': settings,
        }, context_instance=RequestContext(request))
