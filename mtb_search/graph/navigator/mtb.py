# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from futures import ThreadPoolExecutor, TimeoutError
from threading import RLock as Lock, current_thread
from base import Navigator, Path, NOWHERE
import logging

class MTBranchingNavigator(Navigator):

	active = False
	result = NOWHERE
	visited = []

	def navigate_to(self, start, goal, num_threads = 4, timeout = None, trace = False):

		self.active = True
		self.result = NOWHERE
		self.visited = []

		threads = ThreadPoolExecutor(num_threads)
		lock = Lock()

		def __multi__(n):

			if self.active is False:
				if trace: logging.info('%s: Invalidating due to state closure' % current_thread().name)
			else:

				# Check if current node is the goal node
				if n.node is goal:

					# Invalidate state if it hasn't been done already
					with lock:

						if self.active is True:

							self.active = False
							if trace: logging.info('%s: Signalling closure and yielding path to objective "%s" (cost: %.8f)' % (current_thread().name, goal.id, float(n.cost)))

							self.result = [ path for path in reversed(list(n)) ]
				else:

					# Add this node to the visited list and its children to the frontier if this hasn't been done already
					if n.node not in self.visited:

						if trace: logging.info('%s: Visiting node "%s" (parent: "%s", current cost: %.8f)' % (current_thread().name, n.id, n.parent, float(n.cost)))
						self.visited.append(n.node)

						# Submit a new job for the thread pool in order to explore children
						for child in [ _ for _ in n.list_connections() if _ not in self.visited ]:

							cost = (n.cost + n.estimate_cost_to(child))
							threads.submit(__multi__, self.path_class(child, parent = n, cost = cost))

		with threads:

			value = threads.submit(__multi__, self.path_class(start))

			try: value.result(timeout)
			except TimeoutError:

				if trace: logging.info('No path found to objective "%s"' % goal.id)
				return NOWHERE

		if trace: logging.info('Path information: %s' % self.result)
		return self.result
