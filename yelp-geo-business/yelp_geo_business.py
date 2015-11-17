

##############################################################################
# Factory created module. Edit 
# as you like 
# @author Nadir Hamid
# @package Geolocation Yelp Streamer
# @does Shows how to stream geo based business
# data using Yelp's Academic dataset
##############################################################################

from oneline import ol

## This example uses the JOIN table
## functionality which will on success
## take the reviews table and correlate the
## business ids this can be seen more in depth
## (view ./yelp_geo_business.conf) 
##
##
class yelp_geo_business(ol.module):
    def start(self):
        print "starting yelp module"
        self.pipeline = ol.stream()
   
    ## provide the data
    ## to our frontend
    ## since we are using
    ## a database here
    ## it is not needed
    #def provider(self, message): 
    #    return self.pipeline.run(message)

    ## receive our data
    ## this will either be
    ## search terms
    ## or can be
    ## streaming results
    ##
    ##
    ## we will use the event
    ## object here which will
    ## take our search term 
    ## and match it agaianst our
    ## business table
    def receiver(self, message):
        #data = ol.parse_message(message)
        generic = message.get("generic")
        geo = message.get("geo")
        event = message.get("event")
        time = message.get("time")
        if generic:
          print "Received a generic"
        if time:
          print "Received a time object"
        if event:
          print "Received an event object"
          
        return self.pipeline.run(message)


    def stop(self):
        print "closing  Yelp module"
