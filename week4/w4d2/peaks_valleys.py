
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def peaks(data):
    indexs_peak = []
    for i in range(1, len(data)-1):
        # print(f'left: {data[i-1]}, x: {data[i]}, right: {data[i+1]}')
        middle = data[i]
        left = data[i-1]
        right = data[i+1]
        
        if left < middle > right:
            indexs_peak.append(i)
    return indexs_peak
# print(peaks(data))
def valley(data):
    valley_index = []
    for i in range(1, len(data)-1):
        middle = data[i]
        left = data[i-1]
        right = data[i+1]
        if right > middle < left:
            valley_index.append(i)
    return valley_index
# print(valley(data))
def peak_valley(data):
    peak_valley_join = sorted(peaks(data) + valley(data))
    return peak_valley_join
print(peak_valley(data))