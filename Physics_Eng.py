#Importing everything math related and physics and for data
import math #For math stuff 
import numpy as np # More math
import matplotlib.pyplot as plt # Sketching out diagrams and models for kinematics
from pysketcher import *
import pandas as pd
import openpyxl

def main(): 
	while True: 
		planet_physics_functions() 
    
# Physics Option for Calculating Energy, Force, etc.
def planet_physics_functions():
    # Setting up values and variables for energy, weight, and mass
    gravity = [3.59, 8.87, 9.81, 3.77, 25.95, 11.08, 10.67, 14.07]
    
    planet_mass = []
    planet_radius =[]
    G_const = 6.6743E-11
    
    
    
    
    height = float
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    # Calculation Set Up for energy and mass
    Mass_Calc = float(input("What Mass do you want to use in kg? : "))

    height = float(input("What height do you want to set your mass at in Meters? "))

    Planet_Choice = int(input("Choose a planet: 1. Mercury, 2. Venus, 3. Earth, 4. Mars, 5. Jupiter, 6. Saturn, 7. Uranus, 8. Neptune "))
    # Calculations for planets and energy
        
    if(Planet_Choice >= 1 and Planet_Choice < 9):
        global gravity_value 
        global planet_name
        
        planet_name = planets[Planet_Choice - 1]
        gravity_value = gravity[Planet_Choice - 1]
        weight_force = float(Mass_Calc * gravity_value)
        print(str(weight_force) + "N is the weight of the mass on the planet " + planet_name)
        
    else:
        print("This planet choice does not exist, try again")
        main()

    # Setting up functions [For calculations]
    
    #Potential Energy Value Set Up
    def potenergyCalc(Mass_Calc, gravity_value, height):
        global potential_energy
        potential_energy = Mass_Calc * gravity_value * height
        print(str(potential_energy) + " Joules is the potential-energy of the mass-gravitational height system")
    
    # Solving Kinematic Equations
    def kinematicCalc(gravity_value, height):
        global time
        time = float(math.sqrt(2 * height / gravity_value))
        return time 

    
    potenergyCalc(Mass_Calc, gravity_value, height)
    
    # Energy graphing simulator [KE , Velocity conversion graph]
    def energyGraph():     
        fig = plt.figure(figsize = (12, 7))
        xpoints =  np.linspace(0, potential_energy, 10)
        ypoints = (2 * xpoints / Mass_Calc)**0.5
        plt.plot(xpoints, ypoints, alpha = 0.4, label ='V = $\sqrt{2PE/m}$', 
            color ='red', linestyle ='dashed',
            linewidth = 2)
 
        
        plt.title("Potential Energy to Velocity conversion rate on " + planet_name)
        plt.xlabel("Potential Energy")
        plt.ylabel("Velocity")

        plt.grid(alpha =.6, linestyle ='--')
        fig.text(0.70, 0.15, 'Glaiven_Dev',
            fontsize = 12, color ='blue',
            ha ='left', va ='bottom',
            alpha = 0.5)
 
        plt.legend()
        plt.show()
    
    # Momentum graphing simulator [Time to Momentum change for a planet - AKA Force - Also include Riemann Sums]    
    def momentumGraph():
        fig = plt.figure(figsize = (12, 7))
        xpoints =  np.linspace(0, kinematicCalc(gravity_value, height), 10)
        ypoints = Mass_Calc * gravity_value * xpoints
        
        plt.plot(xpoints, ypoints, alpha = 0.4, label ='P = mv/t', 
            color ='green', linestyle ='dashed',
            linewidth = 2)
        
        plt.title("Change in Momentum over Time on Planet " + planet_name)
        plt.xlabel("Time (Seconds)")
        plt.ylabel("Momentum")
        
        
        plt.grid(alpha =.6, linestyle ='--')
        fig.text(0.8, 0.05, 'Glaiven_Dev',
            fontsize = 12, color ='blue',
            ha ='left', va ='bottom',
            alpha = 0.5)
 
        plt.legend()
        plt.show()      
        
    momentumGraph()
    energyGraph()
    
# Mapping data on an excel sheet -> Later
def data_store():
    Inst_PE = int
    
# Iterates over the whole function
if __name__ == '__main__': main() 


