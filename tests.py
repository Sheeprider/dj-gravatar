from urlparse import urlparse, parse_qsl
import hashlib
import unittest

from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    ROOT_URLCONF='gravatar.urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'gravatar',))

from django.shortcuts import RequestContext
from django.template import Template, TemplateSyntaxError
from django.test import RequestFactory


class GravatarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = RequestFactory().get('/fake/path')
        cls.c = RequestContext(cls.r)
        cls.email = 'email@domain.com'
        cls.c.update({'email': cls.email})

    def test_gravatar_default_params(self):
        tpl = Template("{% load gravatar %}{% gravatar email %}")
        url = urlparse(tpl.render(self.c))
        qs = parse_qsl(url.query)

        self.assertEqual(url.scheme, '')
        self.assertEqual(url.netloc, 'www.gravatar.com')
        self.assertEqual(url.path, '/avatar/%s' % hashlib.md5(self.email.encode('utf-8')).hexdigest())
        self.assertIn((u's', u'55'), qs)
        self.assertIn((u'r', u'pg'), qs)

    def test_gravatar_custom_params(self):
        default_image = u"http://domain.com/image.png"
        self.c.update({'default_image': default_image})

        tpl_with_size = Template("{% load gravatar %}{% gravatar email 40 'g' default_image %}")
        url = urlparse(tpl_with_size.render(self.c))
        qs = parse_qsl(url.query)

        self.assertIn((u's', u'40'), qs)
        self.assertIn((u'r', u'g'), qs)
        self.assertIn((u'd', default_image), qs)

    def test_gravatar_invalid_params(self):
        self.assertRaises(TemplateSyntaxError, Template, "{% load gravatar %}{% gravatar %}")
        self.assertRaises(TemplateSyntaxError, Template, "{% load gravatar %}{% gravatar 'email' 40 other unknown args %}")
        self.assertRaises(TemplateSyntaxError, Template, "{% gravatar email %}")


if __name__ == '__main__':
    unittest.main()
