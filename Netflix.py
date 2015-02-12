#!/usr/bin/env python3

# -----------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Keerthana Kumar, Fatimah Zohra
# -----------------------------

import json

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    if ":" in s :
        global current_movie
        current_movie = int(s.split(":")[0])
        get_movie_avg_rating()
        return -1
    else:
        return s.strip()

# ------------
# data_collection
# ------------

def get_movie_avg_rating ():
    '''
        Gets the average rating for a single movie
    '''
    path = "/u/mck782/netflix-tests/pma459-mvAvgCache.json"
    json_data=json.loads(open(path).read())
    global current_movie_rating_avg
    current_movie_rating_avg = json_data[current_movie]

def get_user_avg_rating (customer_id):
    '''
        Gets the average rating of all the movies rated by the user
        input: customer_id String  
    '''
    path = "/u/mck782/netflix-tests/pma459-usrAvgCache.json"
    json_data=json.loads(open(path).read())
    return json_data[customer_id]


# ------------
# netflix_eval
# ------------

def netflix_eval (i) :
    return 0



# -------------
# netflix_print
# -------------

def netflix_print (w, s) :
    w.write(s + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        user = netflix_read(s)
        if user is not -1 :
            rating = netflix_eval(user)
            netflix_print(w, str(rating))
        else:
            netflix_print(w, str(current_movie)+":")
