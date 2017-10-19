#!/usr/bin/python

import random
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
def count_random_numbers(sample_size):
    arr_count = []
    for i in range(sample_size):
        arr = []
        for j in range(1001):
            random_int = random.randint(1,1000)
            #print(random_int)
            if arr.count(random_int) < 1:
                arr.append(random_int)
            else:
                arr_length = len(arr)
                print(arr_length)
                arr_count.append(arr_length)
                break
    arr_count.sort()
    #print(arr_count)
    numbers = []
    counts = []
    for number in range(1, arr_count[-1] + 1):
        count = arr_count.count(number)
        numbers.append(number)
        counts.append(count)
        print(number, count)
    sample_name = "Sample size " + str(sample_size)
    return [numbers, counts, sample_name]

samples = []
sizes = [50000, 100000, 500000, 1000000]
for size in sizes:
    samples.append(count_random_numbers(size))

data = []
for sample in samples:
    trace = go.Scatter(
        x = sample[0],
        y = sample[1],
        mode = 'lines',
        name = sample[2]
    )
    data.append(trace)

py.iplot(data, filename='Test-with-1000-side-dice-v0')

