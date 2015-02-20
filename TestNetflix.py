#!/usr/bin/env python3

# -------------------------------
# projects/netflix/TestNetflix.py
# Copyright (C) 2014
# Fatimah Zohra, Keerthana Kumar
# -------------------------------

# -------
# imports
# -------
from io import StringIO
from unittest import main, TestCase
from Netflix import *
import json

# -----------
# TestNetflix
# -----------
class TestNetflix (TestCase) :

# ----
# read
# ----
    def test_read (self) :
        s = "3382:\n"
        movie_cache = json.loads('{"3382": {"count": 475, "average": 2.9642105263157896, "period": "1990"}}')
        i = netflix_read(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i[0], -1)
        self.assertEqual(i[1], (3382, 2.9642105263157896, "1990"))


    def test_read_1 (self) :
        s = "10101\n"
        movie_cache = json.loads('{"1": {"count": 1, "average": 1, "period": "1990"}}')
        i = netflix_read(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i[0], "10101")
        self.assertEqual(i[1], -1)


    def test_read_2 (self) :
        s = "4445:\n"
        movie_cache = json.loads('{"8091": {"count": 2127, "average": 4.213916314057358, "period": "2000"}, "4445": {"count": 212, "average": 3.4245283018867925, "period": "2000"}}')
        i = netflix_read(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i[0], -1)
        self.assertEqual(i[1], (4445, 3.4245283018867925, "2000"))

    def test_read_3 (self) :
        s = "4445:abc\n"
        movie_cache = json.loads('{"8091": {"count": 2127, "average": 4.213916314057358, "period": "2000"}, "4445": {"count": 212, "average": 3.4245283018867925, "period": "2000"}}')
        i = netflix_read(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i[0], -1)
        self.assertEqual(i[1], (4445, 3.4245283018867925, "2000"))


# -----
# print
# -----

    def test_print (self) :
        w = StringIO()
        netflix_print(w, "1024:")
        self.assertEqual(w.getvalue(), "1024:\n")

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, "10101")
        self.assertEqual(w.getvalue(), "10101\n")
	
    def test_print_2 (self) :
        w = StringIO()
        netflix_print(w, str(1))
        self.assertEqual(w.getvalue(), "1\n")

    def test_print_3 (self) :
        w = StringIO()
        netflix_print(w, "abc")
        self.assertEqual(w.getvalue(), "abc\n")

# ----
# eval WARNING! These values will change if you refine the algorithm.
# ----

    def test_eval (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (10825, 4.285965942454492, "1990")
        v = netflix_eval(customer_cache, customer_id, movie_details)
        self.assertEqual(v, 4.835120684859536)

    def test_eval_1 (self) :
        customer_cache = json.loads('{"1642779": {"count": 66, "1990": [4.222222222222222, 18], "1980": [4.6, 5], "average": 4.393939393939393, "1970": [4.8, 5], "2000": [4.394736842105263, 38]}}')
        customer_id = "1642779"
        movie_details = (2913,  3.9924890407006504, "2000")
        v = netflix_eval(customer_cache, customer_id, movie_details)
        self.assertEqual(v, 4.529101976715193)

    def test_eval_2 (self) :
        customer_cache = json.loads('{"649512": {"count": 20, "1990": [1.0, 1], "average": 2.85, "2000": [2.888888888888889, 18], "1970": [4.0, 1]}}')
        customer_id = "649512"
        movie_details = (2840,  2.730232558139535, "1970")
        v = netflix_eval(customer_cache, customer_id, movie_details)
        self.assertEqual(v, 3.2978139534883724)

# -----
# read_<customer/answer/movie>_json
# -----

    def test_read_json (self) :
        d = read_customer_json()
        self.assertIs(type(d), dict)

    def test_read_json_1 (self) :
        d = read_answer_json()
        self.assertIs(type(d), dict)

    def test_read_json_1 (self) :
        d = read_movie_json()
        self.assertIs(type(d), dict)

# -----
# get_movie_details
# -----
    def test_movie_details (self) :
        s = 3382
        movie_cache = json.loads('{"3382": {"count": 475, "average": 2.9642105263157896, "period": "1990"}}')
        i = get_movie_details(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i, (3382, 2.9642105263157896, "1990"))
    
    def test_movie_details_1 (self) :
        s = 8091
        movie_cache = json.loads('{"8091": {"count": 2127, "average": 4.213916314057358, "period": "2000"}, "4445": {"count": 212, "average": 3.4245283018867925, "period": "2000"}}')
        i = get_movie_details(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i, (8091, 4.213916314057358, "2000"))
    
    def test_movie_details_2 (self) :
        s = 1
        movie_cache = json.loads('{"1": {"count": 1, "average": 1.000000, "period": "1990"}}')
        i = get_movie_details(movie_cache, s)
        self.assertIs(type(i), tuple)
        self.assertEqual(i, (1, 1.000000, "1990"))


#------
# get_user_avg_rating
#------
    def test_user_avg (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        avg = get_user_avg_rating(customer_cache, customer_id)
        self.assertEqual(avg, 4.451553930530162)
    
    def test_user_avg_1 (self) :
        customer_cache = json.loads('{"1": {"count": 1, "1990": [1.00000, 1], "1980": [1.000000, 1], "average": 1.000000}}')
        customer_id = "1"
        avg = get_user_avg_rating(customer_cache, customer_id)
        self.assertEqual(avg, 1.000000)
    
    def test_user_avg_2 (self) :
        customer_cache = json.loads('{"4": {"average": 4.322}}')
        customer_id = "4"
        avg = get_user_avg_rating(customer_cache, customer_id)
        self.assertEqual(avg, 4.322)
        
#-------
# get_user_period_avg
#-------

    def test_user_period_avg (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 1.000000, "1990")
        avg = get_user_period_avg(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 4.348178137651822)
    

    def test_user_period_avg_1 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 1.000000, "1990")
        avg = get_user_period_avg(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 4.451553930530162)
    
    def test_user_period_avg_2 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 1.000000, "1980")
        avg = get_user_period_avg(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 4.591304347826085)
   
    def test_user_period_avg_3 (self) :
        customer_cache = json.loads('{"1": {"count": 547, "1990": [0, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "1"
        movie_details = (1, 1.000000, "1990")
        avg = get_user_period_avg(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 0)
    
    def test_user_period_avg_4 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 1, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 1.000000, "1700")
        avg = get_user_period_avg(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 1)
    
