# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import numpy
import random
import pylab

''' 
Begin helper code
'''


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
# Enter your definitions for the SimpleVirus and Patient classes in this box.


class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        r = random.random()
        return (r <= self.clearProb)

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        # roll a dice
        # if hits the zone(virus reproduce)
        #    return new virus
        # else
        #    nothing
        r = random.random()
        if popDensity < 1.0 and r < (self.maxBirthProb * (1 - popDensity)):
            dup = SimpleVirus(self.maxBirthProb, self.clearProb)
            return dup
        else:
            raise NoChildException

    def __str__(self):
        return '(%s, %s)' % (self.maxBirthProb, self.clearProb)

import copy


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        if maxPop < 0:
            raise ValueError
        self.viruses = viruses[:]
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)

    def getSurvivedViruses(self):
        survived = []
        for v in self.viruses:
            if v.doesClear() == False:
                survived.append(v)
        return survived

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   

        - The current population density is calculated. This population density
          value is used until the next call to update() 

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        # survive game for viruses
        # count current population
        # reproduce or not

        # pop may introduce many error, try filter(dummy block?) or create a new array to save them
        # and pop is not quite efficient

        self.viruses = self.getSurvivedViruses()
        currPopDen = float(self.getTotalPop()) / self.getMaxPop()
        duplicates = []
        for v in self.viruses:
            # current viruses number chances to dup, sim all dup in a loop but
            # the true process is happened at the same time
            try:
                newViruse = v.reproduce(currPopDen)
                duplicates.append(newViruse)
            except NoChildException:
                continue
        self.viruses += duplicates
        return self.getTotalPop()

# test problem 1
##virus = SimpleVirus(1.0, 0.0)
##patient = Patient([virus], 100)
# for i in range(100):
# patient.update()

#
# PROBLEM 3
#
#from ps3b_precompiled_27 import *


def drawPlot(lst):
    pylab.plot(lst, label='SimpleVirus simulation')
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend(['virus population'])
    pylab.show()


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    TIMESTEPS = 300
    virusPop = [0 for t in range(TIMESTEPS)]
    # get sum of virus population at each timestep
    for nt in range(numTrials):
        virus = SimpleVirus(maxBirthProb, clearProb)
        patient = Patient([virus for vnum in range(numViruses)], maxPop)
        for t in range(TIMESTEPS):
            virusPop[t] += patient.update()
    # get the avg
    for t in range(TIMESTEPS):
        virusPop[t] = float(virusPop[t]) / numTrials
    drawPlot(virusPop)


#
# PROBLEM 4
#
import copy
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = copy.deepcopy(resistances)
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances.get(drug, False)

    def inheritedResistance(self):
        """
        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        childLst: the reproduced child virus' resistance drug dict, mutable and 
        rewrite at the same place
        Return: dict of child virus's resistance
        """
        childResistances = {}
        for drug in self.resistances:
            chance = random.random()
            if self.isResistantTo(drug):
                # hits the 1-mutProb zone in [0,1]
                childResistances[drug] = chance >= self.mutProb
            else:
                childResistances[drug] = chance < self.mutProb
        return childResistances

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        The reproduced new virus inherists the resistance to drugs by calling 
        method self.inheritedResistance(my reorganized codes, seperated in 
        another method instead of this one)

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        if [self.resistances.get(drug, False) for drug in activeDrugs].count(False) > 0:  # not resistant to all drugs
            raise NoChildException
        if random.random() > self.maxBirthProb * (1 - popDensity):  # fall out of the zone of getting reproduced
            raise NoChildException
        return ResistantVirus(self.maxBirthProb, self.clearProb, self.inheritedResistance(), self.mutProb)


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.postcondition = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.postcondition:  # already prescribed, no effect
            self.postcondition.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.postcondition

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistPop = 0
        for v in self.viruses:
            resistToAll = True
            for drug in drugResist:
                if v.isResistantTo(drug) == False:  # no resistance
                    resistToAll = False
                    break  # break the 2-lv loop and check next virus
            if resistToAll:
                resistPop += 1
        return resistPop

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        self.viruses = self.getSurvivedViruses()
        currPopDen = float(self.getTotalPop()) / self.getMaxPop()
        duplicates = []
        for v in self.viruses:
            try:
                newViruse = v.reproduce(currPopDen, self.postcondition)
                duplicates.append(newViruse)
            except NoChildException:
                continue
        self.viruses += duplicates
        return self.getTotalPop()

#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    def drawPlot(lst1, lst2):
        pylab.plot(lst1, 'b', label = 'total pop')
        pylab.plot(lst2, 'r', label = 'guttagonol-resistant pop')
        pylab.title('ResistantVirus simulation')
        pylab.xlabel('time step')
        pylab.ylabel('# viruses')
        pylab.legend(['Total', 'ResistantVirus'])
        pylab.show()

    timestepsWithoutDrug = 150
    timestepsOverall = timestepsWithoutDrug + 150
    virusPop = [0 for t in range(timestepsOverall)]
    resistantVirusPop = [0 for t in range(timestepsOverall)]   
    for nt in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        patient = TreatedPatient([virus for vnum in range(numViruses)], maxPop)
        #timestepswithoutDrug times: Patient without drug 
        for t in range(timestepsWithoutDrug):
            virusPop[t] += patient.update()
            resistantVirusPop[t] += patient.getResistPop(['guttagonol'])
        #timestepsAddedDrug times: Patient treated with drug
        patient.addPrescription('guttagonol')
        for t in range(timestepsWithoutDrug, timestepsOverall):
            virusPop[t] += patient.update()
            resistantVirusPop[t] += patient.getResistPop(['guttagonol'])
    for t in range(timestepsOverall):
        virusPop[t] /= float(numTrials)
        resistantVirusPop[t] /= float(numTrials)
    drawPlot(virusPop, resistantVirusPop)

#test run online
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
