from django.db import models

from wagtail.models import Page


class HomePage(Page):
    hero_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.PROTECT, related_name="+"
    )
    hero_text = models.CharField(max_length=120)

    content_panels = Page.content_panels + ["hero_image", "hero_text"]
