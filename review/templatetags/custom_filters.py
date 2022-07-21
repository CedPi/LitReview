from django import template

register = template.Library()


@register.filter(name="num")
def num(value):
    return range(abs(value))


@register.filter(name="objtype")
def objtype(value):
    return type(value).__name__
