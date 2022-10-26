# Author : Manohar Akula
# Date: 10/25/22
# Project - Data Munging and Visualisation Assignment




from wf_dataprocessing import pre_process

from wf_datavisualization import visual

lut={}
lut["Dirt"] = 0
lut["Water"] = 1


pre_process(lut)
visual(lut)
