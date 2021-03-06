from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from formatter import extract
from axes_setup import *
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter


rec_iems = ['fqq', 'innerfidelity']  # Can match user input with entries in a database and get a list of names with filenames
iem_filename = ['fqq', 'innerfidelity']
rec_ref = ['harman']
ref_filename = ['harman']
rec_baseline = ''
base_filename = ''
zoom = None
normhz = 1000
normdb = 60

def plot_graph(rec_iems, iem_filename, rec_ref, ref_filename, rec_baseline, base_filename, normhz, normdb, zoom):
    
    iems = []
    ref = []
    
    plt.axvline(x=200, color='k', lw=1)
    plt.axvline(x=2000, color='k', lw=1)

    class iem:
        def __init__ (self, device_name, file_name): # get filename as argument as well
            self.name = device_name # find from phonebook
            self.filename = file_name
            self.x, self.y = extract(self.filename) # replace device_name with self.filename
            try:
                self.f = interp1d(self.x, self.y, kind='linear')
                self.unfilt_new_y = self.f(new_x)
                self.file = 1
            except:
                self.file = 0


    new_x = np.geomspace(20, 20000, 20000)

    # gathering data
    i = 0
    for device in rec_iems:
        iems.append(iem(device, iem_filename[i]))
        if not iems[i].file:
            print(f'Files for {iems[i].name} missing')
            return
        i += 1

    r = 0
    for reference in rec_ref:
        ref.append(iem(reference, ref_filename[r]))
        if not ref[r].file:
            print(f'Files for {ref[r].name} missing')
            return
        r += 1

    #normalizing
    normal = normhz
    at = normdb

    for dev in iems:
        dB_norm = dev.f(normal) - at
        for value in range(len(dev.unfilt_new_y)):
            dev.unfilt_new_y[value] = dev.unfilt_new_y[value] - dB_norm
    
    for reference in ref:
        dB_norm = reference.f(normal) - at
        for value in range(len(reference.unfilt_new_y)):
            reference.unfilt_new_y[value] = reference.unfilt_new_y[value] - dB_norm

    #baselining
    if rec_baseline:
        baseline = iem(rec_baseline, base_filename)
        if not baseline.file:
            print(f'Files for {baseline.name} missing')
            return
        for dev in iems:
            for i in range(len(dev.unfilt_new_y)):
                dev.unfilt_new_y[i] -= baseline.unfilt_new_y[i]
                dev.unfilt_new_y[i] += 60
        for reference in ref:
            for i in range(len(reference.unfilt_new_y)):
                reference.unfilt_new_y[i] -= baseline.unfilt_new_y[i]
                reference.unfilt_new_y[i] += 60

    #plotting data
    for reference in ref:
        new_y = savgol_filter(reference.unfilt_new_y, 301, 3)
        ax = plt.plot(new_x, new_y, lw=2.2, label=reference.name, color='#9ea0a6', linestyle='--')

    for dev in iems:
        new_y = savgol_filter(dev.unfilt_new_y, 301, 3)
        ax = plt.plot(new_x, new_y, lw=2.2, label=dev.name)

    if rec_baseline:
        ax = plt.plot([20, 20000], [60, 60], lw=2.2, label=baseline.name, color='#9ea0a6', linestyle='--')

    plt.xscale("log")

    ax = plt.gca() #getting the current axes
    setter(ax, ticker, plt)

    # zooming
    if zoom == 'bass':
        ax.set_xlim(20, 400)
    elif zoom == 'mids':
        ax.set_xlim(100, 4000)
    elif zoom == 'treble':
        ax.set_xlim(1000, 20000)

    figure = plt.gcf() #getting the entire plotted figure
    figure.set_size_inches(16, 7.45)

    plt.title('Graph')
    plt.xlabel('Frequency')
    plt.ylabel('Decibals')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('plot.png', dpi=100)
    plt.show()

plot_graph(rec_iems, iem_filename, rec_ref, ref_filename, rec_baseline, base_filename, normhz, normdb, zoom)