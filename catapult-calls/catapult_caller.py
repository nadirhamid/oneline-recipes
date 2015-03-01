
##############################################################################
# Factory created module. Edit 
# as you like 
# @author Nadir Hamid 
# @package Bandwidth Catapult WebSocket Caller
# @does this example shows a live streaming demo 
# using Bandwidth's Catapult API. it will allow you to
# make calls and view their state in real time

##############################################################################

from oneline import ol
from bandwidth_sdk import Client
from bandwidth_sdk import Call
import bsonlib

class catapult_caller(ol.module):
    def start(self):
        print "Starting the Catapult Module."
        self.pipeline = ol.stream()
        self.config = ol.config()

        self.bandwidth_client = Client(self.config['bandwidth_user_id'], self.config['bandwidth_app_id'], self.config['bandwidth_app_secret'])
    
    def receiver(self, message):
        ## let's parse our message and
        ## see what we need to do
        ##
        ## remember: messages come in BSON
        ## so we need to call ol.parse_message
        ## make sure to resend these messages in their
        ## BSON form as oneline's client will only read
        ## that
        parsed_message = ol.parse_message(message) 
        packet = parsed_message['packet']

        if packet['generic']['type'] == "call":
          print "Calling someone!"
          try:
            call = Call.create(self.config['bandwidth_number'],packet['generic']['data']['to'])
          except:
            pass
        if packet['generic']['type'] == "list":
          calls = Call.list()
          calls_d = []
          for i in calls:
            call = { 'from':getattr(i,'from_'),'to':i.to,'state':i.state }
            calls_d.append(call)

          parsed_message['data'] = calls_d

        packed = ol.pack_message(parsed_message)

        self.pipeline.run(packed)

    def provider(self, message):
        ## provides the message
        ## this should just be
        ## a block of json because 
        ## we do all the work in receiver/1

        ## custom message:
        ## since we're using a different approach
        parsed_message = ol.parse_message(message)

        self.pipeline.run(message)

    def end(self):
        print "Closing Catapult module. See you soon!"

