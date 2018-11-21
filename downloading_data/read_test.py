# reading test

import netCDF4 as n

read = n.Dataset("./files/temperature_Eu.nc", "r")
print(read.variables)

temp = read.variables["t2m"]
time = read.variables["time"]
lat = read.variables["latitude"]
long = read.variables["longitude"]
#print(temp.shape) (2755, 88, 180)
# (time, latitude, longitude)
#print(temp[:,1:10,0])
print(time[:])
