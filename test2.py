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
      if line_number == 1:
        pass
      if line_number == 2:
        pass
      else:
        x_data, y_data, z_data = line.split()
        wertepaare.append(Wertepaar(filename, type_of_file, x_data, y_data, z_data))
      #if line_number in range(3,10):
        #x_data, value, time = line.split()
        #wertepaare.append(Wertepaar(x_data, value, time))
      line_number += 1
    return wertepaare
if __name__ == "__main__":
  #file_value = r"C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out"
  #wertepaare = read_file_to_persons(file_value)
  wertepaare = read_file_to_persons('C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out')
  print('One')
  for wertepaar in wertepaare:
    print(Wertepaar.__dict__)
  print('Two')