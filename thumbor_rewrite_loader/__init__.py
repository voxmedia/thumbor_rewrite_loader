#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

import re
from urlparse import urlparse
from thumbor.loaders import http_loader
from tornado.concurrent import return_future

def _normalize_url(url):
    url = http_loader.quote_url(url)
    return url if url.startswith('http') else 'http://%s' % url


def validate(context, url):
    return http_loader.validate(context, url, normalize_url_func=_normalize_url)


def return_contents(response, url, callback, context):
    return http_loader.return_contents(response, url, callback, context)


@return_future
def load(context, url, callback):
    if context.config.REWRITE_LOADER_HOST_PATTERNS:
      parsed_url = urlparse(_normalize_url(url))
      for pattern in context.config.REWRITE_LOADER_HOST_PATTERNS:
        if re.match('^%s$' % pattern, parsed_url.hostname):
          url = re.sub(pattern, context.config.REWRITE_LOADER_CANONICAL_HOST, url, 1)

    return http_loader.load_sync(context, url, callback, normalize_url_func=_normalize_url)


def encode(string):
    return http_loader.encode(string)
