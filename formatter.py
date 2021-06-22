import re
import os

def shaper(readings, direction, x, y):
    with open(f"data/{readings}{direction}.txt", 'r') as mid:
            for line in mid:
                data = re.findall('\d*\.?\d+', line)
                if len(data) == 2:
                    x.append(float(data[0]))
                    y.append(float(data[1]))
    return x, y

def extract(readings):
    axisx = []
    axisy = []
    axisx_R = []
    axisy_R = []
    axisx_L = []
    axisy_L = []

    try:
        shaper(readings, '', axisx, axisy)
        return axisx, axisy

    except:
        try:
            shaper(readings, ' R', axisx_R, axisy_R)
            try:
                shaper(readings, ' L', axisx_L, axisy_L)
                for k in range(len(axisx_R)):
                    axisx.append((axisx_R[k] + axisx_L[k])/2)
                    axisy.append((axisy_R[k] + axisy_L[k])/2)
                return axisx, axisy
            except:
                return axisx_R, axisy_R
        
        except:
            try:
                shaper(readings, ' L', axisx_L, axisy_L)
                return axisx_L, axisy_L
            except:
                return None, None