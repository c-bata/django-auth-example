from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def user_profile(request):
    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('accounts/user_profile.html',
                              context_instance=context)
