xs = [1,2,3,4,5]
def search(xs, number):
    minimum = 0
    maximum = len(xs) - 1  
    while (minimum <= maximum):
        average = int((minimum+maximum) /2)
        if (xs[average] == number):
            return average
        elif (xs[average] < number):
            minimum = average + 1
        else:
            maximum = average - 1
            
    return -1
print(search(xs, 5))