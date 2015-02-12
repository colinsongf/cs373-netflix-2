#!/usr/bin/env python3

# -----------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2015
# Keerthana Kumar, Fatimah Zohra
# -----------------------------

# ---------------
# global variable
# ---------------
current_movie = ""

# ------------
# netflix_read
# ------------

def netflix_read (s) :
    if ":" in s :
        current_movie = s.split(":")[0]
        return -1
    else:
        return s.strip()

# ------------
# netflix_eval
# ------------

def netflix_eval (i, j) :
    

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
            netflix_print(w, current+":")
