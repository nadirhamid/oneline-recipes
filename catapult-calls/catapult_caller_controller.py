from oneline import ol
## no need to add any sql,
## by supplying False nothing will
## be executed
def catapult_caller_init(sql=False, startserver=True):
  return ol.controller_init(sql,startserver)

def catapult_caller_stop(stopserver=True):
  return ol.controller_stop(stopserver)
