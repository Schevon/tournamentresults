--Table Schema
--Table definitions for the tournament project.


--Create Table PLAYER
--PLAYER_ID is used as the primary key to uniquely identify PLAYERS
--SERIAL is used to autoincrement PLAYER_ID

CREATE TABLE PLAYER(
   PLAYER_ID      SERIAL PRIMARY KEY,
   NAME           TEXT    NOT NULL,
   WINS           INT,
   LOSSES         INT,
   DRAWS          INT,
   NUM_OF_MATCHES INT,
   CREATED_DATE   DATE
 );

--create table MATCH
--MATCH_ID is used as the primary key to uniquely identify matches
--SERIAL is used to autoincrement MATCH_ID
--WINNER_ID is the foreign key in MATCH, it references 
--PLAYER_ID (the primary key in the PLAYER table).This enforces referential integrity 

CREATE TABLE MATCH(
   MATCH_ID 	  SERIAL PRIMARY KEY,
   WINNER_ID      INT references PLAYER(PLAYER_ID),
   LOSER_ID       INT,
   CURRENT_ROUND  INT,
   MATCH_DATE     DATE
 );

