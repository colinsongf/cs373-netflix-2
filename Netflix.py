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
        current_movie = int(s.split(":")[0])
        movie_details = get_movie_avg_rating(movie_json, current_movie)
        return (-1, movie_details)
    else:
        return (s.strip(), -1)

# ------------
# data_collection
# ------------

def read_customer_json () :
    customer_cache_file = "caches/cache.json"
    return json.loads(open(customer_cache_file).read())

def read_movie_json () :
    movie_cache_file = "caches/moviecache.json"
    return json.loads(open(movie_cache_file).read())

def get_movie_avg_rating (movie_json, current_movie) :
    '''
        Gets the average rating for a single movie
        Return: tuple with current movie, rating average and period
    '''
    current_movie_rating_avg = movie_json[str(current_movie)]["average"]
    current_movie_period = movie_json[str(current_movie)]["period"]
    return (current_movie, current_movie_rating_avg, current_movie_period)

def get_user_avg_rating (customer_json, customer_id) : 
    '''
        Gets the average rating of all the movies rated by the user
        input: customer_id String  
    '''
    return customer_json[customer_id]["average"]

def get_user_period_avg (customer_json, customer_id, movie_detail) :
    if movie_detail[2] in customer_json[customer_id]:
        return customer_json[customer_id][movie_detail[2]][0]
    else: 
        return get_user_avg_rating(customer_json, customer_id)

def average_factor (customer_json, customer_id):
    """
        hypothesis: if the overall average is lower for large counts then the factor should be < 0, else > 1
        
        small improvement from 0.9741 to 0.9598
    """

    avg = customer_json[customer_id]["average"]
    if(avg > 4):
        return 1.08
    elif(avg > 3.60):
        return 1.03
    elif(avg > 3.50):
        return 1.0
    else:
        return 0.98

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

    return rmse(e_rating, c_rating)

# ------------
# netflix_eval
# ------------

def netflix_eval (json, i, movie_detail) :
    """
        Evaluate the estimated rating for a user
    """

    estimated_rating_based_on_period = (get_user_period_avg(json, i, movie_detail) + movie_detail[1])/2
    estimated_rating_factoring_in_count_average = estimated_rating_based_on_period * average_factor(json, i)
    return estimated_rating_factoring_in_count_average

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
    movie_detail = ()
    for s in r :
        user = netflix_read(movie_json, s)
        if user[0] is not -1 :
            rating = netflix_eval(customer_json, user[0], movie_detail)
            e_rating.append(rating)
            netflix_print(w, str(rating))
        else:
            movie_detail = user[1]
            netflix_print(w, str(movie_detail[0])+":")



    print(evaluate_rating(e_rating))
