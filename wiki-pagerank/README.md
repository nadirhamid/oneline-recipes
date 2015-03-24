Wiki Page Rank
=================================================================

This recipe performs Google's pagerank. It will
stream pagerank with websockets using a dampening factor of
0.08. Pig does the data processing while websockets will deliver
its content

Prequisites:
  1. Make sure you have a valid wikipedia export.
  NOTE:
  In this directory there is an open data set (from wikipedia)
  it is an export of computer science articles. You can however use
  anything. 
  2. Apache PIG and Hadoop
  3. Jython 
  4. Oneline server

Deploying
---------------------------------------------------

  1. set this up on a known web server
  2. to deploy this you will need to update wiki_pagerank.conf
with your database info.
  3. run ./bootstrap.py this will generate the immediate pageranks
  4. visit wiki_pagerank.html in your browser

Other
---------------------------------------------------
  1. the file wiki.xml can be replaced with any
  wikipedia export you need to obtain this you should visit:
