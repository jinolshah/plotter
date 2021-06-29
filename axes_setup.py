majorvaluex = [0, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 
600, 800, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 8000, 10000, 15000, 20000]

majorlabels = [0, 20, 30, 40, 50, 60, 80, 100, 150, 200, 300, 400, 500, 
600, 800, '1k', '1.5k', '2k', '3k', '4k', '5k', '6k', '8k', '10k', '15k', '20k']

majorvaluey = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

def setter(ax, ticker, plt):
    ax.xaxis.set_major_locator(ticker.FixedLocator((majorvaluex)))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter((majorlabels)))
    ax.set_xlim(20, 20000)

    ax.yaxis.set_major_locator(ticker.FixedLocator((majorvaluey)))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter((majorvaluey)))
    ax.set_ylim(30, 85)
