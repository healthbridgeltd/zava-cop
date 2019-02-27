#!/usr/bin/env python

"""
This Python code is based on Java code by Lee Jacobson found in an article
entitled "Applying a genetic algorithm to the travelling salesman problem"
that can be found at: http://goo.gl/cJEY1
"""

import math
from math import sin, cos, sqrt, atan2, radians
import random

class City:
    def __init__(self, name, y=None, x=None):
      self.name = name
      self.x = None
      self.y = None
      if x is not None:
         self.x = x
      else:
         self.x = int(random.random() * 200)
      if y is not None:
         self.y = y
      else:
         self.y = int(random.random() * 200)
   
    def getX(self):
      return self.x
   
    def getY(self):
      return self.y

    def getName(self):
      return self.name
   
    def distanceTo(self, city):
      R = 6373.0  # Radius of the earth in km
      lat1 = radians(self.getY())
      lng1 = radians(self.getX())
      lat2 = radians(city.getY())
      lng2 = radians(city.getX())
      dlng = lng2 - lng1
      dlat = lat2 - lat1

      # Trigonometric functions to calculate distance
      a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlng / 2)**2
      c = 2 * atan2(sqrt(a), sqrt(1 - a))

      return R * c

    def __repr__(self):
      return self.getName()


class TourManager:
   destinationCities = []
   
   def addCity(self, city):
      self.destinationCities.append(city)
   
   def getCity(self, index):
      return self.destinationCities[index]
   
   def numberOfCities(self):
      return len(self.destinationCities)


class Tour:
   def __init__(self, tourmanager, tour=None):
      self.tourmanager = tourmanager
      self.tour = []
      self.fitness = 0.0
      self.distance = 0
      if tour is not None:
         self.tour = tour
      else:
         for i in range(0, self.tourmanager.numberOfCities()):
            self.tour.append(None)
   
   def __len__(self):
      return len(self.tour)
   
   def __getitem__(self, index):
      return self.tour[index]
   
   def __setitem__(self, key, value):
      self.tour[key] = value
   
   def __repr__(self):
      geneString = "|"
      for i in range(0, self.tourSize()):
         geneString += str(self.getCity(i)) + "|"
      return geneString + str(self.getDistance())
   
   def generateIndividual(self):
      for cityIndex in range(0, self.tourmanager.numberOfCities()):
         self.setCity(cityIndex, self.tourmanager.getCity(cityIndex))
      random.shuffle(self.tour)
   
   def getCity(self, tourPosition):
      return self.tour[tourPosition]
   
   def setCity(self, tourPosition, city):
      self.tour[tourPosition] = city
      self.fitness = 0.0
      self.distance = 0
   
   def getFitness(self):
      if self.fitness == 0:
         self.fitness = 1/float(self.getDistance())
      return self.fitness
   
   def getDistance(self):
      if self.distance == 0:
         tourDistance = 0
         for cityIndex in range(0, self.tourSize()):
            fromCity = self.getCity(cityIndex)
            destinationCity = None
            if cityIndex+1 < self.tourSize():
               destinationCity = self.getCity(cityIndex+1)
            else:
               destinationCity = self.getCity(0)
            tourDistance += fromCity.distanceTo(destinationCity)
         self.distance = tourDistance
      return self.distance
   
   def tourSize(self):
      return len(self.tour)
   
   def containsCity(self, city):
      return city in self.tour


class Population:
  def __init__(self, tourmanager, populationSize, initialise):
    self.tours = []
    for i in range(0, populationSize):
        self.tours.append(None)
    
    if initialise:
        for i in range(0, populationSize):
          newTour = Tour(tourmanager)
          newTour.generateIndividual()
          self.saveTour(i, newTour)
    
  def __setitem__(self, key, value):
    self.tours[key] = value
  
  def __getitem__(self, index):
    return self.tours[index]
  
  def saveTour(self, index, tour):
    self.tours[index] = tour
  
  def getTour(self, index):
    return self.tours[index]
  
  def getFittest(self):
    fittest = self.tours[0]
    for i in range(0, self.populationSize()):
      if fittest.getFitness() <= self.getTour(i).getFitness():
        fittest = self.getTour(i)
    return fittest
   
  def populationSize(self):
    return len(self.tours)

  def __repr__(self):
    geneString = "|"
    for i in range(0, self.populationSize()):
      geneString += str(self.getTour(i)) + "\n"
    return geneString

