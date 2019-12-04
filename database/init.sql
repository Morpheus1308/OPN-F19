CREATE DATABASE IF NOT EXISTS crowd;

USE crowd;

CREATE TABLE IF NOT EXISTS people (
    personid int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    firstname varchar(255),
    lastname varchar(255)
);