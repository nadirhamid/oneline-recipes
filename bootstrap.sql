CREATE DATABASE oneline_lastfm_demo;

use lastfm_data;

CREATE TABLE tracks (
  id int(5) AUTO_INCREMENT, 
  title varchar(255), 
  track_id varchar(255), 
  artist varchar(255), 
  datetime varchar(255), 
  tags mediumblob, 
  PRIMARY KEY(id)
);

INSERT INTO tracks (id, track_id, title, artist, datetime, tags) VALUES (NULL, 'TR', 'test', 'TR', 'TR', 'pop');
