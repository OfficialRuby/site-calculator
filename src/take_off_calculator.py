#!/usr/bin/python3
import sys
from modules.softstructure import Soft
from modules.superstructure import *

Soft.getInit()
Soft.getRecessValue()


# Global initializations
# wtIF = float(input("Enter the wall thickness in foundation (in meter): "))
# wtAF = float(input("Enter the wall thickness above foundation (in meter): "))
# blockThickness = float(input("Enter the thickness for block: "))
# girthBIF = int(input('Enter the girth of blockwork in foundation: '))
# girthBAF = int(input("Enter girth for blockwork above foundation: "))


print('''
1.  Site Clearance
2.  Top Soil Excavation
3.  Removal of Top Soil Excavation
4.  Trench Excavation
5.  Leveling and Compaction on Trench
6.  Concreate Footing
7.  Blockwork in Foundation
8.  Backfilling 
9.  Removal of Surplus Offsite 
10. Laterite Earth Filling 
11. Hardcore Filling
12. Floor Reinforcement
13. Damp Proof Course
14. Damp Proof Membrane
15. Leveling and Compacting on Surface of Filling
16. Oversite Concrete
17. Formwork for Oversite Concrete
''')

status = True
while status:
    userChoice = input("Please enter the value that corresponds with what you want to calculate: ")
    userChoice = str(userChoice)
    if userChoice == "Q":

        print("Stopping program")
        print(userChoice)
        status = False
        sys.exit()

    elif userChoice == '1':
        Soft.siteClearance()

    elif userChoice == '2':
        Soft.topSoilExcavation()

    elif userChoice == '3':
        Soft.remOfTopSoilExcav()

    elif userChoice == '4':
        Soft.trenchExcavation()

    elif userChoice == '5':
        Soft.levAndCompacting()

    elif userChoice == '6':
        Soft.concFooting()

    elif userChoice == '7':
        Soft.blockWorkInFDN()

    elif userChoice == '8':
        Soft.backfilling()

    elif userChoice == '9':
        Soft.remofSurpOffsite()

    elif userChoice == '10':
        Soft.latEarthFilling()

    elif userChoice == '11':
        Soft.hardcoreFilling()

    elif userChoice == '12':
        Soft.floorReinforcement()

    elif userChoice == '13':
        Soft.dampProofCourse()

    elif userChoice == '14':
        Soft.dampProofMembrane()

    elif userChoice == '15':
        Soft.surfaceLevelingAndCompacting()

    elif userChoice == '16':
        Soft.oversiteConcrete()

    elif userChoice == '17':
        Soft.oversiteConcreteFormwork()


# SUPERSTRUCTURE
    elif userChoice == '16':
        Soft.latEarthFilling()

    else:
        print("Invalid Input")
