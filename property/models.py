from django.db import models
from wagtail.models import Page, Orderable
from wagtail.blocks import CharBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
import os


class PropertyPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "PropertyPage", on_delete=models.CASCADE, related_name="tagged_property"
    )


class PropertyPage(Page):
    parent_page_types = ["home.HomePage"]

    address = models.CharField(max_length=200)
    country = models.CharField(max_length=180)
    state = models.CharField(max_length=160)
    district = models.CharField(max_length=160)
    description = RichTextField()
    benefits = StreamField([("benefit", CharBlock())], blank=True)
    type = models.CharField(max_length=50)
    offer = models.CharField(max_length=50)
    price = models.BigIntegerField()
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    tags = ClusterTaggableManager(through=PropertyPageTag, blank=True)

    def main_image(self):
        gallery_image = self.gallery_images.first()
        if gallery_image:
            return gallery_image.image

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["whatsapp_link"] = os.getenv("WHATSAPP_LINK")
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                "gallery_images",
                "description",
                "benefits",
                "type",
                "bedrooms",
                "bathrooms",
                "size",
            ],
            heading="Property details",
        ),
        MultiFieldPanel(
            ["address", "country", "state", "district"], heading="Property location"
        ),
        MultiFieldPanel(["offer", "price"], heading="Property pricing"),
        FieldPanel(
            "tags", help_text="Enter tags related to this property for easy search"
        ),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("description"),
        index.SearchField("benefits"),
    ]


class PropertyImageGallery(Orderable):
    page = ParentalKey(
        PropertyPage, on_delete=models.PROTECT, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.PROTECT, related_name="+"
    )

    panels = ["image"]
