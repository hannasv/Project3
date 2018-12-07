#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

periode = "1990-12-01/to/1990-12-08"

server = ECMWFDataServer()
server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "expver": "1",
    "stream": "oper",
    "type": "an", # use fc for forcast data
    "levtype": "sfc", #surface variable
    "param": "167.128", #temperature
    "date": periode,
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    #"step": "0", # Steps to use when downloading a forcast. 
    "grid": "0.75/0.75", # 0.75, 0.75 is recomended resolution for grib, 1.0/1.0 is recomended for when you dont do global.
    "area":"75/-15/30/42", #Europa --> N/W/S/E lat long degrees
    "format":"netcdf",
    "target": "./filesML/temperature_Europa_sp.nc"
    #"resol":"av"
})
