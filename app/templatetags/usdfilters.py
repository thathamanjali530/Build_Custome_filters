from django import template
register=template.Library()

def swap(value):
    return value.swapcase()


def remove(value,arg):
    return value.replace(arg:'h')

register.filter('swap',swap)
register.filter('remove',remove)

