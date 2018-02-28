# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    # files will be uploaded under MEDIA_ROOT
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
