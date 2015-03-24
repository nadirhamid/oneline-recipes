

##############################################################################
# Factory created module. Edit 
# as you like 
# @author Nadir Hamid
# @package Wiki Page Rank
# @does WikiPedia article pagerank using WebSockets

##############################################################################


## IMPORTANT: you should run ./bootstrap.py
## before using this module. 
import os
from oneline import ol

class wiki_pagesearch():
    ## define where we can
    ## find the wikipedia results
    ## also should be able to update
    def __init__(self):
      self.results = os.path.abspath("./out/results/")

    ## looks up our term
    ## where our term 
    ##
    ## @param term: string search
    ##
    def search(self, term):
      file = open(self.results,"r+").read()
      ## match the article
      ## name and its page rank
      results = re.findall("^(.*" + term + ".*)\s([\d\.]+)$", file)
      processed =dict() 
      for i in results:
        processed[i] = i
      
      return processed


    def run_job(self):
      subprocess.popen("pig", ['./pagerank-all.py'])
      

    ## update page rank
    ## this should be using
    ## the dampening factor defined above
    ##
    ##
    ## we use Python's subprocess
    ## to update our page ranks

    ## NOTE: this calls a Hadoop (in PIG)
    ## job so usage on EMR or something
    ## similar is highly recommended
    ##
    ##
    ## to update the rnak we need to look
    ## at the file containing the wiki output
    ## as made by pagernak-parse.py
    ## append to this data using another 
    ## page which will be set as 
    ## article_name_time
    ## @param term: this is the fully qualified article
    ## name.

    def update(term):

      new_page = term + time.time()
      file = open(os.path.abspath("./data/wikilinks", "r+")).read()
      system.Popen("pig", [os.path.abspath("./pagerank-core.py")])
      if len(re.findall(term, file)) > 0:
        m = re.findall(term + "\\((.*)\)", file) 
        existing_term = m[1]
        new_term = "(" + m[1] + ", " + new_page + ")" 
        new_term_full = term + new_term
        file = re.sub("^" + term +  "(.*)" + "$", new_term_full)

     
        nf = open(os.path.abspath("./data/wikilinks", "w+"))
        nf.write(file)
     
        ## close the file  
        ## as we have written our new
        ## contents
        nf.close()


        ## now we need to call
        ## a PIG job to reanlyze the
        ## data
        self.run_job()

        return True
      else:
        ## we need to trow an error here as we could
        ## not find the article, this should rarelyt
        ## happen when it does, we should warn 
        ## the frontend
        return False



    
class wiki_pagerank(ol.module):
    ## initialize our 
    ## oneline module
    def start(self):
        self.pipeline = ol.stream()
        self.config = ol.config()
        self.wiki = wiki_pagesearch()


    ## our oneline receiver    
    ## this will use Oneline.generic
    ## and handle a search or pagerank
    ## update
    def receiver(self, message):
      data = ol.parse_message(message)
      if data['type'] == 'search':
        results = self.wiki.search(data['data']['term']) 
        data['data'] =  results
        data['message'] = "SUCCESS"
      elif data['type'] == 'update':
        result = self.wiki.update(data['data']['term'])
        if not result:
          ## something went wrong we
          ## should include the result
          ## in part of our message
          data['message'] = "ERROR"
        else:
          data['message'] ="SUCCESS"

      message = ol.pack_message(data)

      return self.pipeline.run(message)

    ## closes the oneline module
    def stop():
      print "Closing wikipedia pagerank module"
