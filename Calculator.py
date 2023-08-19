#Importing everything math related and physics
import math #For math stuff 
import numpy as np # More math
import matplotlib.pyplot as plt # Sketching out diagrams and models for kinematics
import pysketcher as ps # Drawing out Physics diagrams and FBD

# Setting up values and variables for energy, weight, and mass
gravity = float
Mass_Calc = float(input("Mass: "))
energy = float
height = float
print(str(Mass_Calc) +"kg")


Planet_Choice = int(input("Choose a planet: 1. Mercury, 2. Venus, 3. Earth, 4. Mars, 5. Jupiter, 6. Saturn, 7. Uranus, 8. Neptune "))


# Unfortunately have to brute force these calcs
if(Planet_Choice == 1):
    gravity = 3.59
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Mercury")
    
if(Planet_Choice == 2):
    gravity = 8.87
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Venus")
    
    
if(Planet_Choice == 3):
    gravity = 9.81
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Earth")
    
if(Planet_Choice == 4):
    gravity = 3.77
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Mars")
    
if(Planet_Choice == 5):
    gravity = 25.95
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Jupiter")
    
if(Planet_Choice == 6):
    gravity = 11.08
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Saturn")
    
if(Planet_Choice == 7):
    gravity = 10.67
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Uranus")
    
if(Planet_Choice == 8):
    gravity = 14.07
    print(str(Mass_Calc * gravity) + "N is the weight of the mass on Neptune")
    
if(Planet_Choice < 1 or Planet_Choice > 8):
    print("This planet does not exist")
    







plt.title("Increasing Velocity on Planet")
plt.xlabel("Time")
plt.ylabel("Velocity")

plt.plot(x, y)

plt.grid()

plt.show()