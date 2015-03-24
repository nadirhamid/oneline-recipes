## use both redlinks and
## pagerank in same script
## to prevent overhead by PIG

import os

execfile(os.path.abspath("pagerank-redlinks.py"))
execfile(os.path.abspath("pagerank-core.py"))
execfile(os.path.abspath("pagerank-clean.py"))
