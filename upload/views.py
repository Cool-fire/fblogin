# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse

from .models import Document
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required

@login_required()
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(user = request.user.username,docfile = request.FILES['docfile'])
            newdoc.save()


            # Redirect to the document list after POST
            return HttpResponse('succesfully uploaded')
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'upload/upload.html',
        {'documents': documents, 'form': form},

    )
