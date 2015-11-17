CREATE TABLE IF NOT EXISTS `yelp_businesses` (
  `id`  smallint(3) AUTO_INCREMENT,
  `city` varchar(255),
  `business_name` varchar(255),
  `business_type` varchar(255),
  `business_id` varchar(255),
  `code` varchar(255),
  `verified` varchar(255),
  `open_time` varchar(255),
  `close_time` varchar(255),
  `type` varchar(255),
  `category` varchar(255),
  `state` varchar(255),
  `time`  varchar(255),
  `lat` varchar(255), 
  `lng` varchar(255),
  `dist` varchar(255),
  `addr` varchar(255),
  `business_description` varchar(255),  
  PRIMARY KEY(`id`)
);
 
