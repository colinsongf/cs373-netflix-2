#!/usr/bin/env python3

# -----------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Keerthana Kumar, Fatimah Zohra
# -----------------------------

import json
from math import sqrt

PRINT=True

# ------------
# netflix_read
# ------------

def netflix_read (movie_json, s) :
    if ":" in s :
        global current_movie
        current_movie = int(s.split(":")[0])
        get_movie_avg_rating(movie_json)
        return -1
    else:
        return s.strip()

# ------------
# data_collection
# ------------

def read_customer_json () :
    customer_cache_file = "cache.json"
    return json.loads(open(customer_cache_file).read())

def read_movie_json () :
    movie_cache_file = "moviecache.json"
    return json.loads(open(movie_cache_file).read())

def get_movie_avg_rating (movie_json) :
    '''
        Gets the average rating for a single movie
    '''
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

def average_factor (customer_json, customer_id):
    """
        hypothesis: if the overall average is lower for large counts then the factor should be < 0, else > 1
        
        small improvement from 0.9741 to 0.9631
    """
    avg = customer_json[customer_id]["average"]
    if(avg > 4):
        return 1.1
    elif(avg > 3.5):
        return 1.05
    else:
        return 0.95

# -----------------
# evaluating rating
# -----------------

def rmse (e, c) :
    v = sum(map(lambda x, y : (x - y) ** 2, e, c))
    return sqrt(v / len(e))

def evaluate_rating(e_rating) :
    """
        Evaluate the accuracy of the rating by calculating the rmse for
        the expected rating and the correct (actual) rating

    """
    #correct_ratings = open("correct_sample.txt")
    correct_ratings = open("/u/mck782/netflix-tests/jms6879-expected-ratings.txt")
    c_rating = []
    for line in correct_ratings:  
        if ":" not in line:
            c_rating.append(float(line.strip()))

    """
    print("Correct ratings:")
    for c in c_rating:
        print(c)

    print("Evaluated readings")
    for e in e_rating:
        print(e)
    """
    return rmse(e_rating, c_rating)

# ------------
# netflix_eval
# ------------

def netflix_eval (json, i) :
    """
        Evaluate the estimated rating for a user
    """
    estimated_rating_based_on_period = (get_user_period_avg(json, i) + current_movie_rating_avg)/2
    estimated_rating_factoring_in_count_average = estimated_rating_based_on_period * average_factor(json, i)
    return estimated_rating_factoring_in_count_average
    #return estimated_rating_based_on_period
# -------------
# netflix_print
# -------------

def netflix_print (w, s) :
    if (PRINT):
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
    movie_json = read_movie_json()
    e_rating = []
    
    for s in r :
        user = netflix_read(movie_json, s)
        if user is not -1 :
            rating = netflix_eval(customer_json, user)
            e_rating.append(rating)
            netflix_print(w, str(rating))
        else:
            netflix_print(w, str(current_movie)+":")



    print(evaluate_rating(e_rating))
