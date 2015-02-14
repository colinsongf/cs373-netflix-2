import glob, json

root_path = "/u/downing/cs/netflix/"
training_set = root_path + "training_set/*.txt"
user_data = dict()
movie_period = dict()
movie_data = dict()


for line in open("/u/kk8/CS373/p2/movie_titles.txt"):
    line = line.strip()
    data = line.split(",")
    movie = data[0]
    if "NULL" in data[1]:
        movie_period[movie] = "NULL"
    else:
        year = int(data[1])
        movie_period[movie] = str(year//10) + "0"

for movie_file in glob.glob(training_set) :
    f = open(movie_file)
    movie = f.readline().split(":")[0]
    period = movie_period[movie]
    sum_rating = 0
    count = 0
    for line in f:
        d = line.strip().split(",")
        sum_rating += float(d[1])
        count+=1
    movie_data[movie] = {"average": sum_rating/count, "count": count, "period": movie_period[movie]}

#for movie_file in glob.glob(training_set) :
#    f = open(movie_file)
#    movie = f.readline().split(":")[0]
#    period = movie_period[movie]
#    period_string = period + " count"
#    for line in f:
#        line = line.strip()
#        d = line.split(",")
#        if d[0] in user_data:
#            count = user_data[d[0]]["count"]
#            s = user_data[d[0]]["average"]*count
#            s += float(d[1])
#            count += 1
#            user_data[d[0]]["count"] = count 
#            user_data[d[0]]["average"] = s/count
#            if period in user_data[d[0]]:
#                period_avg, period_count = user_data[d[0]][period]
#                period_sum = (period_avg*period_count) + float(d[1])
#                period_count += 1
#                user_data[d[0]][period] = (period_sum/period_count, period_count)
#            else:
#                user_data[d[0]][period] = (float(d[1]), 1)
#        else:
#            user_data[d[0]] = {"count" : 1, "average" : float(d[1]), period: (float(d[1]),1)}

with open("moviecache.json", "w") as outfile:
    json.dump(movie_data, outfile)
