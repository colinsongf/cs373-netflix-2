import plotly
import json

plotly.tools.set_credentials_file(username='fzohra92', api_key='69jftnfpjg', stream_ids=['jv1ia6gvoy', '30rrunbpeu'])

import plotly.plotly as py
from plotly.graph_objs import *
from datetime import datetime

customer_cache_file = "../caches/cache.json"
customer_json = json.load(open(customer_cache_file))


movie_cache_file = "../caches/moviecache.json"
movie_cache = json.load(open(movie_cache_file))

#--------------
#    Parse
#--------------
"""
    a : rating for the movie
    b : rating date

    x : user count
    y : user average rating

    x1 : movie period
    y1 : movie avg

    x2 : movie count
    y2 : movie avg
"""

x = []
y = []
count = 0
for customer_key, customer_data in customer_json.iteritems():
    if count > 500:
        break
    count += 1
    for count_key , count_value in customer_data.iteritems():
        if(count_key == "count"):
            x.append(count_value)
        elif(count_key == "average"):
            y.append(count_value)

x1 = []
y1 = []
count = 0
for m, _ in movie_cache.iteritems():
    if count < 750:
        avg = movie_cache[m]["average"]
        period = movie_cache[m]["period"]
        x1.append(period)
        y1.append(avg)
        count += 1
    else :
        break

#--------------
#    Trace
#--------------
trace0 = Scatter(x=x, y=y)
trace1 = Scatter(x=x1, y=y1)


#--------------
#    Data
#--------------
data = Data([trace0])
data1 = Data([trace1])


#--------------
#    Layout
#--------------

layout0 = Layout(
    title='Customer Counts x Averages',
    xaxis=XAxis(
        title='count',
        showgrid=True,
        zeroline=True
    ),
    yaxis=YAxis(
        title='average rating',
        showline='True'
    )
)

layout1 = Layout(
    title='Movie Period x Movie Average',
    xaxis=XAxis(
        title='Period',
        showgrid=True,
        showline=True,
    ),
    yaxis=YAxis(
        title='Average',
        showgrid=True,
        showline='True'
    )
)

#--------------
#    Figures
#--------------
fig = Figure(data=data, layout=layout0)
fig1 = Figure(data=data1, layout=layout1)


#--------------
#    Plots
#--------------
plot_url = py.plot(fig, filename='customer-count-avg')
plot_url = py.plot(fig1, filename='movie-period-avg')
