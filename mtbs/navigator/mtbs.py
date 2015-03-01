# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from futures import ThreadPoolExecutor
from base import Navigator, Path, NOWHERE
from threading import RLock
import logging

class MTBranchingNavigator(Navigator):

	visited = []
	active = True
	result = NOWHERE
	frontier = None

	def navigate_to(self, start, goal, num_threads = 4, heuristic = lambda n, goal: 0, path_cls = Path, timeout = None):

		logging.info('Started search (num_threads: %i)' % num_threads)

		self.frontier = [ start ]
		threads = ThreadPoolExecutor(max_workers = num_threads)
		result_notify = RLock()
		visiting = RLock()
		query = RLock()

		def run_search(node, parent):

			logging.info('Starting task (node: %s)' % node.id)

			# Invalidate this job if a response has already been found
			with query:
				if self.active is False:

					logging.info('Invalidating task "%s" due to result being found...' % node.id)
					return

			if node is goal:

				logging.info('Node "%s": Attempting to signal result...', node.id)

				# Lock state and attempt to notify we found a solution
				with result_notify:
					if self.active is True:

						logging.info('Found path to "%s", locking state and yielding...' % goal.id)
						self.active = False
						self.result = path_cls(node, parent = parent)
			else:

				logging.info('Visiting node "%s"...' % node.id)

				with visiting:

					# Add this node to the visited list
					if node not in self.visited:

						self.visited.append(node)

						# Post a new job for the executor pool, provide the current node as the parent node
						# We now use a search heuristic, pass it along to the connections list to organize it
						for child in [ n for n in node.list_connections(heuristic, goal) if n not in self.visited ]:
							threads.submit(run_search, child, path_cls(node, parent = parent))

		with threads:

			for _ in range(num_threads):
				t = threads.submit(run_search, start, None)
				t.result(timeout)

		return self.result
