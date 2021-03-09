DROP TABLE IF EXISTS comment;

CREATE TABLE comment ( 
   comment_id       INT AUTO_INCREMENT  NOT NULL, 
   content          VARCHAR (55)        NOT NULL, 
   commented_on 	DATETIME,
   user_id	 		INT     		NOT NULL,
   PRIMARY KEY (comment_id)
   );
