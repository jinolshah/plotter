from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import formatter
from scipy.signal import savgol_filter

# print(plt.style.available)
# plt.xkcd()
# plt.style.use('seaborn-dark')

todo = ['harman.txt', 'zk.txt', 'hh.txt']

for chart in todo:
    formatter.clear(chart)

    x=formatter.axisx
    y=formatter.axisy

    yhat = savgol_filter(y, 51, 8)

    ax = plt.plot(x, yhat, lw=2, label=chart)
    formatter.axisx.clear()
    formatter.axisy.clear()


majorvalues = [0, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 
600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 20000]
majorlabels = [0, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 
600, 800, '1k', '1.5k', '2k', '3k', '4k', '5k', '6k', '8k', '10k', '15k', '20k']
majorvaluey = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

plt.xscale("log")

ax = plt.gca()
ax.xaxis.set_major_locator(ticker.FixedLocator((majorvalues)))
ax.xaxis.set_major_formatter(ticker.FixedFormatter((majorlabels)))
ax.set_xlim(20, 20000)

ax.yaxis.set_major_locator(ticker.FixedLocator((majorvaluey)))
ax.yaxis.set_major_formatter(ticker.FixedFormatter((majorvaluey)))
ax.set_ylim(30, 85)

zoom = input('Zoom: ')

if zoom == 'bass':
    ax.set_xlim(20, 400)
elif zoom == 'mids':
    ax.set_xlim(100, 4000)
elif zoom == 'treble':
    ax.set_xlim(1000, 20000)

plt.axvline(x=200, color='k', lw=1)
plt.axvline(x=2000, color='k', lw=1)

figure = plt.gcf()
figure.set_size_inches(16, 7.45)

plt.title('Graph')
plt.xlabel('Frequency')
plt.ylabel('Decibals')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.savefig('plot.png', dpi=100)
plt.show()