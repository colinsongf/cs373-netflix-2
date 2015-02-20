#!/usr/bin/env python3

# -----------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Keerthana Kumar, Fatimah Zohra
# -----------------------------

import json
from numpy import mean, sqrt, square, subtract
#from math import sqrt

# ------------
# netflix_read
# ------------

def netflix_read (movie_json, s) :
    """
    Read line, determine movie or user
    Input: movie_json a pre computed file with information about all the movies, s a string
    Return: Tuple for a movie (-1, movie_details) and for a user (user_id, -1)
    """
    if ":" in s :
        current_movie = int(s.split(":")[0])
        assert current_movie > 0
        assert current_movie <= 17770
        movie_details = get_movie_details(movie_json, current_movie)
        return (-1, movie_details)
    else :
        return (s.strip(), -1)

# ------------------
# read_customer_json
# ------------------

def read_customer_json () :
    """
    Loads the user_cache created by kk24268
    Return: dictionary of the user_cache
    """
    customer_cache_file = "/u/mck782/netflix-tests/kk24268-AvgUseCache.json"
    file_read = open(customer_cache_file, "r")
    json_obj = json.loads(file_read.read())
    file_read.close()
    return json_obj

# ------------------
# read_answer_json
# ------------------

def read_answer_json () :
    """
    Loads the answer_cache created by kk24268
    Return: dictionary of the answer_cache
    """
    answer_cache_file = "/u/mck782/netflix-tests/pma459-answersCache.json"
    file_read = open(answer_cache_file, "r")
    json_obj = json.loads(file_read.read())
    file_read.close()
    return json_obj

# ---------------
# read_movie_json
# ---------------

def read_movie_json () :
    """
    Loads the movie_cache created by kk24268
    Return: dictionary of the movie_cache
    """
    movie_cache_file = "/u/mck782/netflix-tests/kk24268-AvgMovieCache.json"
    file_read = open(movie_cache_file, "r")
    json_obj = json.loads(file_read.read())
    file_read.close()
    return json_obj

# -----------------
# get_movie_details
# -----------------

def get_movie_details (movie_json, current_movie) :
    """
    Gets movie's average rating and period
    Input: movie_json containing the cache, current_movie int of the current movie
    Return: tuple with current movie, rating average and period
    """
    assert str(current_movie) in movie_json
    assert "average" in movie_json[str(current_movie)]
    assert "period" in movie_json[str(current_movie)]
    current_movie_rating_avg = movie_json[str(current_movie)]["average"]
    current_movie_period = movie_json[str(current_movie)]["period"]
    movie_detail = (current_movie, current_movie_rating_avg, current_movie_period)
    assert len(movie_detail) == 3
    return movie_detail

# -------------------
# get_user_avg_rating
# -------------------

def get_user_avg_rating (customer_json, customer_id) :
    """
    Gets the average rating of all the movies rated by the user
    Input: customer_json the cache of the users, customer_id string of the user
    Return: average customer rating
    """
    assert customer_id in customer_json
    assert "average" in customer_json[customer_id]
    return customer_json[customer_id]["average"]

# -------------------
# get_user_period_avg
# -------------------

def get_user_period_avg (customer_json, customer_id, movie_detail) :
    """
    Gets the average rating of all the movies rated by the user in the period or calls get_user_avg_rating if period doesn't exist
    Input: customer_json the cache of the users, customer_id string of the user, movie_detail
    Return: average customer rating of period/user
    """
    assert len(movie_detail) == 3
    assert customer_id in customer_json
    if movie_detail[2] in customer_json[customer_id] :
        return customer_json[customer_id][movie_detail[2]][0]
    else :
        return get_user_avg_rating(customer_json, customer_id)

# --------------
# average_factor
# --------------

def average_factor (customer_json, customer_id, movie_detail) :
    """
    Idea: if the overall average is lower for large counts then the factor should be < 0, else > 1
    Input: customer_json the cache of users
    Return: averaging factor based on prior study
    """
    # improvement from 0.9741 to 0.9598
    assert len(movie_detail) == 3
    assert customer_id in customer_json
    assert "average" in customer_json[customer_id]
    avg = customer_json[customer_id]["average"]
    factor = 0
    if movie_detail[2] != "NULL":
        period = int(movie_detail[2])
    else:
        period = 0

    if period == 2000 and int(movie_detail[1]) > 3.0:
        factor = 0.06
    elif period == 1990 and int(movie_detail[1]) > 3.0:
        factor = 0.04
    elif period == 1940 and int(movie_detail[1]) > 3.0:
        factor = 0.05
    elif period == 1930 and int(movie_detail[1]) > 3.0:
        factor = 0.05
    elif period == 1920 and int(movie_detail[1]) > 3.0:
        factor = 0.15

    if(avg > 4) :
        factor += 1.08
    elif(avg > 3.60) :
        factor += 1.03
    elif(avg > 3.50) :
        factor += 1.0
    else :
        factor += 0.98
    return factor


# -----------------
# period_avg_fit
# -----------------
def period_average_fit (movie_detail) :
    """
    Idea: y = (-0.00566)*x + (14.4)
          x = period, y = average rating
    Input: movie_json and movie_id
    Return: period factor based on prior study
    """
    if movie_detail[2] == 'NULL':
        return -1
    else:
        return ((-0.00566)*int(movie_detail[2]) + (14.4))


# -----------------
# evaluating rating
# -----------------

def rmse (e, c) :
    """
    Calculates the root mean square error between two lists
    Input: e list, c list
    Return: rmse float
    """
    assert len(e) == len(c)
    return sqrt(mean(square(subtract(e,c))))

# ----------
# get_answer
# ----------

def get_answer (answer_json, customer_id, movie) :
    """
    Collects the correct answer from the answers_cache
    Input: answer_json cache of the answers, customer_id int, movie int
    Return: rating
    """
    assert str(movie) in answer_json
    assert str(customer_id) in answer_json[str(movie)], "ERROR "+ str(customer_id) +" "+  str(movie)
    return answer_json[str(movie)][str(customer_id)]


# ------------
# netflix_eval
# ------------

def netflix_eval (json, i, movie_detail) :
    """
    Evaluate the estimated rating for a user
    Input: json  with the user information, customer_id, movie detail - tuple
    Return: estimated rating
    """
    assert len(movie_detail) == 3
    estimated_rating_based_on_period = (get_user_period_avg(json, i, movie_detail) + movie_detail[1])/2
    estimated_rating_factoring_in_count_average = estimated_rating_based_on_period * average_factor(json, i, movie_detail)
    return estimated_rating_factoring_in_count_average

# -------------
# netflix_print
# -------------

def netflix_print (w, s) :
    """
    Print string in writer
    Input: w writer, s string
    """
    assert type(s) == str
    if (True):
        w.write(s + "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    Main function solver
    Input: r a reader, w a writer
    """
    customer_json = read_customer_json()
    movie_json = read_movie_json()
    answer_json = read_answer_json()
    e_rating = []
    c_rating = []
    movie_detail = ()
    for s in r :
        user = netflix_read(movie_json, s)
        if user[0] is not -1 :
            rating = netflix_eval(customer_json, user[0], movie_detail)
            c_rating.append(get_answer(answer_json, user[0], movie_detail[0]))
            e_rating.append(rating)
            netflix_print(w, str(round(rating, 1)))
        else:
            movie_detail = user[1]
            netflix_print(w, str(movie_detail[0])+":")


    dec, flo = str(rmse(e_rating, c_rating)).split(".")
    rms = '.'.join((dec, flo[0:2]))

    netflix_print(w, "RMSE: "+ rms)
