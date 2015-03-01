# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from navigator import MTBranchingNavigator
from graph import GraphFactory
import logging

if __name__ == '__main__':

	logging.basicConfig(filename = 'output.log', level = logging.INFO)

	g = GraphFactory.from_file('test.grp')
	nav = MTBranchingNavigator(g)

	def name_diff(node, goal): return abs(ord(goal.id[0]) - ord(node.id[0]))
	print nav.run('A', 'H', num_threads = 4, heuristic = name_diff)
