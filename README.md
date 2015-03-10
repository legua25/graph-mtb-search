# Concurrent Branching Search
A Python implementation for a fully concurrent, uninformed search algorithm over a search space.
Includes a search space generator, two search algorithm implementations, and a benchmark generator to test implementations.

## Installation / Running
This program requires Python version 2.7.+ to run with the following requirements list:

  * `` futures version 2.2.0 ``
  * `` Jinja2 version 2.7.3 ``

To install and configure the contained tools, run the following command on a terminal from the root directory of the source distribution:

  `` python setup.py install ``

In order to execute the benchmark generator, run the following command from a terminal:

  `` python profile.py <num-nodes> <max-connect> [-min_connect <min-connect> -tests <tests> [-t|--trace]] ``

The program will generate a series of random test suites and execute profiling tests for each of the contained search 
algorithms. The navigated graphs, along with the resulting benchmark information and output log (if requested using the 
`` -t|--trace `` flag) are written inside the current working directory.
