import os

class Wertepaar:
  """
  Eine Klasse, die eine Person darstellt.

  Attributes:
    value: Der value der Person.
    time: Das Alter der Person.
  """

  def __init__(self, filename=None, type_of_file=None, timestep=None, value=None, time=None):
    self.timestep = timestep
    self.value = value
    self.time = time
    self.filename = filename
    self.type_of_file = type_of_file

  #def __repr__(self):
  #  return f"Person(Filename={self.filename}, Type_of_file={self.type_of_file}, timestep={self.timestep}, value={self.value}, time={self.time})"

  #def __str__(self):
  #  return f"Filename={self.filename}, Type_of_file={self.type_of_file}, Timestep: {self.timestep}, value: {self.value}, Zeit: {self.time}"


def read_file_to_persons(file_value):
  """
  Liest den Inhalt einer Textdatei ein und erstellt eine Liste von Personen.

  Args:
    file_value: Der value der Textdatei.

  Returns:
    Eine Liste von Personen.
  """
  wertepaare = []
  filename='test'
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
        timestep, value, time = line.split()
        wertepaare.append(Wertepaar(filename, type_of_file, timestep, value, time))
      #if line_number in range(3,10):
        #timestep, value, time = line.split()
        #wertepaare.append(Wertepaar(timestep, value, time))
      line_number += 1
    return wertepaare
  
def extract_peaks(x_data, y_data, threshold=0):
    # Finden der Peaks mithilfe von scipy.signal.find_peaks
    peaks, _ = find_peaks(y_data, height=threshold)

    # Extrahieren der x- und y-Werte der Peakmaxima als Liste von Tupeln
    peak_coordinates = [(x_data[peaks[i]], y_data[peaks[i]]) for i in range(len(peaks))]

    return peak_coordinates




if __name__ == "__main__":
  wertepaare = read_file_to_persons('C:/Users/Jan/Desktop/Simulation/Geometrien/fertig/2_2_2_2_1_10000-mt_volav-rfile.out')
  print('One')
  for wertepaar in wertepaare:
    print(Wertepaar.__dict__)
