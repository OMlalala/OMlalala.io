#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

###############################################################
###############################################################   Site abt.
###############################################################
AUTHOR = 'OMlalala'
AUTHOR_INFOS = True

SITENAME = ''
SITETITLE = 'Reborn'
SITEURL = 'https://omlalala.github.io'

MARKUP = ('md', 'rst',)#'rst', 'html', 
READERS = {
        'html': None,
}
#   TIMEZONE = 'Europe/Paris'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_DATE = 'fs' # use filesystem's mtime

#LOCALE = ('zh_CN.utf8',)
DEFAULT_LANG = 'zh_CN'
FILENAME_METADATA = '(?P<slug>.*)'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

###############################################################
###############################################################   Plugins abt.
###############################################################
# Plugins 
PLUGIN_PATHS = ['_plugins']
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

###############################################################
###############################################################   Template abt.
###############################################################
THEME = "_themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'readable'

DEFAULT_PAGINATION = 3

DISPLAY_TAGS_ON_SIDEBAR = False
TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = None      # 分类标签是否显示在导航
# Social widget -> China jiathis.com
ADDTHIS_PROFILE = None #True
    
#GITHUB_USER = "ZoomQuiet"
MENUITEMS = (('PyChina', 'http://pychina.org')
#    , ('OBP', 'http://obp.zoomquiet.io')
    , ('abt.', '/pages/about.html')
#    , ('design', '/pages/design.html')
    )
DISPLAY_PAGES_ON_MENU = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
# ('rss', SITEURL + '/' + FEED_ALL_ATOM)
SOCIAL = (('.io', 'http://ZoomQuiet.io')
        , ('Wiki', 'http://wiki.zoomquiet.io')
        , ('旧曰', 'http://blog.zoomquiet.org/pyblosxom/')
        , ('啄木鸟', 'http://wiki.woodpecker.org.cn/moin/ZoomQuiet')
        , ('GitHub', 'https://github.com/ZoomQuiet')
        , ('O.B.P', 'https://github.com/OpenBookProjects/wiki/blob/master/HowToBuildBookOnline.md')
        , ('Weekly', 'http://weekly.pychina.org/')
        , ('weibo', 'http://weibo.com/zoomquiet')
        )
# Blogroll
LINKS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images'
	,
]