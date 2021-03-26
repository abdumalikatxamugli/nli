from django import template
from sales.models import *
register = template.Library()


@register.simple_tag
def get_product_types():
    return list(Product.objects.all())
