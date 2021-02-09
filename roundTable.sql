DROP TABLE IF EXISTS round;

CREATE TABLE round (
   round_id    INT AUTO_INCREMENT NOT NULL,
   golfer_id	 INT     		NOT NULL,
   course_name VARCHAR(25)  NOT NULL,
   score  	 VARCHAR(3) NOT NULL,
   played_on   DATETIME NOT NULL,       
   PRIMARY KEY(round_id),
   FOREIGN KEY(golfer_id) REFERENCES user(id)) AUTO_INCREMENT=1;
   