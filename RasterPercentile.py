from comodel import *

url = 'H:\\Python\\Projects\\BasicExercises\\Data\\RS\\'
filenames = ['FVC20030.tif']
ras = arcpy.Raster(url+filenames[0])
print(ras.mean)


