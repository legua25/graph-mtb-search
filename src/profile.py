# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from jinja2 import Environment, PackageLoader
from StringIO import StringIO
from cProfile import Profile
from random import choice
from pstats import Stats
from graph import *

BASE_DIR = '../tests'
data = { 'bfs': [], 'mtb-4': [], 'mtb-8': [], 'searches': [] }
tests = 10

env = Environment(loader = PackageLoader('src.graph'))
t = env.get_template('template.txt')

num_nodes = 1000
max_connect = 900
min_connect = 5
name_length = 3

for i in range(tests):

	g = GraphBuilder.create_graph(num_nodes, max_connect, min_connections = min_connect, name_length = name_length)
	with open('%s/%i/graph_%i_%i.txt' % (BASE_DIR, num_nodes, num_nodes, i), 'w') as f:
		f.write(t.render({ 'i': i, 'size': num_nodes, 'g': g }))

	n1 = BreadthFirstNavigator(g)
	n2 = MTBranchingNavigator(g)

	start, end = choice(g._nodes.keys()), choice(g._nodes.keys())
	data['searches'].append(( start, end ))

	for fn, key in [
		(lambda: n1.navigate(start, end), 'bfs'),
		(lambda: n2.navigate(start, end, num_threads = 4), 'mtb-4'),
		(lambda: n2.navigate(start, end, num_threads = 8), 'mtb-8')
	]:

		p = Profile()
		p.enable()
		fn()
		p.disable()

		data[key].append(Stats(p, stream = StringIO()).print_stats(0.05))

with open('%s/%i/benchmarks.txt' % (BASE_DIR, num_nodes), 'w') as f:

	f.write('Searches in graph, by order:\n')
	f.write('\n'.join(map(lambda (i, v): '%i: from node "%s" to node "%s"' % (i, v[0], v[1]), enumerate(data['searches']))))
	f.write('\n--------------------------------------------------------\n')

	f.write('BFS:\n')
	f.write('\n'.join(map(lambda p: p.stream.getvalue(), data['bfs'])))
	f.write('--------------------------------------------------------\n')

	f.write('MTBS (4 cores):\n')
	f.write('\n'.join(map(lambda p: p.stream.getvalue(), data['mtb-4'])))
	f.write('--------------------------------------------------------\n')

	f.write('MTBS (8 cores):\n')
	f.write('\n'.join(map(lambda p: p.stream.getvalue(), data['mtb-8'])))
