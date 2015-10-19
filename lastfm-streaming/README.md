Recipe: Oneline Last.fm Tag Streamer
====================================================================

What it does
--------------------------------------------------------------------

This application will stream tag based data using Last.fm's publicly
available dataset. You can add as many tags as you want filter
and results will update accordingly 

Oneline Recipe
-------------------------------------------------------------------
To set this up with oneline you will to do the following:

Application Specific:
  1. Make sure these files are accessible via your web server!
  2. make sure to fill in last_fm.conf first you will need to provide it
    your database credentials above anything
  3. oneline --pack 'last_fm'
  4. oneline --controller 'init'
  5. oneline --controller 'load'

  5. oneline --start


Notes
------------------------------------------------------------------

- The dataset with this recipe is 128mb. if pulling from Git make sure
the delta size is sufficient. 

- There is even a larger dataset Last.fm offers which for the sake of 
size is not provided with this. Instructions on using this in place of the
s
