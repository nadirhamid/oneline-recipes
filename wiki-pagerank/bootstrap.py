##
## initial call. compute
## our pageranks
##
## we should only call 
## python for the parsing
##
## jython will be used for the
## pagerank as it is usable with PIG and Hadoop.

import subprocess

subprocess.call(['python', './pagerank-parse.py'])
subprocess.call(['pig', './pagerank-proc.py'])
