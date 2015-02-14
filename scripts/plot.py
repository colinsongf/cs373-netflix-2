import plotly
import json

plotly.tools.set_credentials_file(username='fzohra92', api_key='69jftnfpjg', stream_ids=['jv1ia6gvoy', '30rrunbpeu'])

import plotly.plotly as py
from plotly.graph_objs import *

customer_cache_file = "../cs373-netflix/cache.json"
customer_json = json.load(open(customer_cache_file))

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

"""
    x : count
    y : average rating
"""

trace0 = Scatter(x=x, y=y)


data = Data([trace0])

layout = Layout(
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
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='line-style')

#unique_url = py.plot(data, filename = 'basic-line')
