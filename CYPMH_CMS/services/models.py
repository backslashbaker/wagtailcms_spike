# Create your models here.
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel 

from wagtail.api import APIField

class Services(Page):
    services_title = models.CharField(
        max_length=70,
        blank=True, 
        help_text='Title to display on webpage'
    )
    services_description =  models.TextField(
        blank=True, 
        help_text='Description written on the card'
    )
    services_url =  models.URLField(
        blank=True, 
        help_text='url to external website'
    )
    content_panels = Page.content_panels + [
        FieldPanel("services_title"),
        FieldPanel("services_description"),
        FieldPanel("services_url")
        ]
    api_fields = [
        APIField("services_title"),
        APIField("services_description"),
        APIField("services_url")
    ]
