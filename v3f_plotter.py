import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import plotly.graph_objects as go

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

def find_corresponding_mtvolav(filtered_peaks, new_x_data, new_y_data):
    # Searches the corresponding y-Value in the mt_volav-File (mass-transfer-volume-average) for a given list of peak-tuples.
    # Take the first two tuples from filtered_peaks
    x_values_to_find = [x for x, _ in filtered_peaks[:2]]

    # Find the corresponding y-values for the given x-values
    corresponding_y_values = []
    for x in x_values_to_find:
        try:
            index = new_x_data.index(x)
            corresponding_y_values.append(new_y_data[index])
        except ValueError:
            # If x-value not found in the new_x_data, append None
            corresponding_y_values.append(None)

    return corresponding_y_values

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

    # Create a scatter plot for the peaks with the area under the peaks filled with transparent blue
    peaks_x, peaks_y = zip(*peaks)
    peaks_trace = go.Scatter(
        x=peaks_x,
        y=peaks_y,
        mode='markers',
        marker=dict(color='red', size=10),
        name='Peaks',
        fill='tozeroy',  # Fill the area under the peaks with transparent blue
        fillcolor='rgba(0, 0, 255, 0.3)'  # Set the fill color and transparency (blue with 30% opacity)
    )

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

# Ihre kontinuierlichen Messdaten (x- und y-Werte)
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46])
y_data = np.array([0, 0, 1, 3, 16, 3, 1, 0, 0, 2,0, 0, 1, 3, 6, 3, 1, 0, 0, 2,0, 0, 1, 3, 6, 3, 1, 0, 0, 2,0, 0, 1, 3, 6, 3, 1, 0, 0, 2,3,2,1,0,0,0])

# Extrahieren der Peaks
peaks = extract_peaks(x_data, y_data, threshold=0)

# Ausgabe der Peaks
print("Peaks:", peaks)

mean_y = calculate_mean_y(peaks)
filtered_peaks = remove_outliers(peaks)
print(filtered_peaks)

interplot_xy_values(title="Testdiagramm",xLabel="x",yLabel="y",x_data=x_data,y_data=y_data,peaks=peaks)


print("Mittelwert der y-Werte:", mean_y)
