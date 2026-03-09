from django.db import models
from wagtail.models import Page, Orderable
from wagtail.blocks import CharBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import MultiFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class PropertyPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "PropertyPage", on_delete=models.CASCADE, related_name="tagged_property"
    )


class PropertyPage(Page):
    parent_page_types = ["home.HomePage"]

    address = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    lga = models.CharField(max_length=50)
    description = RichTextField()
    benefits = StreamField([("benefit", CharBlock())], blank=True)
    type = models.CharField(max_length=50)
    offer = models.CharField(max_length=50)
    price = models.BigIntegerField()
    tags = ClusterTaggableManager(through=PropertyPageTag, blank=True)

    def main_image(self):
        gallery_image = self.gallery_images.first()
        if gallery_image:
            return gallery_image.image

    content_panels = Page.content_panels + [
        MultiFieldPanel(["address", "state", "lga"], heading="Property location"),
        MultiFieldPanel(
            ["description", "benefits", "type"], heading="Property details"
        ),
        MultiFieldPanel(["offer", "price"], heading="Property pricing"),
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