#-------
# average_factor
#-------
    def test_average_factor (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 1.000000, "1990")
        avg = average_factor(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 1.08)

    def test_average_factor_1 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 3.7400892348473897, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 1.000000, "1990")
        avg = average_factor(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 1.03)

    def test_average_factor_2 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 3.555555555555555, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 3.7, "1990")
        avg = average_factor(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 1.0)

    def test_average_factor_3 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 3.60, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 3.7, "1990")
        avg = average_factor(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 1.0)

    def test_average_factor_4 (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average":1.2555655555555, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (1, 3.7, "1990")
        avg = average_factor(customer_cache, customer_id, movie_details)
        self.assertEqual(avg, 0.98)

#-------
# rmse
#-------
    def test_rmse (self) :
        e = [1, 1, 1, 1]
        c = [1, 1, 1, 1]
        r = rmse(e, c)
        self.assertEqual(r, 0)
    
    def test_rmse_1 (self) :
        e = [1, 1, 1, 1]
        c = [2, 2, 2, 2]
        r = rmse(e, c)
        self.assertEqual(r, 1.0)

    def test_rmse_2 (self) :
        e = [2, 2, 2, 2]
        c = [1, 1, 1, 1]
        r = rmse(e, c)
        self.assertEqual(r, 1.0)

    def test_rmse_3 (self) :
        e = [1, 1, 1, 1]
        c = [1, 2, 3, 4]
        r = rmse(e, c)
        self.assertEqual(r, 1.8708286933869707)

    def test_rmse_4 (self) :
        e = [1]
        c = [1]
        r = rmse(e, c)
        self.assertEqual(r, 0)

#-------
# get_answer
#-------
    
    def test_get_answer (self) :
        answer_cache = json.loads('{"7643": {"1345754": 3, "326619": 4, "1716604": 4, "919032": 4}}')
        customer_id = 919032
        movie_id = 7643
        r = get_answer(answer_cache, customer_id, movie_id)
        self.assertEqual(r, 4)
    
    def test_get_answer_1 (self) :
        answer_cache = json.loads('{"7643": {"1345754": 3, "326619": 4, "1716604": 4, "919032": 4}}')
        customer_id = 1345754
        movie_id = 7643
        r = get_answer(answer_cache, customer_id, movie_id)
        self.assertEqual(r, 3)

    def test_get_answer_2 (self) :
        answer_cache = json.loads('{"7643": {"1345754": 3, "326619": 4, "1716604": 4, "919032": 4}, "1": {"1345754": 3, "326619": 4, "1716604": 4, "919032": 5}}')
        customer_id = 919032
        movie_id = 1
        r = get_answer(answer_cache, customer_id, movie_id)
        self.assertEqual(r, 5)

    def test_get_answer_3 (self) :
        answer_cache = json.loads('{"7643": {"1345754": 3, "326619": 4, "1716604": 4, "919032": 4}, "1": {"1345754": 3, "326619": 4, "1716604": 4, "1": 0}}')
        customer_id = 1
        movie_id = 1
        r = get_answer(answer_cache, customer_id, movie_id)
        self.assertEqual(r, 0)

# -----
# solve
# -----

    def test_solve (self) :
        r = StringIO("1:\n30878\n14756\n2625019\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.8\n3.8\n3.2\nRMSE: 0.20\n")

    def test_solve_1 (self) :
        r = StringIO("1:\n30878\n14756\n2625019\n10:\n1952305\n1531863\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "1:\n3.8\n3.8\n3.2\n10:\n3.2\n3.1\nRMSE: 0.19\n")

    def test_solve_2 (self) :
        r = StringIO("10:\n1952305\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10:\n3.2\nRMSE: 0.21\n")

# ----
# main
# ----

if __name__ == "__main__" :
	main()

