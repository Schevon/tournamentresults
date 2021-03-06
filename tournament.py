#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import psycopg2
import sys

# thoughout the code cur = conn.cursor() has been used to
# prepare a cursor object using the cursor method.
# try/except  has also been used to handle exceptions
# if an exception occurs  the relevant database changes
# are reverted with conn.rollback() else the SQL statement
# is excecuted and committed to the db. Whether an exception
# occurs or not the databse connection closes after every
# function has returned a value or has completed executing.


# open database connection
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM MATCH")
        conn.commit()
    except:
        conn.rollback
        print"A databse error occured when trying to delete records"
    conn.close()


def deletePlayers():
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM PLAYER")
        conn.commit()
    except:
        conn.rollback()
        print"A databse error occured when trying to delete records"
    conn.close()


def countPlayers():
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT COUNT (*) FROM PLAYER")
        result = int((cur.fetchall())[0][0])
        return result
    except:
        conn.rollback()

    conn.close()


def registerPlayer(name):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO PLAYER (PLAYER_ID,NAME,WINS,LOSSES,DRAWS \
        ,NUM_OF_MATCHES,CREATED_DATE) \
            VALUES(DEFAULT, %s,0,0,0,0,CURRENT_DATE)", (name,))
        conn.commit()
        print "Player %s registered successfully !" % (name)
    except:
        conn.rollback()
        print "An error occurred while registering player"
    conn.close()


def playerStandings():

    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("SELECT PLAYER_ID, NAME, WINS, NUM_OF_MATCHES FROM PLAYER\
        ORDER BY WINS DESC")
        return cur.fetchall()
    except:
        conn.rollback()
        print"An error occurred while retrieving player standings"
    conn.close()

"""Returns a list of the players and their win records, sorted by wins.
The first entry in the list should be the player in first place, or a player
tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    conn = connect()
    cur = conn.cursor()
# if the relevant player id wins update and  increment the wins column
# else if the relevant player_id losesupdate and increment the loses column
    try:
        cur.execute("UPDATE PLAYER SET WINS = WINS + 1,NUM_OF_MATCHES =\
        NUM_OF_MATCHES + 1  WHERE PLAYER_ID = '%s'" % (winner))
        cur.execute("UPDATE PLAYER SET LOSSES = LOSSES + 1,NUM_OF_MATCHES =\
        NUM_OF_MATCHES + 1  WHERE PLAYER_ID = '%s'" % (loser))
        # after every match a new match record is inserted into the MATCH table
        cur.execute("INSERT INTO MATCH (MATCH_ID,WINNER_ID,LOSER_ID, MATCH_DATE) \
            VALUES(DEFAULT, %s ,%s,CURRENT_DATE)", (winner, loser,))
        conn.commit()
    except:
        conn.rollback()
        print"An error occured in reporting match"
    conn.close()

"""Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # playerStandings returns a list of player ids based on their rankings
    result = playerStandings()
    # creating a new array
    pairings = []
    i = 0
    # iterate through the list of playerStandings
    while i < len(result):
        # using the index to find the value of i = 0  thus [0][0]
        # which returns the  first player in the list "playerID" value
        player1Id = result[i][0]
        player1Name = result[i][1]

        player2Id = result[i+1][0]
        player2Name = result[i+1][1]

        # add the following results and store in an array
        pairings.append((player1Id, player1Name, player2Id, player2Name))
        # i = i+2
        i += 2
    print pairings
    return pairings
