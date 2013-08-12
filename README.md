#Dj-Gravatar

Django-Gravatar contains a templatetag to include a gravatar url in your templates.

##Exemple

	{% load gravatar %}
	<img src="{% gravatar 'email@domain.com' %}">

	{# Advanced usage : #}
	<img src="{% gravatar 'email@domain.com' 40 'g' 'http://domain.com/default/image.png' %}">

##License

MIT, see LICENSE.

##Installation

	pip install -e git+git@github.com:Sheeprider/dj-gravatar.git@1.1#egg=Gravatar
