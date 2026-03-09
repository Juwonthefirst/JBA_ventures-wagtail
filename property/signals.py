from django.db.models.signals import post_delete
from django.dispatch import receiver
from property.models import PropertyImageGallery


@receiver(post_delete, sender=PropertyImageGallery)
def delete_extra_media_after_row_delete(sender, instance, **kwargs):
    if instance:
        instance.image.delete(save=False)
