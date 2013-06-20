#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blog.dbrgn.ch'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feed.atom'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'dbrgn'
GOOGLE_ANALYTICS = 'UA-1033934-12'
