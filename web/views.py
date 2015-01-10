from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('web/home.html',
                              context_instance=context)