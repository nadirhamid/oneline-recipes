

##############################################################################
# @author Nadir Hamid 
# @package Last.fm streaming application
# @does Streams tag based data using last.fm's public data set
##############################################################################

from oneline import ol

class last_fm(ol.module):
    def start(self):
        self.pipeline = ol.stream()
    
    def receiver(self, message):
        self.pipeline.run(message)
  
