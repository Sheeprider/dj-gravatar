# -*- coding: utf-8 -*-
import hashlib
import urllib

try:
    from django import settings
except:
    settings = {}

from django import template

register = template.Library()


@register.simple_tag
def gravatar(email, size=None, rating=None, default=None):
    """
    Template Syntax::

        {% gravatar email [size] %}

    Example usage::

        {% gravatar email 40 %}
    """
    params = {
        's': settings.get('GRAVATAR_SIZE', 55),
        'r': settings.get('GRAVATAR_RATING', 'pg'),
    }

    default_image = settings.get('GRAVATAR_DEFAULT')
    if default_image:
        params.updade(d=default_image)

    if size:
        params.update(s=int(size))
    if rating:
        params.update(r=unicode(rating))
    if default:
        params.update(d=unicode(default))

    url = "//www.gravatar.com/avatar/{0}?{1}"
    return url.format(hashlib.md5(email.encode('utf-8')).hexdigest(), urllib.urlencode(params))
