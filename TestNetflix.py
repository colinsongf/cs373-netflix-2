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
"""
# ----
# eval
# ----

    def test_eval (self) :
		#global variables making it difficult to unit test
        cache = json.dumps({"1" : {"count": 1, "1990": [5.0, 1], "1980": [5.0, 1], "2000": [5.0, 1]}})
        customer_id = 1
        v = netflix_eval(cache, 1)
        self.assertEqual(v, 20)

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
