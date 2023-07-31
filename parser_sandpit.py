

line = ("Time Step" "mt_volav" "flow-time")

# for lines in file - Schleife hier setzen!
if line_number == int(1):
  file_name = file_name[1:-1]
elif line_number == int(3):
  values = re.findall(r'"(.*?)"', line)


line = "1 0.2509840045191862 2e-06
xyzdata = line.split()
self.xdata = xdata.append(float(xyzdata[0]))
self.ydata = ydata.append(float(xyzdata[1]))
self.zdata = zdata.append(float(xyzdata[2]))
