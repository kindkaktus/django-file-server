# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import logging

# from fileprovider.utils import sendfile
from sendfile import sendfile
from models import Document
from forms import DocumentForm

logger = logging.getLogger(__name__)


@login_required
def list(request):
    logger.info("Handling login request {}".format(request))
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info("Handling upload of {}".format(request.FILES['docfile']))
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


@login_required
def download_media(request, file_id):
    logger.info("Handling media download request {}. File id {}".format(request, file_id))
    file = get_object_or_404(Document, pk=file_id)
    logger.info('Db lookup result: {}'.format(file.docfile.url))
    # return sendfile(file.docfile.url)
    return sendfile(request, file.docfile.url)
    #@todo download as attachment. see also https://github.com/johnsensible/django-sendfile/blob/master/sendfile/__init__.py
    # https://pypi.python.org/pypi/django-sendfile/
    # sudo pip install django-sendfile
    # Db lookup result: /documents/2018/02/27/plan_8PLhWE2.txt"
    # got 2018-02-28 05:18:34,863 django.request <39455> [WARNING] "get_response() Not Found: /list/9/"
