#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://omlalala.io'
DISQUS_SITENAME = "omlalalaio" #填入你的Shortname
DELETE_OUTPUT_DIRECTORY = None #因为嵌套仓库的原因,不能清除发布目录!


# Feed generation is usually not desired when developing
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS= None

SOCIAL = SOCIAL + (('rss', SITEURL + '/' + FEED_ALL_ATOM),)


ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL

TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'


RELATIVE_URLS = False