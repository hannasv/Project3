#!/usr/bin/env python

# Surface temp 167.128
# Pressure 54.128 levtype =
# Relative humidity 157.128
# specific humidity .128
# total cloud cover .128
from ecmwfapi import ECMWFDataServer



periode = "1979-01-01/to/2018-07-31"
periode = "1990-12-01/to/1990-12-08"

server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "expver": "1",
    "stream": "oper",
    "type": "an", # use fc for forcast data
    "levtype": "pl", # pressure level
    "param": "157.128",
    "date": periode,
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    #"step": "0", # timestep is 3 hours
    "grid": "0.75/0.75", # 0.75, 0.75 is recomended resolution for grib, 1.0/1.0 is recomended for when you dont do global.
    "area":"75/-15/30/42", #Europa --> N/W/S/E lat long degrees
    "format":"netcdf",
    "target": "./filesML/relative_humidity_Europa_sp.nc"
    #"resol":"av"
})
