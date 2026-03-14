from django.db import models
from django.http.request import HttpRequest
from wagtail.models import Page

from property.models import PropertyPage
from search.views import search_in_base_manager


class HomePage(Page):
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )
    hero_text = models.CharField(max_length=120)

    content_panels = Page.content_panels + ["hero_image", "hero_text"]

    def get_context(self, request: HttpRequest, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        filter_query: dict[str, str] = {}
        property_pages = PropertyPage.objects.live()
        # add filtering for fields from query param here
        search_query, search_results = search_in_base_manager(request, property_pages)
        context["search_results"] = search_results
        context["search_query"] = search_query
        context["property_pages"] = property_pages
        return context
