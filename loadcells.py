from neuron import h, gui
import neuron
import os
import sys

def loadCell(cellName, cellTemplateName):
    origDir = os.getcwd()
    os.chdir(cellName)
    h.load_file('import3d.hoc')
    h.load_file('template.hoc')
    cell = getattr(h, cellTemplateName)(0)
    os.chdir(origDir)
    return cell

cell1 = loadCell('L1_DAC_bNAC219_1', 'bNAC219_L1_DAC_ec2fc5f0de')
cell2 = loadCell('L1_DAC_bNAC219_2', 'bNAC219_L1_DAC_0d58fdf14a')
