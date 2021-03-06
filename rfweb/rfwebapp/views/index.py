from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.middleware.gzip import GZipMiddleware

gzip_middleware = GZipMiddleware()

from rfweb.rfwebapp.models import Suite
from search import SearchForm
import sys

def index(request):
    def _raw(request):
        suites = Suite.objects.all().order_by('name')
        return render_to_response('index.html', 
                {'suites': suites, 'form': SearchForm()}, context_instance=RequestContext(request))
    response = _raw(request)
    return gzip_middleware.process_response(request, response)
    return index

