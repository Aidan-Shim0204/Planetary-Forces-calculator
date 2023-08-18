import math 
import numpy as np
import matplotlib.pyplot as plt

gravity = float
Mass_Calc = float(input("Mass: "))
print(str(Mass_Calc) +"kg")

Planet_Choice = int(input("Choose a planet: 1. Mercury, 2. Venus, 3. Earth, 4. Mars, 5. Jupiter, 6. Saturn, 7. Uranus, 8. Neptune "))

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

else:
    print("The planet choice does not exist")
