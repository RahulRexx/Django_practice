from django import template

register = template.Library()

@register.filter(name='cut') # this is done using decorators
def cut(value,args):
    return value.replace(args,"")


# register.filter('cut',cut)   # this is done using function