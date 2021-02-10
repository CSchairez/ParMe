DROP TABLE IF EXISTS round;

CREATE TABLE round (
   round_id    INT AUTO_INCREMENT NOT NULL,
   user_id	 INT     		NOT NULL,
   course_name VARCHAR(25)  NOT NULL,
   score  	 INT NOT NULL,
   played_on   DATETIME ,       
   PRIMARY KEY(round_id),
   FOREIGN KEY(user_id) REFERENCES user(user_id)) AUTO_INCREMENT=1;
   