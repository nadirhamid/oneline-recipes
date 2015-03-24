#!/usr/bin/python
"""
Perform the functionality as per
the PIG pagerank. Run in jython for

"""

import os
from org.apache.pig.scripting import * 

## PageRank definition:
## (A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))
## needs dampening factor of 0.8

P = Pig.compile("""
-- PR(A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))

previous_pagerank = load '$docs_in' as (url:chararray, pagerank:float,
                      links:{link:(url:chararray)});
outbound_pagerank = foreach previous_pagerank generate
                      pagerank / $pages as pagerank,
                      flatten(links) as to_url;
cogrpd            = cogroup outbound_pagerank by to_url,
                      previous_pagerank by url;
new_pagerank      = foreach cogrpd generate group as url,
                      (1 - $d) + $d * SUM (outbound_pagerank.pagerank)
                      as pagerank,
                      flatten(previous_pagerank.links) as links,
                      flatten(previous_pagerank.pagerank) AS previous_pagerank;
store new_pagerank into '$docs_out';
nonulls           = filter new_pagerank by previous_pagerank is not null and
                        pagerank is not null;
pagerank_diff     = foreach nonulls generate ABS (previous_pagerank - pagerank);
grpall            = group pagerank_diff all;
max_diff          = foreach grpall generate MAX (pagerank_diff);
store max_diff into '$max_diff';
new = load '$docs_out' as (page:chararray, pagerank:float);
new1 = filter new by pagerank > $threshold;
new2 = DISTINCT new1;
new3 = order new2 by pagerank DESC;
store new3 into '$docs_final';
""")

## wikilinks should be available by now
params = { 'd': '0.8', 'docs_in': './data/wikilinks' }

if __name__ == '__main__':
  threshold = 0.0
  pages = len(open(os.path.abspath("./data/wikilinks"), "r+").readlines())

  for i in range(8):

    if os.path.isfile(os.path.abspath("./out/max_diff_" + str(i))):
      m = float(open(os.path.abspath("./out/max_diff_" + str(i)), "r"))
    else:
      m = None 

    if i == 8 or m < 0.01:
      threshold = 0.05

    out = "./out/wikilinks_data_" + str(i + 1)
    max_diff = "./out/max_diff_" + str(i + 1)
  
    params["docs_out"] = out
    params["docs_final"] = out + '_final'
    params["max_diff"] = max_diff
    params["pages"] = pages
    params["threshold"] = threshold
    Pig.fs("rmr " + out)
    Pig.fs("rmr " + max_diff)
    bound = P.bind(params)
    stats = bound.runSingle()
    if not stats.isSuccessful():
      break
      

    try:
      mdv = float(str(stats.result("max_diff").iterator().next().get(0)))
      if mdv < 0.01:
        print "done at iteration " + str(i)
    except:
      print "done at iteration " + str(i)
      break

    params["docs_in"] = out


