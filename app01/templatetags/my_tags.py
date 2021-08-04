
from django import template

register = template.Library()


@register.filter
def has_permisstion(user, perm):
    if user:
        return user.has_perm(perm)
    return False