#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Blog information
AUTHOR = 'Danilo Bargen'
SITENAME = 'blog.dbrgn.ch'
SITEURL = ''

# Localization issues
TIMEZONE = 'Europe/Zurich'
DEFAULT_LANG = 'en'
LOCALE = ['en_US']

# Metadata
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Blog'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Jinja
JINJA_EXTENSIONS = []
JINJA_FILTERS = []

# Plugins
PLUGINS = ['plugins.iframe_rst_directive', 'plugins.video_rst_directives']

# Markup
MARKUP = ('rst',)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Build process
STATIC_PATHS = ['images', 'files']
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 15
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

# URL configuration
RELATIVE_URLS = True  # dev only
ARTICLE_URL = '{date:%Y}/{date:%-m}/{date:%-d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%-m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%-m}/{date:%-d}/index.html'
PAGE_LANG_SAVE_AS = False
ARTICLE_LANG_SAVE_AS = False
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False

# Theme
THEME = 'themes/dbrgn'
GITHUB_URL = 'https://github.com/dbrgn/'
FAVICON = 'favicon.ico'
BLOG_LICENSE = 'http://creativecommons.org/licenses/by-sa/3.0/'
GOOGLE_SITE_VERIFICATION = 'uJWWR6d5ESb8torD0v97T_07HLMGX7VzQ-smcUTc_IQ'
