import datetime

f = open('hayden_island.txt', 'r')
contents = f.read()
contents = contents.split('\n')

temp = []
for content in contents:
    temp.append(content.split())
contents = temp

def average(contents):
    total = 0
    number_days = 0
    for content in contents:
        content[1] = int(content[1])
        total += content[1]
        number_days += 1
    return total/number_days
# print(average(contents))

def varieance(contents):
    mean = average(contents)
    return sum([(content[1] - mean)**2 for content in contents]) / len(contents)
# print(varieance(contents))

def get_year_total(contents):
    year_total = {}
    for content in contents:
        date = datetime.datetime.strptime(content[0], '%d-%b-%Y')
        year = date.year
        rain_data = int(content[1])
        
        if year in year_total:
            year_total[year] += rain_data
        else:
            year_total[year] = rain_data

    year_total = list(year_total.items())
    return year_total
# print(get_year_total(contents))

def maxi(contents):
    dict_year = get_year_total(contents)

    max_rain = 0 
    max_year = 0 
    for year, rain_average in dict_year:
        if rain_average > max_rain:
            max_rain = rain_average
            max_year = year
    return max_year, max_rain
# print(maxi(contents))

def main():
    data = get_year_total(contents)
        
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.xlabel('year')
    plt.ylabel('rain_max')
    plt.show()
    
main()
