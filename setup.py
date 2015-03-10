# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
	name = 'graph-mtb-search',
    version = '1.0',
    author = 'Luis Eduardo Gutiérrez',
    author_email = 'legua.2507@gmail.com',
    description = 'A sample implementation for Concurrent Branching Search, threaded variant',

    keywords = 'example search uninformed ai artificial intelligence graph concurrent',
    url = 'https://github.com/legua25/graph-mtb-search',
    packages = [ 'mtb_search', 'mtb_search.graph', 'mtb_search.graph.navigator' ],
    classifiers = [ 'Development Status :: 4 - Beta' ]
)
