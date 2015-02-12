#!/usr/bin/env python3

# -----------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Keerthana Kumar, Fatimah Zohra
# -----------------------------

import json
from math import sqrt

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

def read_customer_json () :
    customer_cache_file = "/u/kk8/CS373/p2/cs373-netflix/cache.json"
    return json.loads(open(customer_cache_file).read())

def get_movie_avg_rating ():
    '''
        Gets the average rating for a single movie
    '''
    movie_cache_file = "/u/kk8/CS373/p2/cs373-netflix/moviecache.json"
    movie_json=json.loads(open(movie_cache_file).read())
    global current_movie_rating_avg
    current_movie_rating_avg = movie_json[str(current_movie)]["average"]
    global current_movie_period
    current_movie_period = movie_json[str(current_movie)]["period"]

def get_user_avg_rating (customer_json, customer_id) : 
    '''
        Gets the average rating of all the movies rated by the user
        input: customer_id String  
    '''
    return customer_json[customer_id]["average"]

def get_user_period_avg (customer_json, customer_id) :
    if current_movie_period in customer_json[customer_id]:
        return customer_json[customer_id][current_movie_period][0]
    else: 
        return get_user_avg_rating(customer_json, customer_id)

# -----------------
# evaluating rating
# -----------------

def rmse (e, c) :
    v = sum(map(lambda x, y : (x - y) ** 2, e, c))
    return sqrt(v / len(e))

def evaluate_rating(e_rating) :
    correct_ratings = open("RunNetflix.sample.out")
    c_rating = []
    for line in correct_ratings:  
        if ":" not in line:
            c_rating.append(float(line.strip()))
    return rmse(e_rating, c_rating)

# ------------
# netflix_eval
# ------------

def netflix_eval (json, i) :
    estimated_rating = (get_user_period_avg(json, i) + current_movie_rating_avg)/2
    return estimated_rating

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
    customer_json = read_customer_json()
    e_rating = []
    for s in r :
        user = netflix_read(s)
        if user is not -1 :
            rating = netflix_eval(customer_json, user)
            e_rating.append(rating)
            netflix_print(w, str(rating))
        else:
            netflix_print(w, str(current_movie)+":")
    print(evaluate_rating(e_rating))
