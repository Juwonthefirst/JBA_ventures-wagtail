import django_filters
from django.db import models
from property.models import PropertyPage


class PropertyQueryFilter(django_filters.FilterSet):
    price_base = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_roof = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    size_base = django_filters.NumberFilter(field_name="size", lookup_expr="gte")
    size_roof = django_filters.NumberFilter(field_name="size", lookup_expr="lte")

    class Meta:
        model = PropertyPage
        fields = ["state", "district", "type", "offer"]
