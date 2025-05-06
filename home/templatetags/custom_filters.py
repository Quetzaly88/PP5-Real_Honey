from django import template

register = template.Library()


@register.filter(name='secure_url')
def secure_url(value):
    if value:
        return value.replace('http://', 'https://')
    return value
