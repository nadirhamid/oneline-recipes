## This should run as a final
## step it will take the last
## iteration in pagerank
##
## and output its results
## to unique file named results

## NOTE:
##
## this will also delete all previous
## pagerank iterations

import os
import re

files = os.listdir("./out/")

if __name__ == '__main__':
  for i in files:
    current_i = 0
    last = False
    if len(re.findall("wikilinks_data_\d+")):
       m =  re.findall("wikilinks_data_(\d+)")
    if int(m[1]) > current_i:
      current_i = int(m[1])


  old = os.open("./out/wikilinks_data_{0}".format(current_i)).read()
  fp = os.open("./out/results", "w+")
  fp.write(old)
  fp.close()

  os.system("rm -rf ./out/wikilinks_data*")
