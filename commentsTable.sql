DROP TABLE IF EXISTS comments;

CREATE TABLE comments ( 
   comment_id       INT AUTO_INCREMENT  NOT NULL, 
   content          VARCHAR (55)        NOT NULL, 
   commented_on 	DATETIME,
   user_id	 		INT     		NOT NULL,
   PRIMARY KEY (comment_id),
   FOREIGN KEY(user_id) REFERENCES user(user_id)) AUTO_INCREMENT=1;