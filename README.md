# VaporVolumeValueFinder
V3F is a software module used for the determination of vapor volume from simulations with ANSYS Fluent during research in Advanced Oxidation Processes
Need of a mass-transfer (e.g. volume average) record file with peaks and a vapor-volume record file from report definitions in ANSYS FLuent
General file-style:
- .txt-alike, three rows of text then 1st coloumn for number of time step and 2nd coloumn corresponding value (volume average mass transfer rate or vapor volume)

Workflow:
- Extraction of relevant mass-transfer peaks from .ou-files (from report definitions file of ANSYS FLuent)
- Plotting of mass-transfer curve with relevant peaks
- Finding corresponding vapor-volume-rfile
- Using time-step-value of mass-transfer-file to find corresponding value in vapor-volume-file
- Plotting vapor-volume curve with marked values
- Giving values of vapor volume for further usage
