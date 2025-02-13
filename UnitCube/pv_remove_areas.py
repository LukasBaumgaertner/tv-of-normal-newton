import os
import paraview.simple as pv

#reader = pv.PVDReader(FileName="sub_domain_triangles.pvd")
reader = pv.OpenDataFile("sub_domain_triangles.pvd")

dataInfo = reader.GetDataInformation()
#print(dataInfo.GetNumberOfCells())
#print(reader.CellData[:])
reader.CellData[:]


threshold = pv.Threshold(reader)
threshold.Scalars = "f"
threshold.ThresholdMethod = "Between"
threshold.LowerThreshold = -0.5
threshold.UpperThreshold = 0.5

surface = pv.ExtractSurface(threshold)
pv.SaveData("cube_deleted.stl", surface)
#pv.SaveData("cube_deleted.pvd", surface)

threshold2 = pv.Threshold(reader)
threshold2.Scalars = "f"
threshold2.ThresholdMethod = "Between"
threshold2.LowerThreshold = 0.5
threshold2.UpperThreshold = 1.5

surface2 = pv.ExtractSurface(threshold2)
pv.SaveData("cube_fill_areas.stl", surface2)
