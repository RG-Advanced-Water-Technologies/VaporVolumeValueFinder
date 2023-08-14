# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
VaporVolumeFinder (V3F) - v1.0.0 Build 0001

Name: VaporVolumeFinder.py
Authors: Christian Beringer, Westdale94
Product Owner: BaconBeaver
Date: July 31, 2023

Created for usage inside "UltraStaRK" - a project of Thuringia Water Innovation Cluster (ThWIC)
For more information visit: https://www.thwic.uni-jena.de/projekte/ultrastark

This script is licensed under the Mozilla Public License v2.0

Description:
"""

import re
import os
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import plotly.graph_objects as go


class XyzDataFile:
    """
    Represents a data file containing XYZ data.

    This class is designed to store and manipulate data from an XYZ data file. It provides attributes to store the
    filename, type of file, variable names, units, and data points for the X, Y, and Z axes.

    Attributes:
        filename (str): The name of the data file.
        type_of_file (str): The type of the data file (e.g., 'text', 'csv', 'binary').
        x_var (str): The name of the variable associated with the X-axis data.
        y_var (str): The name of the variable associated with the Y-axis data.
        z_var (str): The name of the variable associated with the Z-axis data.
        x_unit (str): The unit of measurement for the X-axis data.
        y_unit (str): The unit of measurement for the Y-axis data.
        z_unit (str): The unit of measurement for the Z-axis data.
        xdata (list): A list of numerical values representing data points along the X-axis.
        ydata (list): A list of numerical values representing data points along the Y-axis.
        zdata (list): A list of numerical values representing data points along the Z-axis.

    Methods:
        __repr__(self): Returns a string representation of the XyzDataFile object.
    """
    def __init__(self, filename=None,type_of_file=None,x_var=None,y_var=None,z_var=None,x_unit=None,y_unit=None,z_unit=None,xdata=None,ydata=None,zdata=None):
        # Initialize instance variables with default values
        self.filename = str(filename)
        self.type_of_file = str(type_of_file)
        self.x_var = str(x_var)
        self.y_var = str(y_var)
        self.z_var = str(z_var)
        self.x_unit = str(x_unit)
        self.y_unit = str(y_unit)
        self.z_unit = str(z_unit)
        self.xdata = []
        self.ydata = []
        self.zdata = []

    def __repr__(self):
        return f"XyzDataFile(filename='{self.filename}', type_of_file='{self.type_of_file}', " \
                f"x_var='{self.x_var}', y_var='{self.y_var}', z_var='{self.z_var}', " \
                f"x_unit='{self.x_unit}', y_unit='{self.y_unit}', z_unit='{self.z_unit}', " \
                f"xdata={self.xdata}, ydata={self.ydata}, zdata={self.zdata})"

    # Setter methods
    def set_filename(self, filename):
        # Set the filename attribute with the provided value
        self.filename = str(filename)

    # Other setter methods follow a similar pattern

class OUfile_Parser(XyzDataFile):
    def __init__(self,file_path=None):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__()
        self.file_path = file_path
    def set_filename(self, file_path):
        # Set the filename attribute by extracting the base name from the file path
        filename = os.path.basename(file_path)
        return filename
    def read_datafile(self,filepath):
        # Read data from the specified file and populate xdata, ydata, and zdata lists
        with open(filepath, "r") as file:
            lines = file.readlines()
            line_number = 0
            for line in lines:
                if line_number == 0:
                    # Remove quotes from the type_of_file
                    type_of_file = line.strip()[1:-1]
                elif line_number == 1:
                    pass
                elif line_number == 2:
                    # Extract variable names from the third line using regex
                    valuenames = re.findall(r'"(.*?)"', line)
                    x_var = valuenames[0]
                    y_var = valuenames[1]
                    z_var = valuenames[2]
                else:
                    # Split the line and convert data to float, then add to respective lists
                    xdata,ydata,zdata = line.split()
                    #xyzdata = line.split()
                    self.xdata.append(float(xdata))
                    self.ydata.append(float(ydata))
                    self.zdata.append(float(zdata))
                line_number += 1

class XyzDataFile2:
    """
    Represents a second data file containing XYZ-2 data.

    """
    def __init__(self, filename2=None,type_of_file2=None,x_var2=None,y_var2=None,z_var2=None,x_unit2=None,y_unit2=None,z_unit2=None,xdata2=None,ydata2=None,zdata2=None):
        # Initialize instance variables with default values
        self.filename2 = str(filename2)
        self.type_of_file2 = str(type_of_file2)
        self.x_var2 = str(x_var2)
        self.y_var2 = str(y_var2)
        self.z_var2 = str(z_var2)
        self.x_unit2 = str(x_unit2)
        self.y_unit2 = str(y_unit2)
        self.z_unit2 = str(z_unit2)
        self.xdata2 = []
        self.ydata2 = []
        self.zdata2 = []

    def __repr__(self):
        return f"XyzDataFile(filename='{self.filename2}', type_of_file='{self.type_of_file2}', " \
                f"x_var='{self.x_var2}', y_var='{self.y_var2}', z_var='{self.z_var2}', " \
                f"x_unit='{self.x_unit2}', y_unit='{self.y_unit2}', z_unit='{self.z_unit2}', " \
                f"xdata={self.xdata2}, ydata={self.ydata2}, zdata={self.zdata2})"

    # Setter methods
    def set_filename(self, filename2):
        # Set the filename attribute with the provided value
        self.filename2 = str(filename2)

    # Other setter methods follow a similar pattern

class OUfile_Parser2(XyzDataFile2):
    def __init__(self,file_path2=None):
        # Call the parent class constructor to initialize inherited attributes
        super().__init__()
        self.file_path2 = file_path2
    def set_filename2(self, file_path2):
        # Set the filename attribute by extracting the base name from the file path
        filename2 = os.path.basename(file_path2)
        return filename2
    def read_datafile2(self,filepath2):
        # Read data from the specified file and populate xdata, ydata, and zdata lists
        with open(filepath2, "r") as file:
            lines = file.readlines()
            line_number = 0
            for line in lines:
                if line_number == 0:
                    # Remove quotes from the type_of_file
                    type_of_file = line.strip()[1:-1]
                elif line_number == 1:
                    pass
                elif line_number == 2:
                    # Extract variable names from the third line using regex
                    valuenames = re.findall(r'"(.*?)"', line)
                    x_var2 = valuenames[0]
                    y_var2 = valuenames[1]
                    z_var2 = valuenames[2]
                else:
                    # Split the line and convert data to float, then add to respective lists
                    xdata2,ydata2,zdata2 = line.split()
                    #xyzdata = line.split()
                    self.xdata2.append(float(xdata2))
                    self.ydata2.append(float(ydata2))
                    self.zdata2.append(float(zdata2))
                line_number += 1
                


def extract_peaks(x_data, y_data, threshold=0):
    # Finden der Peaks mithilfe von scipy.signal.find_peaks
    peaks, _ = find_peaks(y_data, height=threshold, distance=150, width=20)
   
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
    outlier = abs(y - mean_y) > 10 * std_dev
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

def find_corresponding_mtvolav(filtered_peaks, x_data2, y_data2):
    # Searches the corresponding y-Value in the mt_volav-File (mass-transfer-volume-average) for a given list of peak-tuples.
    # Take the first two tuples from filtered_peaks
    x_values_to_find = [x for x, _ in filtered_peaks[:20]]

    # Find the corresponding y-values for the given x-values
    corresponding_y_values = []
    for x in x_values_to_find:
        try:
            index = x_data2.index(x)
            corresponding_y_values.append(y_data2[index])
        except ValueError:
            # If x-value not found in the new_x_data, append None
            corresponding_y_values.append(None)

    return corresponding_y_values

def plot_xy_values(title,xLabel,yLabel,x_data,y_data):
    plt.plot(x_data, y_data, label='Messdaten')
    plt.plot(*zip(*filtered_peaks), 'ro', label='Peaks')

    # Labeln der Peaks mit Nummern und x-Werten
    for i, (x_peak, y_peak) in enumerate(filtered_peaks):
        plt.text(x_peak, y_peak, f"Peak {i+1}", fontsize=12, fontweight='bold', ha='center', va='bottom')
        plt.text(x_peak, y_peak - 0.5, f"x={x_peak}", fontsize=10, ha='center', va='top')

    plt.legend()
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

def interplot_xy_values(title, xLabel, yLabel, x_data, y_data, filtered_peaks):
    # Create an interactive plot of the xy-data with peaks labeled inside the Webbrowser. Opens a new tab inside the browser.
    # Uses plotly as library.
    line_trace = go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Messdaten', line=dict(color='blue'))

    # Create a scatter plot for the peaks
    peaks_x, peaks_y = zip(*filtered_peaks)
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
    ) for i, (x_peak, y_peak) in enumerate(filtered_peaks)]

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
if __name__ == "__main__":
    path = r"C:\Users\Jan\Desktop\Simulation\Geometrien\fertig\2_2_2_2_4_10000-mt_volav-rfile.out"
    path = r"C:\Users\Jan\Desktop\Simulation\Geometrien\fertig\2_16_2_2_1-10000-mt_volav-rfile.out"
    experiment = OUfile_Parser()
    
    experiment.read_datafile(path)
    #OUfile_Parser.read_datafile('C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out')
    #filepath = 'C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out'
    #oufile_parser = OUfile_Parser()
    #oufile_parser.read_datafile(filepath)
    
    path2 = r"C:\Users\Jan\Desktop\Simulation\Geometrien\fertig\2_2_2_2_4_10000-vapor_volume-rfile.out"
    path2 = r"C:\Users\Jan\Desktop\Simulation\Geometrien\fertig\2_16_2_2_1-10000-vapor_volint-rfile.out"
    experiment2 = OUfile_Parser2()
    
    experiment2.read_datafile2(path2)
    
    # Extrahieren der Peaks
peaks = extract_peaks(x_data=experiment.xdata, y_data=experiment.ydata, threshold=0)

# Ausgabe der Peaks
print("Peaks:", peaks)

mean_y = calculate_mean_y(peaks)
#prominence_calc=0*mean_y
peaks = extract_peaks(x_data=experiment.xdata, y_data=experiment.ydata, threshold=0)

filtered_peaks = remove_outliers(peaks)
print("Filtered peaks:", filtered_peaks)

interplot_xy_values(title=experiment.set_filename (file_path=path),xLabel="x",yLabel="y",x_data=experiment.xdata,y_data=experiment.ydata,filtered_peaks=filtered_peaks)

print("Mittelwert der y-Werte:", mean_y)

vapor_volume = find_corresponding_mtvolav(filtered_peaks, x_data2=experiment2.xdata2, y_data2=experiment2.ydata2)

print("Vapor Volume:", vapor_volume)