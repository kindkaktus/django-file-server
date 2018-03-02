# -*- coding: utf-8 -*-
from django.db import models


class Deliverable(models.Model):
    # files will be uploaded under MEDIA_ROOT
    docfile = models.FileField(upload_to='deliverables/%Y/%m/%d')
