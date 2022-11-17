dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
result = {}

for x in range(0, len(dates)):
    result[dates[x]] = rates[x] 

print(result)