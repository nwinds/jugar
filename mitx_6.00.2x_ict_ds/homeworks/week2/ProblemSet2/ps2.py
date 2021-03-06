# -*- coding: utf-8 -*-
# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
#- may be anything, like float, which is not veery good while using!
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    #@staticmethod
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)
        
# my impl
class ConvInt(object):
    @classmethod
    def getInt(self, num):
        return int(math.floor(num))
    @classmethod
    def getIntPos(self, pos):
        tileX = ConvInt.getInt(pos.getX())
        tileY = ConvInt.getInt(pos.getY())
        return Position(tileX, tileY)
        
# === Problem 1
EPSILON = 0.001
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    # const
    CLEANED = 0
    UNCLEANED = 1# for new allocated room, marked as uncleaned
    
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        random.seed()
        if type(width) != int or type(height) != int:
            raise TypeError
        if width <= 0 or height <= 0:
            raise ValueError
        self.width = width
        self.height = height
        #room 2d list like matrix
        self.room = [[self.UNCLEANED for j in range(self.height)] \
                        for i in range(self.width)]        


    #pos.x representin the abstract width(like row in matrix) and 
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        tilePos = ConvInt.getIntPos(pos)
        self.room[tilePos.getX()][tilePos.getY()] = self.CLEANED

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.room[m][n] == self.CLEANED
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return (self.width * self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cnt = 0
        for line in self.room:
            cnt += line.count(self.CLEANED)
        return cnt

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.randint(0, self.width-1), \
                        random.randint(0, self.height-1))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        tilePos = ConvInt.getIntPos(pos)
        return (0 <= tilePos.getX() < self.width) and (0 <= tilePos.getY() < self.height)
    
    #my impl to support print
    def __str__(self):  
        return "(%d, %d)" % (self.width, self.height)



# Enter your code for Robot (from the previous problem)
#  and StandardRobot in this box
EPSILON = 0.00001
import math
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """    
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        if type(room) != RectangularRoom or (type(speed) != float and type(speed) != int):
            raise TypeError
        if speed < EPSILON:
            raise ValueError
        self.room = room
        self.speed = speed
        self.d = random.randint(0, 360)
        if self.setRobotPosition(self.room.getRandomPosition()) == False:
            raise Exception

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
        
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.d


    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        if self.room.isPositionInRoom(position):
            self.pos = position
            self.room.cleanTileAtPosition(self.pos)
            return True
        return False
        
    def setRobotUncleanedPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        tilePos = ConvInt.getIntPos(position)
        if self.room.isPositionInRoom(position) and \
                self.room.isTileCleaned(tilePos.getX(), tilePos.getY()) == False:
            self.pos = position
            self.room.cleanTileAtPosition(self.pos)
            return True
        return False
        
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.d = direction % 360

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!       
        
    #my impl to ease the updatePositionAndClean
    def pos2Mat(self, pos):
        return Position(pos.getY(), pos.getX())

    def getMode(self, pos):
        tilePos = ConvInt.getIntPos(pos)
        mode = 0x0
        if tilePos.getY() == self.room.height-1:
            mode |= 0x1            
        if tilePos.getY() == 0:
            mode |= 0x10            
        if tilePos.getX() == self.room.width-1:
            mode |= 0x100       
        if tilePos.getX() == 0:
            mode |= 0x1000
        return mode
    
    def generatChoices(self, mode):
        #edge cases
        if mode == 0x1:                       #tile(ok, height-1), delta y: cos<=0
            choices = range(180, 270+1)
        elif mode == 0x10:                    #tile(ok, 0), delta y: cos>=0
            choices = range(0, 90+1) + range(270, 360)
        elif mode == 0x100:                   #tile(width-1, ok), delta x: sin>=0
            choices = range(0, 180+1)
        elif mode == 0x1000:                  #tile(0, ok), delta x: sin<=0
            choices = [0] + range(180, 360)
        #corner cases
        elif mode == 0x110:                   #tile(width-1, 0)
            choices = [0] + range(270, 360)   #decrease x(with sin!!!) and increase y(with cos)
        elif mode == 0x101:                   #tile(width-1, height-1), delta(x,y): sin<=0, cos<=0
            choices = range(180, 270+1)
        elif mode == 0x1001:                  #tile(0, height-1), delta(x,y): sin>=0, cos<=0
            choices = range(90, 180+1)
        elif mode == 0x1010:                  #tile(0, 0) 
            choices = range(0, 90+1)
        else:                                 #nomal cases
            choices = range(360)   
        return choices     

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """ 
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if self.room.getNumCleanedTiles() >= self.room.getNumTiles():
            return
        mode = self.getMode(self.pos)
        choices = self.generatChoices(mode)
        try:
            if self.d not in choices: # if original direction cannot go further
                angle = choices.pop(random.randrange(len(choices)))  
            else:
                angle = self.d
            while self.setRobotPosition(self.pos.getNewPosition(angle, self.speed)) == False:   
                angle = choices.pop(random.randrange(len(choices)))  
            if self.d != angle:
                self.setRobotDirection(angle) #tilt to another direction
        except IndexError:
            return

# Uncomment this line to see your implementation of StandardRobot in action!
testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    timesteps = []
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robots = [robot_type(room, speed) for i in range(num_robots)]
        steps = 0
        #move the robots
        while float(room.getNumCleanedTiles())/float(room.getNumTiles()) < min_coverage:
            for r in robots:
                r.updatePositionAndClean()
            steps += 1
        timesteps.append(steps)
    return float(sum(timesteps))/len(timesteps) if len(timesteps) > 0 else float('NaN')


# Uncomment this line to see how much your simulation takes on average
#print  runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if self.room.getNumCleanedTiles() >= self.room.getNumTiles():
            return
        mode = self.getMode(self.pos)
        choices = self.generatChoices(mode)
        if self.d in choices:
            choices.remove(self.d)
        try:
            angle = choices.pop(random.randrange(len(choices)))            
            while self.setRobotPosition(self.pos.getNewPosition(angle, self.speed)) == False:
                angle = choices.pop(random.randrange(len(choices)))         
            self.setRobotDirection(angle)
        except IndexError:
            return


print  runSimulation(1, 1.0, 10, 10, 0.75, 30, RandomWalkRobot)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#


""" My tests """
        
        
class TestRectangularRoom(RectangularRoom):
    def testCleanTileAtPosition(self):
        self.cleanTileAtPosition(Position(self.width/2.0, self.height/2.0))
    def testPrint(self):
        print(self)
        
class TestPosition(Position):
    def testGetNewPosition(self):
        for angle in range(0, 360, 45):
            print(self.getNewPosition(angle, 1.0))

        