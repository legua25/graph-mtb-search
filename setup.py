# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from distutils.core import setup

setup(
	name = 'graph-mtb-search',
    version = '1.0',
    author = 'Luis Eduardo Gutiérrez',
    author_email = 'legua.2507@gmail.com',
    description = 'A sample implementation for Concurrent Branching Search, threaded variant',

    keywords = 'example search uninformed ai artificial intelligence graph concurrent',
    url = 'https://github.com/legua25/graph-mtb-search',
    packages = [ 'src', 'src.graph', 'src.graph.navigator' ],
    classifiers = [ 'Development Status :: 4 - Beta' ]
)
