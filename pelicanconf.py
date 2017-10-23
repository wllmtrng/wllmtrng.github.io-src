#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

LOAD_CONTENT_CACHE = False

AUTHOR = 'Will Truong'
SITENAME = 'Dovetailing Thoughts'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Resume', 'https://github.com/wllmtrng/Resume/blob/wllmtrng/resume.pdf'),)

# Social widget
SOCIAL = (('github', 'https://github.com/wllmtrng'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "/Users/williamtruong/code/wllmtrng.github.io-src/themes/danielfrg"

# THEME SETTINGS
# DEFAULT_HEADER_BG = '/images/station1.jpg'
# ABOUT_PAGE = '/pages/about.html'
# TWITTER_USERNAME = 'danielfrg'
GITHUB_USERNAME = 'wllmtrng'
SHOW_ARCHIVES = True
SHOW_FEED = True

MARKUP = ('md', 'ipynb')

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 150
DEFAULT_PAGINATION = 10

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']

STATIC_PATHS = ['images']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = PAGE_SAVE_AS

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codehilite'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Paths are relative to `content`
STATIC_PATHS = ['images', 'favicon.ico', '404.html', 'robots.txt', 'CNAME']

# PLUGINS SETTINGS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'ipynb.markup', 'ipynb.liquid', 'liquid_tags.youtube', 'liquid_tags.b64img']

SITEMAP = {
    'format': 'xml'
}

IGNORE_FILES = ['.ipynb_checkpoints']

IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('ol', None), ('ul', None)]
