Tournament Results
Project Description
This is a python module which uses an ORDBMS, PostgreSQL database, to support and keep track of players and matches in a game tournament. 
 This Project involves developing a database schema to store match results, write code to query this data and determine the winners of various games.
The tournament uses a “Swiss System” for pairing players per round. Players are never eliminated. Instead players are paired in every single round; their opponent is determined by how similar their records are. In the end, the player with the most points is declared the winner.
The project basically consists of two parts:
1. The database Schema (table definitions)
2. Python code which implements the “Swiss Tournament” System. 
Files
 tournament.sql - database schema, in the form of SQL create table commands. 
 tournament.py – implementation of the “Swiss Style” Tournament
tournament_test.py – unit tests that will test the functions written in tournament.py
Usage
Assuming that a database has been created and the necessary installations are present (see dependencies below), proceed to cloning this repository directory and run tournament.sql.  This creates tables PLAYER and MATCH. Run tournament.py to execute the required CRUD operations on the tables created.  Run tournament_test.py to unit tests the functions written in tournament.py.
Dependencies
Python 2.7.9
PostgreSQL 9.3.6
psql 9.4.1 
Linux based OS such as Ubuntu 
