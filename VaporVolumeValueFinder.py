import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def extract_peaks(x_data, y_data, threshold=0):
    # Finden der Peaks mithilfe von scipy.signal.find_peaks
    peaks, _ = find_peaks(y_data, height=threshold)

    # Extrahieren der x- und y-Werte der Peakmaxima als Liste von Tupeln
    peak_coordinates = [(x_data[peaks[i]], y_data[peaks[i]]) for i in range(len(peaks))]

    return peak_coordinates

# Ihre kontinuierlichen Messdaten (x- und y-Werte)
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20])
y_data = np.array([0, 0, 1, 3, 6, 3, 1, 0, 0, 2,0, 0, 1, 3, 6, 3, 1, 0, 0, 2,])

# Extrahieren der Peaks
peaks = extract_peaks(x_data, y_data, threshold=0)

# Ausgabe der Peaks
print("Peaks:", peaks)

# Visualisierung der Daten und Peaks
plt.plot(x_data, y_data, label='Messdaten')
plt.plot(*zip(*peaks), 'ro', label='Peaks')
plt.legend()
plt.xlabel('x-Werte')
plt.ylabel('y-Werte')
plt.show()

def calculate_mean_y(peaks):
    # Überprüfen, ob die Liste nicht leer ist, um Division durch Null zu vermeiden
    if not peaks:
        return None

    # Berechnen des Mittelwerts der y-Werte
    sum_y = sum(y for _, y in peaks)
    mean_y = sum_y / len(peaks)

    return mean_y

# Beispiel Peaks
peaks = [(1, 5), (2, 7), (3, 3), (4, 9), (5, 6)]

# Aufruf der Funktion und Ausgabe des Mittelwerts
mean_y = calculate_mean_y(peaks)
print("Mittelwert der y-Werte:", mean_y)
