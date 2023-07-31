import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import plotly.graph_objects as go

class xyDataFile:
    def __init__():
        self.filename = filename
        self.type_of_file = type_of_file
        self.xdata = xdata
        self.ydata = ydata
        self.zdata = zdata

    def open_datafile(file):
        with open(file) as inputfile:
            #Fügt den filenamen als Attribut self.filename hinzu.add()
            #Erste Zeile = self.type

    def __repr__(self):
        return (
            self.__class__.__name__ + f"(id={self.id!r}, name={self.name!r}, admin={self.admin!r})"
        )    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.name, self.admin) == (
                other.id,
                other.name,
                other.admin,
            )
        return NotImplemented


def open_mt_volav_file():
    pass

def open_vapor_volume_rt_file():
    pass

def extract_peaks(x_data, y_data, threshold=0):
    # Finden der Peaks mithilfe von scipy.signal.find_peaks
    peaks, _ = find_peaks(y_data, height=threshold)

    # Extrahieren der x- und y-Werte der Peakmaxima als Liste von Tupeln
    peak_coordinates = [(x_data[peaks[i]], y_data[peaks[i]]) for i in range(len(peaks))]

    return peak_coordinates

def calculate_mean_y(peaks):
    # Überprüfen, ob die Liste nicht leer ist, um Division durch Null zu vermeiden
    if not peaks:
        return None

    # Berechnen des Mittelwerts der y-Werte
    sum_y = sum(y for _, y in peaks)
    mean_y = sum_y / len(peaks)

    return mean_y

def is_outlier(y, mean_y, std_dev):
    outlier = abs(y - mean_y) > 2 * std_dev
    return outlier

def remove_outliers(peaks):
    if not peaks:
        return []

    # Berechnen des Mittelwerts der y-Werte
    sum_y = sum(y for _, y in peaks)
    mean_y = sum_y / len(peaks)

    # Berechnen der Standardabweichung der y-Werte
    std_dev = (sum((y - mean_y) ** 2 for _, y in peaks) / len(peaks)) ** 0.5

    # Filtern der Tupel, um Ausreißer zu entfernen
    filtered_peaks = [(x, y) for x, y in peaks if not is_outlier(y, mean_y, std_dev)]

    return filtered_peaks

def plot_xy_values(title,xLabel,yLabel,x_data,y_data):
    plt.plot(x_data, y_data, label='Messdaten')
    plt.plot(*zip(*peaks), 'ro', label='Peaks')

    # Labeln der Peaks mit Nummern und x-Werten
    for i, (x_peak, y_peak) in enumerate(peaks):
        plt.text(x_peak, y_peak, f"Peak {i+1}", fontsize=12, fontweight='bold', ha='center', va='bottom')
        plt.text(x_peak, y_peak - 0.5, f"x={x_peak}", fontsize=10, ha='center', va='top')

    plt.legend()
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def interplot_xy_values(title, xLabel, yLabel, x_data, y_data, peaks):
    # Create an interactive plot of the xy-data with peaks labeled inside the Webbrowser. Opens a new tab inside the browser.
    # Uses plotly as library.
    line_trace = go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Messdaten', line=dict(color='blue'))

    # Create a scatter plot for the peaks
    peaks_x, peaks_y = zip(*peaks)
    peaks_trace = go.Scatter(x=peaks_x, y=peaks_y, mode='markers', marker=dict(color='red', size=10), name='Peaks')

    # Labeling the peaks with numbers and x-values
    annotations = [dict(
        x=x_peak,
        y=y_peak,
        xref='x',
        yref='y',
        text=f"Peak {i+1}<br>x={x_peak}",
        showarrow=True,
        arrowhead=3,
        ax=0,
        ay=-30,
        font=dict(size=12)
    ) for i, (x_peak, y_peak) in enumerate(peaks)]

    layout = go.Layout(
        title=title,
        xaxis=dict(title=xLabel),
        yaxis=dict(title=yLabel),
        showlegend=True,
        annotations=annotations
    )

    fig = go.Figure(data=[line_trace, peaks_trace], layout=layout)
    fig.show()



#================ TESTING SECTION ============================================================================
