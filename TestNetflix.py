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

# ----
# eval WARNING! These values will change if you refine the algorithm.
# ----

    def test_eval (self) :
        customer_cache = json.loads('{"378466": {"count": 547, "1990": [4.348178137651822, 247], "1980": [4.591304347826085, 115], "average": 4.451553930530162, "1960": [4.769230769230769, 13], "1970": [4.696969696969697, 33], "2000": [4.423357664233579, 137], "1950": [5.0, 2]}}')
        customer_id = "378466"
        movie_details = (10825, 4.285965942454492, "1990")
        v = netflix_eval(customer_cache, customer_id, movie_details)
        self.assertEqual(v, 4.66243780325741)

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

"""
# -----
# solve
# -----

    def test_solve (self) :
        r = StringIO()
        w = StringIO()
        netflix_solve(r, w)
"""

# ----
# main
# ----

if __name__ == "__main__" :
	main()
