import json
import os
import re
from oneline.dal import DAL, Field
## this script will walk
## the Last.fm data tree
## turn .JSON objects to
## SQL like objects and store
## using our .conf filej

## store only when .JSON

db = DAL("mysql://root:@localhost/lastfm_data", migrate=False)
db.define_table(
  "tracks", 
  Field("id"), 
  Field("track_id"),
  Field("title"),
  Field("artist"),
  Field("datetime"),
  Field("tags")
)

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
      pass ## not a valid object
    

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

if __name__ == '__main__':
  prefix = "./lastfm_test/" 
  _dir = os.listdir(os.path.abspath("./lastfm_test"))
  
  for i in _dir: 
    i = i.encode('ascii', 'ignore')
    print i
    p =  os.path.abspath("./lastfm_test/{0}".format(i))
    if os.path.isdir(p):
      _dirs(p) 
    if os.path.isfile(p):
      _files(p)    
  
