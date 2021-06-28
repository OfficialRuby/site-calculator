#!/usr/bin/python3
import sys
import time
import os
from modules.structure import Struct
from modules.superstructure import Super

try:
    print("Creating folder for take off report")
    time.sleep((1.5))
    os.mkdir('REPORTS')
    print("Created the folder 'REPORTS' ")
except FileExistsError:
    print("REPORTS folder already exists")

try:
    Struct.getSoftInit()
    Struct.getRecessValue()
    Struct.getRingsAndBarDia()
    Struct.getWallThickness()
    Struct.getWindowsValue()
    Struct.getDoorsValue()
    Struct.getOtherOpeningsValue()

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
    18. Concrete in Lintel
    19. Reiforcement in Lintel
    20. Formwork in Lintel
    21. Plastering/Rendering
    22. Painting
    23. Floor Finishes
    24. Ceiling Finishes
    25. Window Revel
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
            Struct.siteClearance()

        elif userChoice == '2':
            Struct.topSoilExcavation()

        elif userChoice == '3':
            Struct.remOfTopSoilExcav()

        elif userChoice == '4':
            Struct.trenchExcavation()

        elif userChoice == '5':
            Struct.levAndCompacting()

        elif userChoice == '6':
            Struct.concFooting()

        elif userChoice == '7':
            Struct.blockWorkInFDN()

        elif userChoice == '8':
            Struct.backfilling()

        elif userChoice == '9':
            Struct.remofSurpOffsite()

        elif userChoice == '10':
            Struct.latEarthFilling()

        elif userChoice == '11':
            Struct.hardcoreFilling()

        elif userChoice == '12':
            Struct.floorReinforcement()

        elif userChoice == '13':
            Struct.dampProofCourse()

        elif userChoice == '14':
            Struct.dampProofMembrane()

        elif userChoice == '15':
            Struct.surfaceLevelingAndCompacting()

        elif userChoice == '16':
            Struct.oversiteConcrete()

        elif userChoice == '17':
            Struct.oversiteConcreteFormwork()

    # SUPERSTRUCTURE
        elif userChoice == '18':
            Struct.concInLintel()

        elif userChoice == '19':
            Struct.reinforcementBarsInLintel()
        elif userChoice == '20':
            Struct.formWorkInLintel()
        elif userChoice == '21':
            Struct.plasteringRendering()
        elif userChoice == '22':
            Struct.plasteringRendering()
        elif userChoice == '23':
            Struct.floorFinish()
        elif userChoice == '24':
            Struct.cielingFinish()
        elif userChoice == '25':
            Struct.windowRevels()
        else:
            print("Invalid Input")
except KeyboardInterrupt:
    print("\nProgram terminated by user")
