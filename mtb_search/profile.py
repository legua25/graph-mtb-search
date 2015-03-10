# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from argparse import ArgumentParser
from mtb_search.graph import *
from StringIO import StringIO
from cProfile import Profile
from jinja2 import Template
from random import choice
from pstats import Stats
from math import log
import logging
import os

if __name__ == '__main__':

	cmd = ArgumentParser(
		prog = 'Multithreaded Branching Search',
	    description = 'Benchmark generator comparing Breadth-First Search (BFS) with Multithreaded Branching Search (MTBS).'
	)
	cmd.add_argument('num_nodes',
	    type = int,
	    help = 'Specify the number of nodes to create for each test graph.'
	)
	cmd.add_argument('max_connect',
	    type = int,
	    help = 'Specify the maximum number of connections to create per node.'
	)
	cmd.add_argument('-min_connect',
	    type = int,
	    default = 1,
	    help = 'Specify the minimum number of connections to create per node. Defaults to 1.'
	)
	cmd.add_argument('-tests',
	    type = int,
	    default = 10,
	    help = 'Specify the number of tests cases to generate. Defaults to 10.'
	)
	cmd.add_argument('-t', '--trace',
		action = 'store_true',
	    default = False,
	    help = 'Toggles on/off logging information.'
	)
	args = cmd.parse_args()

	BASE_DIR = os.getcwd()
	data = { 'bfs': [], 'mtb-4': [], 'mtb-8': [], 'searches': [] }
	tests = 10

	t = Template("""test_{{ size }}_{{ i }} {}
{% for n in g %}
{{ n.to_template_string() }}{% endfor %}
""")

	num_nodes = args.num_nodes
	max_connect = args.max_connect
	min_connect = args.min_connect
	name_length = int(log(float(num_nodes), 10))
	trace = args.trace

	if trace: logging.basicConfig(filename = '%s/out.log' % BASE_DIR, level = logging.INFO)

	for i in range(tests):

		g = GraphBuilder.create_graph(num_nodes, max_connect, min_connections = min_connect, name_length = name_length)
		with open('%s/graph_%i_%i.txt' % (BASE_DIR, num_nodes, i), 'w') as f:
			f.write(t.render({ 'i': i, 'size': num_nodes, 'g': g }))

		n1 = BreadthFirstNavigator(g)
		n2 = MTBranchingNavigator(g)

		start, end = choice(g._nodes.keys()), choice(g._nodes.keys())
		data['searches'].append(( start, end ))

		for fn, key in [
			(lambda: n1.navigate(start, end, trace = trace), 'bfs'),
			(lambda: n2.navigate(start, end, num_threads = 4, trace = trace), 'mtb-4'),
			(lambda: n2.navigate(start, end, num_threads = 8, trace = trace), 'mtb-8')
		]:

			p = Profile()
			p.enable()
			fn()
			p.disable()

			data[key].append(Stats(p, stream = StringIO()).print_stats(0.05))

	with open('%s/benchmarks.txt' % BASE_DIR, 'w') as f:

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
