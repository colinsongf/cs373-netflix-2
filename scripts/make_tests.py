#!/usr/bin/env python3

# -----------------------------
# scripts/make_tests.py
#
# Script used for finding edge
# cases and writing them to RunNetflix.in
# -----------------------------

# ----------
#  imports
# ----------
import json

customer_cache_file = "../caches/cache.json"
customer_cache = json.load(open(customer_cache_file))

movie_cache_file = "../caches/moviecache.json"
movie_cache = json.load(open(movie_cache_file))

answer_cache_file = "../caches/pma459-answersCache.json"
answer_cache = json.loads(open(answer_cache_file).read())

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

"""
	m_c : dictionary to write to RunNetflix.in
		  formatted as {movie_id{ customer_id, customer_id, ...}, movie_id{customer_id, ...}, ...}

		  1. Gather movie edge cases
		  2. Gather user edge cases
		  3. Pair them accordingly in m_c
"""
m_c = {}
m_ = set()
c_ = set()

""" Start movie search """
for m, _ in movie_cache.iteritems():
	avg = movie_cache[m]["average"]
	count = movie_cache[m]["count"]
	if( avg >= 4.7): #found: 14961, 7057, 7230
		#m_c[m] = {}
		m_.add(m);
	elif(avg <= 1.3): #found: 515
		m_.add(m)
		#m_c[m] = {}
	elif(round(avg, 1) == 3.7): #found: ... 342, 11916, 13162, 8907, 15394, 9937, 715, ...
		m_.add(m)
		#m_c[m] = {}
	if(count < 10): #found: 13755, 11148
		m_.add(m)
		#m_c[m] = {}

""" Start customer search """
for c, data in customer_cache.iteritems():
	avg = customer_cache[c]["average"]
	count = customer_cache[c]["count"]
	if(count == 1): #way too many results
		c_.add(c)
	elif(count >= 10000): #found: 305344, 2439493, 387418, 2118461, 1664010
		c_.add(c)
	for key, value in data.iteritems():
		if(key[0].isdigit() and value[1] == 1):

			c_.add(c)

""" Start pairing movies to customers n^n^n^n. I'd be fired for writing this. They should just stick this data in a sql db so we can just make joins instead! """
filename = "RunNetflix.in"
fnwrite = open(filename, 'w')

for m in m_:
	padding = 7 - len(m)
	movie_file = "/u/downing/cs/netflix/training_set/mv_" + "0"*padding + m + ".txt"
	f = open(movie_file)
	movie = f.readline() #pass over the movie

	fnwrite.write(str(m) + ":\n") # Write movie name to file
	#m_c[m] = set()
	for line in f:
		line = line.strip()
		d = line.split(",")
		if d[0] in c_ and str(d[0]) in answer_cache[m]:
			fnwrite.write(str(d[0]) + "\n")
			#m_c[m].add(d[0])
	f.close()

"""
for m, c_data in m_c:
	f.write(str(m) + ":\n")
	for c in c_data:
		f.write(str(c) + "\n")
"""

fnwrite.close()
