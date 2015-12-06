# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

"""
ps4 requirements
In Problem 5 of the last problem set you ran a simulation that consists of 150 
time steps, followed by the addition of the drug, guttagonol, followed by 
another 150 time steps. 

Run the same simulation as in Problem 5 in Problem Set 3 but this time for 300, 
150, 75, and 0 time steps before administering guttagonol to the patient. Then, 
run the simulation for an additional 150 time steps. Use the same 
initialization parameters for ResistantVirus and TreatedPatient as you did for
Problem 5 of Problem Set 3.


Use the following parameters to initialize a TreatedPatient:
viruses: a list of 100 ResistantVirus instances
maxPop: maximum sustainable virus population = 1000

Each ResistantVirus instance in the viruses list should be initialized with the
following parameters:
maxBirthProb: maximum reproduction probability for a virus particle = 0.1
clearProb: maximum clearance probability for a virus particle = 0.05
resistances: The virus's genetic resistance to drugs in the 
experiment = {'guttagonol': False}
mutProb: probability of a mutation in a virus particle's offspring = 0.005


"""

def drawHist(lst, labelStr, legend, title='', xLabel='time step', yLabel='virus'):
    pylab.hist(lst, bins=50, label=labelStr)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.legend(legend)
    pylab.show()
    


def genDelayedTreatmentPlot(tsDelayed, tsTreated, viruses, maxPop, drugs, numTrials):
    """
    tsDelayed: timesteps before patient treated with drug
    tsTreated: timesteps simulated after patient treated with drug
    viruses: list of viruses to initilize the simulated patient
    drugs: list of drug used to treat the patient
    numTrials: number of simulation runs to execute (an integer)
    """
    tsOverall = tsDelayed + tsTreated #timesteps of whole simulation
    totalVirusPop = [] 
    for nt in range(numTrials):
        patient = TreatedPatient(viruses, maxPop)
        for t in range(tsDelayed):
            patient.update()
        patient.addPrescription(drugs[0]) #hard coded of first drug, default is guttagonol
        for t in range(tsDelayed, tsOverall):
            patient.update()
        totalVirusPop.append(patient.getTotalPop())
    drawHist([totalVirusPop], 'total', ['total'], 'delaying treatment simulation', \
    'final total virus population', 'number of trials')
#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    delays = [300, 150, 75, 0]
    #delays = [150]
    tsTreated = 150
    virus = ResistantVirus(maxBirthProb=0.1, clearProb=0.05, resistances={'guttagonol': False}, mutProb=0.005)
    numViruses = 100
    viruses = [virus for vnum in range(numViruses)]
    maxPop = 1000
    for d in delays:
        #for i in range(4):
        genDelayedTreatmentPlot(d, tsTreated, viruses, maxPop, ['guttagonol'], numTrials)

#simulationDelayedTreatment(200)
#for i in range(4):
    #simulationDelayedTreatment(50*(i+1))
simulationDelayedTreatment(100)
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO