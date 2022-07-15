#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
from datetime import time
from datetime import datetime

import os
import sys


AUTHOR = 'Carolin Zöbelein'
SITENAME = "Carolin's Blog"
SITEURL = ''

SITEURL_SOCIAL = 'https://blog.carolin-zoebelein.de'

PATH = 'content'

#DATE_FORMATS = {	# TODO
#    'en': ('en_US','%a, %d %b %Y'),
#}

# ******
# Plugins
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['render_math', 'jinja2content'] # TODO: 'pelican_fontawesome', 'summary'
# ******
STATIC_PATHS = ['blog', 'pages', 'images', 'files']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'

PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


# TODO
# TODO: MathJax Mobile Responsive
# TODO: MathJax Definition, Theorem, .... environments
# TODO: Article References
# TODO: General Reference
#MATH_JAX = {'tex_extensions': ['color.js','mhchem.js']}
#MATH_JAX = {'tex_extensions': ['AMSmath.js','AMSsymbols.js','noErrors.js','noUndefined.js']}
#MATH_JAX = {'equation_numbering': 'AMS'}

MATH_JAX = {
	'equation_numbering': 'AMS'
#	'environments': {
#	  'braced': ['\\left\\{', '\\right\\}'],
#	  'ABC': ['(#1)(#2)(', ')', 2, 'X']
#	}
}


# TODO: favicon
# TODO: markdown config
# TODO: Warning Atom feed
# TODO: Dateformate
# TODO: locales
# TODO: index: avatar, newest article summary
# TODO: Size of key page code relative to normal text

# TODO: Fontawesome, Fork Awesome, contact page, q and a
# TODO: icontags
# TODO: osf, jupyter, python, julia, orcid, arxiv, google-scholar, tor-onion, tex, unity
# TODO: References
# TODO: index page: featured, blocks


TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en' # TODO: en_US

# Theme
THEME = 'themes/minimal-xy'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = u'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2016
MINIMALXY_CURRENT_YEAR = date.today().year

# Index introduction
INDEX_INTRO_IMAGE = '/images/computer-2930704_1280.jpg'

# Author
AUTHOR_INTRO = u'Math, CS and Random Stuff :)'
AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
#AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240' # TODO
AUTHOR_AVATAR = '/images/avatar.jpg' # TODO
AUTHOR_WEB = 'https://research.carolin-zoebelein.de'


# Services
#GOOGLE_ANALYTICS = 'UA-00000000-0'
#DISQUS_SITENAME = 'johndoe'


# PGP Keys
SIGNING_KEY = u'8F31 C7C6 E67E 9ACE 8E12 E2EF 0DE3 A4D3 BA87 2A8B'

# Social
#TODO: Crunchbase
SOCIAL = (
    ('twitter', 'https://twitter.com/SamdneyTweet'),
    ('github', 'https://github.com/Samdney'),
    ('linkedin', 'https://www.linkedin.com/in/carolin-zoebelein/'),
    ('youtube-play', 'https://www.youtube.com/channel/UChKn7j071KPz3QNYldPKH1g'),
    #('youtube', 'https://www.youtube.com/channel/UCqboFicvhrlnPi8eeTv1D1Q'), # art youtube
    ('superscript', 'https://research.carolin-zoebelein.de'),
    #('pencil', 'https://art.carolin-zoebelein.de'), # art website
)


# Menu
#MENUITEMS = (
#    ('Categories', '/' + CATEGORIES_SAVE_AS),
#    ('Archive', '/' + ARCHIVES_SAVE_AS),
#)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
	('Archives', '/archives.html'),
	('Categories', '/categories.html'),
	#('References', '/references.html'), # TODO
	('Contact', '/contact.html')
)


# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

#DEFAULT_PAGINATION = 1
PAGINATION_INDEX = 5

PAGINATED_TEMPLATES = {'index': 1, 'tag': 5, 'category': 5, 'author': 5}

#PAGINATION_PATTERNS = (
#	 (1, 'index{number}.html', '{base_name}/index{number}.html'),
#	 (2, 'index{number}.html', '{base_name}/index{number}.html'),
#	 (3, 'index{number}.html', '{base_name}/index{number}.html'),
#	 (4, 'index{number}.html', '{base_name}/index{number}.html'),
#	 (5, 'index{number}.html', '{base_name}/index{number}.html'),
#	 #(6, 'index.html', '{}'),
#)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
