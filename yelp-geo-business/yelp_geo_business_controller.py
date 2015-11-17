import os
import time
import random
from oneline import ol


def yelp_geo_business_init(sql='yelp_geo_business.sql',startserver=True):
  return ol.controller_init(sql=sql,startserver=startserver)
def yelp_geo_business_clean(cleansql=True):
  return ol.controller_clean(cleansql=cleansql)
def yelp_geo_business_load():
  yelp_geo_business_init(sql='yelp_geo_business.sql',startserver=False)
  db  =ol.db_by_module("yelp_geo_business")
  #import bootstrap
  files = [
       dict(type='businesses', file=os.path.abspath("./yelp/business/yelp_academic_dataset_business.tsv"))
   ]

  propagateYelpData(db,files)
  yelp_geo_business_init(sql='yelp_geo_business.sql',startserver=True)

def get_start_of_day():
   pass


def propagateYelpData(db, files):
  countOfRecordsLoaded = 0
  for i in files:
    print "Importing %s" % i['file']
      
    lines  = open(i['file'], "r+").readlines()
    if i['type'] == 'businesses':
      schema = [
        "city",
        "code",
        "business_name",
        "type",
        "business_id",
        "addr",
        "state",
        "lat",
        "dist",
        "lng",
        "verified",
        "category"
      ]
          
    if i['type'] == 'reviews':
      schema = [
        "rating_0",
        "rating_1",
        "rating_2",
        "review_id",
        "review_id1",
        "review",
        "business_id",
        "review_rating",
        "date"
      ] 
    for i1 in lines:
       data = i1.strip().split("\t")
       row = dict() 
       ## add the data according
       ## to the definition in schema
       ## and DAL
       #print "Importing: " + ",".join(data)
       
       start_time = time.time()
       end_time = start_time + int(random.randint(0, 3600*8))
       row['open_time'] = start_time
       row['close_time'] = end_time
       for i2 in range(0, len(schema)):
         row[schema[i2]] = data[i2]
       rec = getattr(db, "yelp_" +i['type']).insert(**row)

       print "Adding record %s" % (rec.as_dict().__str__())
       countOfRecordsLoaded += 1 if rec else 0 
       db.commit()

    print "Imported: " + i['type']
    print "Loaded: " + str(countOfRecordsLoaded) + " records"

    return True  if countOfRecordsLoaded > 0 else False
      
        


