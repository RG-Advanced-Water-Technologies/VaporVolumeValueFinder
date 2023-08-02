import re
import os
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import plotly.graph_objects as go

class Wertepaar:
  """
  Eine Klasse, die Ansys-Simulationsdaten darstellt.

  Attributes:
    filename: Dateipfad und Name der Datei.
    type_of_file: Art der Datei aus erster Zeile ausgelesen (Mass-transfer oder Vapor volume).
    x_data: Werte der ersten Spalte.
    y_data: Werte der zweiten Spalte.
    z_data: Werte der dritten Spalte.
  """

  def __init__(self, filename=None, type_of_file=None, x_data=None, y_data=None, z_data=None):
    self.x_data = x_data
    self.y_data = y_data
    self.z_data = z_data
    self.filename = filename
    self.type_of_file = type_of_file

  #def __repr__(self):
  #  return f"Person(Filename={self.filename}, Type_of_file={self.type_of_file}, x_data={self.x_data}, value={self.value}, time={self.time})"

  #def __str__(self):
  #  return f"Filename={self.filename}, Type_of_file={self.type_of_file}, x_data: {self.x_data}, value: {self.value}, Zeit: {self.time}"



def read_file_to_persons(file_value):
  """
  Liest den Inhalt einer Textdatei ein und erstellt eine Liste von Daten.

  Args:
    file_value: Der Pfad der Textdatei.

  Returns:
    Eine Liste von Daten.
  """
  wertepaare = []
  filename=str(file_value)
  with open(file_value, 'r') as f:
    line_number = 0
    for line in f:
      if line_number == 0:
        type_of_file = line.strip()[1:-1]
      elif line_number == 1:
        pass
      elif line_number == 2:
        pass
      else:
        x_data, y_data, z_data = line.split()
        wertepaare.append(Wertepaar(filename, type_of_file, x_data, y_data, z_data))
      #if line_number in range(3,10):
        #x_data, value, time = line.split()
        #wertepaare.append(Wertepaar(x_data, value, time))
      line_number += 1
    return wertepaare
  
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

def plot_xy_values(title,xLabel,yLabel,x_data,y_data, peaks):
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


if __name__ == "__main__":
  file_value = r"C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out"
  wertepaare = read_file_to_persons(file_value)
  #wertepaare = read_file_to_persons('C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out')
  print('One')
  for wertepaar in wertepaare:
    print(Wertepaar.__dict__)
  print('Two')
  

