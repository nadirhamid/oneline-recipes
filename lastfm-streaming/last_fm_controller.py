from oneline import ol
import json
import os
import re
from oneline.dal import DAL, Field

db= None


def last_fm_init(sql='last_fm.sql', startserver=False):
  return ol.controller_init(sql=sql, startserver=False)

def last_fm_load():
  global db
  db  = ol.db_by_module("last_fm")
  count = db(db.tracks).count() 
  if count > 0:
    print "It seems you have already loaded the records. No need to again"
    
  else:

    ## this script will walk
    ## the Last.fm data tree
    ## turn .JSON objects to
    ## SQL like objects and store
    ## using our .conf filej

    ## store only when .JSON

    prefix = "./lastfm_test/"
    _dir = os.listdir(prefix)
    
    for i in _dir: 
      i = i.encode('ascii', 'ignore')
      print i
      p =  os.path.abspath("./lastfm_test/{0}".format(i))
      if os.path.isdir(p):
        _dirs(p) 
      if os.path.isfile(p):
        _files(p)    
  return True
def _files(file):
  global db
  if len(re.findall(".json$", file)) > 0:
    json_file = open(file, "r+").read()
    json_obj = json.loads(json_file)
    keys = ['artist','timestamp', 'similars', 'tags', 'track_id', 'title']
    ## first make sure its authentic
    ## we do this by checking if all our keys exist in the first object
    ms = 0
    for i in json_obj.keys():
      if i in keys:
        ms += 1
    if ms == len(keys):
      ## store it in our db
      ## make sure to comma seperate our tags
  
      ## we should also make sure similars are fetched
       tags = ",".join([t[0] for t in json_obj['tags']])
       artist = json_obj['artist'].encode('ascii', 'ignore')
       title = json_obj['title'].encode('ascii', 'ignore')

       db.tracks.insert(
        artist=artist,
        title=title,
        datetime=json_obj['timestamp'],
        track_id=json_obj['track_id'],
        tags=tags
       )
    
    else:
      print keys[ms]
   #return True ## true by default if we have errors the db will warn
    

## recursion
def _dirs(dir):
  _dir = os.listdir(dir)
  for i in _dir:
    i = i.encode('ascii', 'ignore')
    print i
    p =  os.path.abspath("{0}/{1}".format(dir,i))
    if os.path.isdir(p):
      _dirs(p) 
    if os.path.isfile(p):
      _files(p)    


