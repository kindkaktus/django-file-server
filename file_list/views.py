# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import logging

from fileprovider.utils import sendfile
from models import Document
from forms import DocumentForm

logger = logging.getLogger(__name__)


@login_required(login_url="/login/")
def list(request):
    logger.info("Handling login request")
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )


@login_required(login_url="/login/")
def download_media(request, file_id):
    logger.info("Handling media request")
    file = get_object_or_404(Document, pk=file_id)
    return sendfile(file.path)
