# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
import logging

from sendfile import sendfile
from models import Deliverable
from forms import DocumentForm
import os

logger = logging.getLogger(__name__)


@login_required
def list(request):
    logger.debug("Handling file list request {}".format(request))
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info("Handling upload of {}".format(request.FILES['docfile']))
            newdoc = Deliverable(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load deliverables for the list page
    deliverables = Deliverable.objects.all()

    # Render list page with the deliverables and the form
    return render(
        request,
        'list.html',
        {'deliverables': deliverables, 'form': form}
    )


@login_required
def download_media(request, file_id):
    logger.debug("Handling media download request {}. File id {}".format(request, file_id))
    file = get_object_or_404(Deliverable, pk=file_id)
    full_path = os.path.join(settings.SENDFILE_ROOT, file.docfile.name)
    logger.info('Downloading file {}'.format(full_path))
    return sendfile(request, full_path)
