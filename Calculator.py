#Importing everything math related and physics
import math #For math stuff 
import numpy as np # More math
import matplotlib.pyplot as plt # Sketching out diagrams and models for kinematics
import pysketcher as ps # Drawing out Physics diagrams and FBD



# Setting up values and variables for energy, weight, and mass
gravity = float
kinetic_energy = float(5)
velocity = float
height = float
planet_name = str


# Calculation Set Up for energy and mass
Mass_Calc = float(input("Mass: "))

print(str(Mass_Calc) +"kg")

height = float(input("What height do you want to set your mass at in Meters? "))

Planet_Choice = int(input("Choose a planet: 1. Mercury, 2. Venus, 3. Earth, 4. Mars, 5. Jupiter, 6. Saturn, 7. Uranus, 8. Neptune "))


# Calculations for planets and energy
if(Planet_Choice == 1):
    gravity = 3.59
    weight_force = Mass_Calc * gravity
    print(str(weight_force) + "N is the weight of the mass on Mercury")
    planet_name = "Mercury"
    
if(Planet_Choice == 2):
    gravity = 8.87
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Venus")
    planet_name = "Venus"
    
    
if(Planet_Choice == 3):
    gravity = 9.81
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Earth")
    planet_name = "Earth"
    
if(Planet_Choice == 4):
    gravity = 3.77
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Mars")
    planet_name = "Mars"
    
    
if(Planet_Choice == 5):
    gravity = 25.95
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Jupiter")
    planet_name = "Jupiter"
    
    
if(Planet_Choice == 6):
    gravity = 11.08
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Saturn")
    planet_name = "Saturn"
    
    
if(Planet_Choice == 7):
    gravity = 10.67
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Uranus")
    planet_name = "Uranus"
    
    
if(Planet_Choice == 8):
    gravity = 14.07
    weight_force = Mass_Calc * gravity
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Neptune")
    planet_name = "Neptune"
    
if(Planet_Choice < 1 or Planet_Choice > 8):
    print("This planet does not exist")


def potenergyCalc(Mass_Calc, gravity, height):
    global potential_energy
    potential_energy = Mass_Calc * gravity * height
    print(str(potential_energy) + " Joules is the potential-energy of the mass-gravitational height system")

potenergyCalc(Mass_Calc, gravity, height)




# Energy graphing simulator [KE , Velocity conversion graph] 
fig = plt.figure(figsize = (12, 7))
xpoints =  np.linspace(0, potential_energy, 100)
ypoints = (2* xpoints / Mass_Calc)**0.5

plt.plot(xpoints, ypoints, alpha = 0.4, label ='V = $\sqrt{PE/m}$',
         color ='red', linestyle ='dashed',
         linewidth = 2)

plt.title("Potential Energy to Velocity conversion rate of " + planet_name)
plt.xlabel("Potential Energy")
plt.ylabel("Velocity")

plt.grid(alpha =.6, linestyle ='--')
fig.text(0.7, 0.15, 'Glaiven_Dev',
         fontsize = 12, color ='blue',
         ha ='left', va ='bottom',
         alpha = 0.5)
 
plt.legend()
 
plt.show()


