--Table Schema
--Table definitions for the tournament project.


--Creating Table name Player
CREATE TABLE PLAYER(
   PLAYER_ID      SERIAL PRIMARY KEY,
   NAME           TEXT    NOT NULL,
   WINS           INT,
   LOSSES         INT,
   DRAWS          INT,
   NUM_OF_MATCHES INT,
   CREATED_DATE   DATE
 );

CREATE TABLE MATCH(
   MATCH_ID 	  SERIAL PRIMARY KEY,
   WINNER_ID      INT references PLAYER(PLAYER_ID),
   LOSER_ID       INT,
   CURRENT_ROUND  INT,
   MATCH_DATE     DATE
 );

