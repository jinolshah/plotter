import re

axisx = []
axisy = []

def clear(reading):
    file = open(reading, 'r')
    for shit in file:
        data = re.findall('\d*\.?\d+',shit)
        if len(data) == 2:
            axisx.append(float(data[0]))
            axisy.append(float(data[1]))