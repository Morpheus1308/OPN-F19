CREATE DATABASE crowd;

USE crowd;

CREATE TABLE people (
    personid int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    firstname varchar(255),
    lastname varchar(255)
);