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
        # if type(maxBirthProb) != float or type(clearProb) != float:
        #    raise TypeError
        # if  0.0 <= maxBirthProb <= 1.0 and 0.0 <= clearProb <= 1.0:
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        # else:
        #    raise ValueError

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
        # if type(viruses) != SimpleVirus or\
        #  (type(maxPop) != int and type(maxPop) != float):
        #    raise TypeError
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
        # if len(duplicates) != 0:
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

# Enter your definition for simulationWithDrug in this box

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
    def getAvg(lst, numTrials):
        if len(lst) == 0:
            return 0
        for ele in lst:
            ele = float(ele)/float(numTrials)

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
    getAvg(virusPop, numTrials)
    getAvg(resistantVirusPop, numTrials)
    drawPlot(virusPop, resistantVirusPop)

#test run online
#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)

def drawPlot(lst1, lst2):
    pylab.plot(lst1, 'b', label = 'total pop')
    pylab.plot(lst2, 'r', label = 'guttagonol-resistant pop')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.legend(['Total', 'ResistantVirus'])
    pylab.show()

drawPlot([10, 17, 27, 36, 44, 49, 50, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51], [2.0, 3.4, 5.4, 7.2, 8.8, 9.8, 10.0, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2, 10.2])
drawPlot([9, 16, 27, 48, 71, 95, 99, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103, 103],[1.8, 3.2, 5.4, 9.6, 14.2, 19.0, 19.8, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6, 20.6])
drawPlot([93, 99, 92, 94, 90, 91, 91, 101, 97, 98, 101, 101, 96, 96, 98, 101, 96, 95, 97, 98, 98, 96, 95, 97, 91, 95, 98, 97, 99, 96, 97, 95, 95, 91, 86, 86, 87, 95, 97, 92, 96, 90, 98, 97, 96, 95, 91, 94, 100, 98, 98, 95, 94, 91, 100, 101, 98, 99, 97, 96, 101, 99, 92, 94, 95, 93, 91, 96, 97, 96, 101, 96, 97, 95, 94, 95, 95, 97, 95, 91, 90, 92, 92, 92, 98, 95, 97, 94, 95, 100, 97, 95, 96, 97, 93, 92, 101, 99, 91, 92, 99, 93, 89, 91, 94, 95, 98, 97, 96, 95, 87, 90, 90, 96, 92, 96, 95, 91, 93, 100, 91, 90, 93, 94, 99, 100, 97, 103, 100, 94, 94, 97, 100, 96, 98, 99, 89, 93, 92, 93, 97, 101, 95, 91, 93, 92, 94, 92, 91, 91, 83, 82, 81, 80, 70, 73, 78, 79, 74, 78, 72, 76, 75, 73, 71, 72, 71, 63, 57, 57, 50, 50, 51, 53, 50, 50, 49, 47, 52, 49, 49, 45, 46, 44, 42, 41, 44, 42, 39, 38, 40, 34, 33, 32, 33, 33, 30, 29, 27, 27, 30, 32, 33, 32, 34, 38, 39, 34, 36, 37, 38, 40, 42, 45, 46, 45, 43, 44, 42, 41, 45, 49, 50, 52, 59, 61, 56, 57, 55, 49, 47, 44, 43, 43, 42, 38, 37, 36, 32, 31, 25, 26, 26, 24, 24, 24, 24, 22, 20, 22, 22, 24, 22, 22, 22, 18, 18, 18, 18, 18, 17, 18, 20, 19, 21, 21, 22, 21, 18, 17, 16, 15, 15, 15, 13, 14, 13, 13, 13, 12, 12, 10, 9, 9, 7, 6, 6, 5, 4, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1], [93.0, 99.0, 92.0, 94.0, 90.0, 91.0, 91.0, 101.0, 97.0, 98.0, 101.0, 101.0, 96.0, 96.0, 98.0, 101.0, 96.0, 95.0, 97.0, 98.0, 98.0, 96.0, 95.0, 97.0, 91.0, 95.0, 98.0, 97.0, 99.0, 96.0, 97.0, 95.0, 95.0, 91.0, 86.0, 86.0, 87.0, 95.0, 97.0, 92.0, 96.0, 90.0, 98.0, 97.0, 96.0, 95.0, 91.0, 94.0, 100.0, 98.0, 98.0, 95.0, 94.0, 91.0, 100.0, 101.0, 98.0, 99.0, 97.0, 96.0, 101.0, 99.0, 92.0, 94.0, 95.0, 93.0, 91.0, 96.0, 97.0, 96.0, 101.0, 96.0, 97.0, 95.0, 94.0, 95.0, 95.0, 97.0, 95.0, 91.0, 90.0, 92.0, 92.0, 92.0, 98.0, 95.0, 97.0, 94.0, 95.0, 100.0, 97.0, 95.0, 96.0, 97.0, 93.0, 92.0, 101.0, 99.0, 91.0, 92.0, 99.0, 93.0, 89.0, 91.0, 94.0, 95.0, 98.0, 97.0, 96.0, 95.0, 87.0, 90.0, 90.0, 96.0, 92.0, 96.0, 95.0, 91.0, 93.0, 100.0, 91.0, 90.0, 93.0, 94.0, 99.0, 100.0, 97.0, 103.0, 100.0, 94.0, 94.0, 97.0, 100.0, 96.0, 98.0, 99.0, 89.0, 93.0, 92.0, 93.0, 97.0, 101.0, 95.0, 91.0, 93.0, 92.0, 94.0, 92.0, 91.0, 91.0, 83.0, 82.0, 81.0, 80.0, 70.0, 73.0, 78.0, 79.0, 74.0, 78.0, 72.0, 76.0, 75.0, 73.0, 71.0, 72.0, 71.0, 63.0, 57.0, 57.0, 50.0, 50.0, 51.0, 53.0, 50.0, 50.0, 49.0, 47.0, 52.0, 49.0, 49.0, 45.0, 46.0, 44.0, 42.0, 41.0, 44.0, 42.0, 39.0, 38.0, 40.0, 34.0, 33.0, 32.0, 33.0, 33.0, 30.0, 29.0, 27.0, 27.0, 30.0, 32.0, 33.0, 32.0, 34.0, 38.0, 39.0, 34.0, 36.0, 37.0, 38.0, 40.0, 42.0, 45.0, 46.0, 45.0, 43.0, 44.0, 42.0, 41.0, 45.0, 49.0, 50.0, 52.0, 59.0, 61.0, 56.0, 57.0, 55.0, 49.0, 47.0, 44.0, 43.0, 43.0, 42.0, 38.0, 37.0, 36.0, 32.0, 31.0, 25.0, 26.0, 26.0, 24.0, 24.0, 24.0, 24.0, 22.0, 20.0, 22.0, 22.0, 24.0, 22.0, 22.0, 22.0, 18.0, 18.0, 18.0, 18.0, 18.0, 17.0, 18.0, 20.0, 19.0, 21.0, 21.0, 22.0, 21.0, 18.0, 17.0, 16.0, 15.0, 15.0, 15.0, 13.0, 14.0, 13.0, 13.0, 13.0, 12.0, 12.0, 10.0, 9.0, 9.0, 7.0, 6.0, 6.0, 5.0, 4.0, 4.0, 3.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])


