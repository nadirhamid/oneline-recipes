"""
This file performs the needed
XML parsing provided the WikiLinks
which should be located in ./data

"""

import xml.etree.ElementTree as ET
import os
import re

## output all the wikipedia
## articles according to their amount
## of mentiones
##
##
class WikiPageRankStart(object):
  def __init__(self):
    out = open(os.path.abspath("./data/wikilinks"), "w+")
    out1 = open(os.path.abspath("./data/wikilinks.members"), "w+")
    xml = ET.parse("./data/wiki.xml")
    root = xml.getroot()

    seq = dict() 
    ostr = ""
    ostr1 = ""

    for page in root.getchildren():
      if not len(re.findall("page", page.tag)) > 0:
        continue

      title = ''
      for p in page.getiterator():
        """ we re only interested in the title and content """
        if len(re.findall("title", p.tag)) > 0:
          title =  p.text

        if not len(re.findall("text", p.tag)) > 0:
          continue


        m = re.findall("\[\[([\"\'\&;\w\s\d|\.!:\(\)\p{Latin}]+)\]\]", p.text) 
          ##m = re.findall("\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", p.text)

        """ take all the links and if they are in the sequence [ | ] or [ ] """

        if not title in seq.keys():
          seq[title] = [] 


        """ use tab in padding for PIG """
        for i in m:
          m1 = re.findall("([\"\'\&;\.\w\s\d\!(\)\:\p{Latin}]+)|([\"\'\&\.\w\s\d\!(\)\:\p{Latin}]+)", i)
          """ a link to a link """
          if len(m1) > 0:
            o = m1[0][0]
          else:
            o = i

          seq[title].append("(" + o + ")")
          #ostr += title + pad + o + "\n"

    """ currently the page rank will be 0 in the second column """

    #pad = " " * 8
    pad = "\t"
    #pr = "0"

    ## starting PageRank 1/N
    pr = str(float(1) / float(len(seq)))
    for k,v in seq.iteritems():
      ostr += k + pad + pr + pad + "{" + ",".join(v) + "}" + "\n"
      ostr1 += "'{0}',".format(re.sub("\)", "\)", re.sub("\(", "\(", re.sub(r"'", '"', k))))

    ostr1 = "({0})".format(re.sub(",$", "", ostr1)) ## not interested in last comma

    out.write(ostr)
    out1.write(ostr1)
    out1.close()
    out.close()

if __name__ == '__main__':
  WikiPageRankStart()
