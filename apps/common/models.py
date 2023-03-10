from django.db import models
from django.utils.translation import gettext as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    pass