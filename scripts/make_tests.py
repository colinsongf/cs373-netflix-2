#!/usr/bin/env python3

# -----------------------------
# scripts/make_tests.py
# 
# Script used for finding edge
# cases and writing them to RunNetflix.in
# -----------------------------

customer_cache_file = "caches/cache.json"
customer_cache = json.loads(open(customer_cache_file).read())

movie_cache_file = "caches/moviecache.json"
movie_cache = json.loads(open(movie_cache_file).read())

"""
	m : movie id
	c : customer id

	Edge cases : 
		Extreme users - users who give very high ratings
					  - users who give very low ratings
					  - users who only rated a few times
					  - users who have rated many times
					  - users who are rating a certain movie period for the first times
					  - users who is rating for the first time
					  - user that has rated the most
		Extreme movies - movie that is being rated for the first time
					   - movies that have 5.0 ratings
					   - movies that have 1.0 ratings
					   - movies that are at 3.7 (overall rating average for the given data set) ratings
	
	Valid test cases? : 
		Can we inquire about a user who has previously rated the movie?

"""


filename = "RunNetflix.in"
f = open(filename, 'w')

m_c = {}

for m, c_data in m_c:
	f.write(str(m) + ":\n")
	for c in c_data:
		f.write(str(c) + "\n")

f.close()