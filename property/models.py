from django.db import models
from wagtail.models import Page, Orderable
from django.contrib.postgres.fields import ArrayField
from wagtail.fields import RichTextField
from wagtail.admin.panels import MultiFieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class PropertyIndexPage(Page):
    hero_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.PROTECT, related_name="+"
    )
    hero_text = models.CharField(max_length=120)

    content_panels = Page.content_panels + ["hero_image", "hero_text"]


class PropertyPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "PropertyPage", on_delete=models.CASCADE, related_name="tagged_property"
    )


class PropertyPage(Page):
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    lga = models.CharField(max_length=50)
    description = RichTextField()
    benefits = ArrayField(models.CharField(max_length=150), default=list)
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


class PropertyImageGallery(Orderable):
    page = ParentalKey(
        PropertyPage, on_delete=models.PROTECT, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.PROTECT, related_name="+"
    )

    panels = ["image"]
