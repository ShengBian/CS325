# Author: Sheng Bian, Terence Berry, Bradley Beise
# Date: June 7, 2018
# Description: This problem uses greedy algorithm and 2-opt algorithm to solve
# travelling salesman problem. In this program, it first uses the nearest
# neighbour algorithm find a viable solution for the problem. Then, it uses 2-op
# algorithm to optimize the solution.

import math
import time
import sys

# class City to represent cities salesman needs to visit
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


# This function is used to calculate distance between city1 and city2
def getDistance(city1, city2):
    distance = int(round(math.sqrt(
        pow((int(city1.x) - int(city2.x)), 2) + pow((int(city1.y) - int(city2.y)), 2))))
    return distance


# This function is used to calculate total distances from list of cities
def getTotalDistance(path):
    totalDistance = 0
    # loop through all the cities to get the distance
    for i in range(0, len(path) - 1):
        totalDistance += getDistance(path[i], path[i + 1])
    # add the distance between last city and the starting city
    totalDistance += getDistance(path[len(path) - 1], path[0])
    return totalDistance


# This function is to find a viable solution by nearest neighbour algorithm
def getPathFromNearestCity(availableCities):
    path = []
    currentCity = availableCities.pop(0)
    path.append(currentCity)
    # loop through available city list until it's empty
    while (availableCities):
        # set minDistance to infinite number
        minDistance = float("inf")
        nextCity = currentCity
        # loop through available city list to find the nearest city
        for availableCity in availableCities:
			# calculate the distance between cities
			newDistance = getDistance(currentCity, availableCity)
			if newDistance < minDistance:
				minDistance = newDistance
				nextCity = availableCity
        # after finding the nearest city, set the current city to nextCity
        currentCity = nextCity
        path.append(currentCity)
        availableCities.remove(currentCity)
    return path

	
# This function is used to reorder the path by 2-opt
def twoOptSwap(route, i, j):
    new_route = route[0:i]
    new_route.extend(reversed(route[i:j + 1]))
    new_route.extend(route[j + 1:])
    return new_route


# This function is to optimize the path by 2-opt algorithm within 3 minutes
def getPathFromTwoOpt(path, startingTime):
    endingTime = startingTime + 179
    improve = True
    while improve:
        improve = False
        minDistance = getTotalDistance(path)
        # neested loop to reorder the path by 2-opt to check if we can get smaller path
        for i in range(len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                # This if statment is quite important, it uses Fixed Radius Search to speed up 2-opt
                # reference from http://tsp-basics.blogspot.com/2017/03/2-opt-basic-with-fixed-radius-search.html
                if getDistance(path[i - 1], path[i]) + getDistance(path[j], path[j + 1]) >= getDistance(path[i], path[j + 1]) + getDistance(path[i - 1], path[j]):
                    newPath = twoOptSwap(path, i, j)
                    newDistance = getTotalDistance(newPath)
                    if newDistance < minDistance:
                        path = newPath
                        minDistance = newDistance
                        improve = True
                    if time.time() > endingTime:
                        return path
    return path


inputfilename = sys.argv[1]
startingTime = time.time()
cities = []

# This block of code is used to read cities from file and add to a list of instances of class City
with open(inputfilename, "r") as file_input:
    for line in file_input:
        # convert string to int, make processing speed much faster!
        city = line.split()
        intCity = []
        for item in city:
            intCity.append(int(item))
        cities.append(City(intCity[0], intCity[1], intCity[2]))


path = getPathFromNearestCity(cities)
path = getPathFromTwoOpt(path, startingTime)

totalDistance = getTotalDistance(path)
# This block of code is to write result to the solution file
with open(inputfilename + ".tour", "w") as file_output:
    file_output.write(str(totalDistance) + '\n')
    for city in path:
        file_output.write("%s\n" % city.id)

runningTime = time.time() - startingTime
print("The total distance is %s" % str(totalDistance))
print("The running time is %.2f seconds" % runningTime)
