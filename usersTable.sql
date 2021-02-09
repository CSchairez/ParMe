DROP TABLE IF EXISTS user;

CREATE TABLE user ( 
   id           INT AUTO_INCREMENT  NOT NULL, 
   name         VARCHAR (55)        NOT NULL, 
   email        INT          UNIQUE NOT NULL, 
   registered_on DATETIME,			
   password 	VARCHAR(255) UNIQUE NOT NULL, 
   PRIMARY KEY (id)) AUTO_INCREMENT=1;