class GA:
  def __init__(self, tourmanager):
    self.tourmanager = tourmanager
    self.mutationRate = 0.015
    self.tournamentSize = 5
    self.elitism = True
   
  def evolvePopulation(self, pop):
    newPopulation = Population(self.tourmanager, pop.populationSize(), False)
    elitismOffset = 0
    if self.elitism:
        newPopulation.saveTour(0, pop.getFittest())
        elitismOffset = 1
    
    for i in range(elitismOffset, newPopulation.populationSize()):
        parent1 = self.tournamentSelection(pop)
        parent2 = self.tournamentSelection(pop)
        child = self.crossover(parent1, parent2)
        newPopulation.saveTour(i, child)
    
    for i in range(elitismOffset, newPopulation.populationSize()):
        self.mutate(newPopulation.getTour(i))
    
    return newPopulation
   
  def crossover(self, parent1, parent2):
    child = Tour(self.tourmanager)
    
    startPos = int(random.random() * parent1.tourSize())
    endPos = int(random.random() * parent1.tourSize())
    
    for i in range(0, child.tourSize()):
      if startPos < endPos and i > startPos and i < endPos:
        child.setCity(i, parent1.getCity(i))
      elif startPos > endPos:
        if not (i < startPos and i > endPos):
          child.setCity(i, parent1.getCity(i))
  
    for i in range(0, parent2.tourSize()):
      if not child.containsCity(parent2.getCity(i)):
        for ii in range(0, child.tourSize()):
          if child.getCity(ii) == None:
            child.setCity(ii, parent2.getCity(i))
            break
    
    return child
   
  def mutate(self, tour):
    for tourPos1 in range(0, tour.tourSize()):
      if random.random() < self.mutationRate:
        tourPos2 = int(tour.tourSize() * random.random())
        
        city1 = tour.getCity(tourPos1)
        city2 = tour.getCity(tourPos2)
        
        tour.setCity(tourPos2, city1)
        tour.setCity(tourPos1, city2)
  
  def tournamentSelection(self, pop):
    tournament = Population(self.tourmanager, self.tournamentSize, False)
    for i in range(0, self.tournamentSize):
      randomId = int(random.random() * pop.populationSize())
      tournament.saveTour(i, pop.getTour(randomId))
    fittest = tournament.getFittest()
    return fittest

if __name__ == '__main__':
  
  tourmanager = TourManager()
  
  # Create and add our cities
  city = City("London", 51.51, -0.12)
  tourmanager.addCity(city)
  city2 = City("Manchester", 53.48, -2.25)
  tourmanager.addCity(city2)
  city3 = City("Birmingham", 52.41, -1.78)
  tourmanager.addCity(city3)
  city4 = City("Dublin", 53.35, -6.25)
  tourmanager.addCity(city4)
  city5 = City("Liverpool", 53.41, -2.98)
  tourmanager.addCity(city5)
  city6 = City("Cardiff", 51.48, -3.18)
  tourmanager.addCity(city6)
  city7 = City("Bristol", 51.45, -2.59)
  tourmanager.addCity(city7)
  city8 = City("Newcastle", 54.98, -1.61)
  tourmanager.addCity(city8)
  city9 = City("Glasgow", 55.86, -4.24)
  tourmanager.addCity(city9)
  city10 = City("Aberdeen", 57.15, -2.10)
  tourmanager.addCity(city10)
  city11 = City("Edinburgh", 55.95, -3.20)
  tourmanager.addCity(city11)
  city12 = City("Southampton", 50.90, -1.40)
  tourmanager.addCity(city12)
  city13 = City("Norwich", 52.62, 1.29)
  tourmanager.addCity(city13)
  city14 = City("Penzance", 50.12, -5.54)
  tourmanager.addCity(city14)
  city15 = City("Belfast", 54.60, -5.93)
  tourmanager.addCity(city15)

  # Initialize population
  pop = Population(tourmanager, 100, True)
  print("Initial distance: " + str(pop.getFittest().getDistance()) + " km")
  print("Journey:")
  print(pop.getFittest())

  # Run 10 generations at a time up to a maximum of 200.
  for i in range(0, 500):

    # Pause for input
    input("Press Enter to start...")

    # Evolve population for 10 generations
    ga = GA(tourmanager)
    pop = ga.evolvePopulation(pop)

    print("Population after evolution:")
    print(pop)
    print("")
    print("Distance after " + str(i) + " generation(s): " + str(pop.getFittest().getDistance()) + " km")
    print("")
    print("Solution:")
    print(pop.getFittest())
