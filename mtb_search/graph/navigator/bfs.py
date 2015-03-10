# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from base import Navigator, NOWHERE
import logging

class BreadthFirstNavigator(Navigator):

	def navigate_to(self, start, goal, trace = False):

		frontier = [ self.path_class(start) ]
		visited = []

		while bool(frontier) is True:

			# Obtain a node to iterate over
			n = frontier.pop(0)
			assert isinstance(n, self.path_class)

			# Check if current node is the goal node
			if n.node is goal:

				if trace: logging.info('Found path to objective "%s" (cost: %.8f)' % (goal.id, float(n.cost)))

				path = [ path for path in reversed(list(n)) ]

				if trace: logging.info('Path information: %s' % path)
				return path
			else:

				if trace: logging.info('Visiting node "%s" (parent: "%s", current cost: %.8f)' % (n.id, n.parent, float(n.cost)))

				# Add this node to the visited list and its children to the frontier if this hasn't been done already
				if n.node not in visited:

					visited.append(n.node)
					frontier.extend([ self.path_class(child, parent = n, cost = (float(n.cost) + n.estimate_cost_to(child))) for child in n.list_connections() if child not in visited ])

		if trace: logging.info('No path found to objective "%s"' % goal.id)
		return NOWHERE
