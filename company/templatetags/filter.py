from django import template

register = template.Library()

@register.filter(name='defineColorList')
def defineColorList(value):
    if value % 2 == 0:
        return True
    else:
        return False