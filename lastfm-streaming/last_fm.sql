CREATE TABLE tracks (
  id int(5) AUTO_INCREMENT, 
  title varchar(255), 
  track_id varchar(255), 
  artist varchar(255), 
  datetime varchar(255), 
  tags mediumblob, 
  PRIMARY KEY(id)
);
