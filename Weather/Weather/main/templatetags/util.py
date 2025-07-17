from django import template

register = template.Library()

@register.filter
def get_type(value):
    return str(type(value)).find('dict')