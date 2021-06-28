import pandas as pd
import numpy as np
import csv


class Struct:
    def getSoftInit():
        global exportValueName, exportValue, exportValueUnit
        exportValueName = []
        exportValue = []
        exportValueUnit = []
        global bldLen, bldWid, spread, blockThicknessInFdn, girthBIF, girthBAF
        print("Please initialize the required values before you continue\n")
        bldLen = float(input(("Enter the length of the building: ")))
        bldWid = float(input("Enter the width of the building: "))
        spread = float(input("Enter the foundation spread: "))
        blockThicknessInFdn = float(input("Enter the thickness of blockwork in foundation: "))
        girthBIF = float(input('Enter the girth of blockwork in foundation: '))
        girthBAF = float(input("Enter girth for blockwork above foundation: "))

    def siteClearance():
        print("Calculating for Site Clearance")
        siteClr = ((bldLen+2) * (bldWid+2))
        print(siteClr)
        unit = 'M2'
        exportValueName.append('Site Clearance')
        exportValue.append(siteClr)
        exportValueUnit.append(unit)
        return siteClr

    def topSoilExcavation():
        global tsExcav
        print("Calculating for Top Soil Excavation")
        tsExcav = ((bldLen+(2*spread)) * (bldWid+(2*spread)))
        unit = 'M2'
        print(tsExcav)
        exportValueName.append("Top Soil Excavation")
        exportValue.append(tsExcav)
        exportValueUnit.append(unit)
        return tsExcav

    # Top soil removal

    def remOfTopSoilExcav():
        global remOfTSE
        remOfTSE = tsExcav * 0.15
        print(remOfTSE)
        unit = "M3"
        exportValueName.append("Removal of Top Soil Excavation")
        exportValue.append(remOfTSE)
        exportValueUnit.append(unit)
        return remOfTSE

    # Trench Excavation

    def trenchExcavation():
        global trenchExcav, depthOfFdn, widOfFdn
        widOfFdn = float(input("Enter the width of the foundation: "))
        depthOfFdn = float(input("Enter the depth of the foundation: "))
        trenchExcav = (girthBIF * widOfFdn * depthOfFdn)
        unit = "M3"
        exportValueName.append("Trench Excavation")
        exportValue.append(trenchExcav)
        exportValueUnit.append(unit)

        print(trenchExcav)
        return trenchExcav, depthOfFdn

    # Leveling and compacting

    def levAndCompacting():
        global levAndComp
        levAndComp = girthBIF * widOfFdn
        print(levAndComp)
        unit = "M2"
        exportValueName.append("Leveling and Compacting")
        exportValue.append(levAndComp)
        exportValueUnit.append(unit)
        return levAndComp

    # Concrete Footing

    def concFooting():
        global concFT, ftThickness
        ftThickness = float(input("Enter the thickness of the footing: "))
        concFT = girthBIF * widOfFdn * ftThickness
        concFT = round(concFT, 2)
        print(concFT)
        unit = "M3"
        exportValueName.append("Concrete Footing")
        exportValue.append(concFT)
        exportValueUnit.append(unit)
        return concFT, ftThickness

    # Blockwork in foundation

    def blockWorkInFDN():
        global blockWInFDN, expVal
        blckWkHeight = float(input("Enter the height of blockwork in foundation: "))
        blockWInFDN = girthBIF * blckWkHeight * blockThicknessInFdn
        expVal = girthBIF * blckWkHeight  # Value to be exported
        print(blockWInFDN)
        unit = "M2"
        exportValueName.append("Blockwork in Foundation")
        exportValue.append(expVal)
        exportValueUnit.append(unit)
        return blockWInFDN, expVal

    # Backfilling

    def backfilling():
        global bckFilling, remSurplusOffsite
        blockWInFDN2 = girthBIF * (depthOfFdn - ftThickness) * blockThicknessInFdn
        remSurplusOffsite = blockWInFDN2 + concFT
        bckFilling = trenchExcav - remSurplusOffsite
        print(bckFilling)
        unit = 'M3'
        exportValueName.append("Backfilling")
        exportValue.append(bckFilling)
        exportValueUnit.append(unit)
        return bckFilling, remSurplusOffsite

    # Removal of surplus offsite

    def remofSurpOffsite():
        global remSurplusOffsite
        remSurplusOffsite
        print(remSurplusOffsite)
        unit = 'M3'
        exportValueName.append("Removal of Surplus Offsite")
        exportValue.append(remSurplusOffsite)
        exportValueUnit.append(unit)
        return remSurplusOffsite

    # Laterite Earth Filling

    def latEarthFilling():
        global latEarthFill, fillingArea, areaOfBld, peremOfWall
        thicknessOfLatFillling = float(
            input("Enter the the thickness of laterite earth filling: "))
        areaOfBld = bldLen*bldWid
        peremOfWall = girthBIF * blockThicknessInFdn
        fillingArea = (areaOfBld - allRcsValues - peremOfWall)
        latEarthFill = fillingArea * thicknessOfLatFillling
        latEarthFill = round(latEarthFill, 2)
        unit = 'M3'
        exportValueName.append("Laterite Earth Filling")
        exportValue.append(latEarthFill)
        exportValueUnit.append(unit)
        print(latEarthFill)
        return latEarthFill, fillingArea, areaOfBld, peremOfWall

    # Hardcore filling

    def hardcoreFilling():
        global hardcoreFill
        thicknessOfCoreFillling = float(
            input("Enter the thickness of hardcore filling: "))
        hardcoreFill = fillingArea * thicknessOfCoreFillling
        print(hardcoreFill)
        unit = 'M3'
        exportValueName.append("Hardcore Filling")
        exportValue.append(hardcoreFill)
        exportValueUnit.append(unit)
        return hardcoreFill

    # Floor reinforcement

    def floorReinforcement():
        global floorReinf
        floorReinf = areaOfBld - allRcsValues
        print(floorReinf)
        unit = 'M2'
        exportValueName.append("Floor Reinforcement")
        exportValue.append(floorReinf)
        exportValueUnit.append(unit)
        return floorReinf

    # Damp proof course

    def dampProofCourse():
        global peremOfWall
        PDC = peremOfWall
        print(peremOfWall)
        unit = 'M2'
        exportValueName.append("Damp Proof Course")
        exportValue.append(peremOfWall)
        exportValueUnit.append(unit)
        return peremOfWall

    # Damp proof membrane

    def dampProofMembrane():
        global DPM
        DPM = floorReinf
        print(DPM)
        unit = "M2"
        exportValueName.append("Damp Proof Membrane")
        exportValue.append(DPM)
        exportValueUnit.append(unit)
        return DPM

    # Leveling and compacting on surface of filling

    def surfaceLevelingAndCompacting():
        global surfLvlAndComp
        surfLvlAndComp = fillingArea
        print(surfLvlAndComp)
        unit = 'M2'
        exportValueName.append("Leveling and Compacting on Surface of Filling")
        exportValue.append(surfLvlAndComp)
        exportValueUnit.append(unit)
        return surfLvlAndComp

    # Oversite concrete

    def oversiteConcrete():
        global oversiteConc, floorThickness
        floorThickness = float(input("Enter the floor thickness: "))
        oversiteConc = floorReinf * floorThickness
        print(oversiteConc)
        unit = 'M3'
        exportValueName.append("Oversite Concrete")
        exportValue.append(oversiteConc)
        exportValueUnit.append(unit)
        return oversiteConc

    # Formwork for oversite concrete

    def oversiteConcreteFormwork():
        global oversiteConcFormwork
        bldVal = (bldLen * 2) + (bldWid * 2)
        oversiteConcFormwork = bldVal * floorThickness
        print(oversiteConcFormwork)
        unit = "M2"
        exportValueName.append("Formwork for Oversite Concrete")
        exportValue.append(oversiteConcFormwork)
        exportValueUnit.append(unit)
        return oversiteConcFormwork

    def getRecessValue():
        global allRcsValues
        rcsTypes = input("How many type recess is present: ")
        rcsLengths = []
        rcsWidths = []
        rcsUnits = []
        rcsValues = []
        rcsTypes = int(rcsTypes)
        answer = 0
        for i in range(1):
            # Loop through to collect the lenght values
            for rcsLen in range(rcsTypes):
                rcsLenVal = float(input(
                    "Enter the lenght for recess type %s : " % (rcsLen+1)))
                rcsLengths.append((rcsLenVal))

            for rcsWid in range(rcsTypes):
                rcsWidVal = float(input(
                    "Enter the width for recess type %s : " % (rcsWid+1)))
                rcsWidths.append(rcsWidVal)

            for rcsUnit in range(rcsTypes):
                rcsUnitVal = float(input(
                    "How many unit of recess type %s : " % (rcsUnit+1)))
                rcsUnits.append(rcsUnitVal)

            for value in range(rcsTypes):
                rcsValue = (
                    rcsLengths[value] * rcsWidths[value] * rcsUnits[value])
                rcsValues.append(rcsValue)
        allRcsValues = sum(rcsValues)
        print("Total recesses value is %s" % allRcsValues)
        return allRcsValues

    def getRingsAndBarDia():
        global weightOfBars, weightOfRings
        diamOfBars = float(input("what is the diameter of bars in lintel: "))
        diamOfRings = float(input("what is the diameter of rings in lintel: "))
        weightOfBars = ((diamOfBars*diamOfBars)/162)  # refactor with math lib
        weightOfRings = ((diamOfRings*diamOfRings)/162)
        return weightOfBars, weightOfRings

    def getWindowsValue():
        global allWndowsValue, allWindowsLintelValue, allWindowLintelFormworkValue, windowLintelReinforcementValue, allWindowLintelReinforcementRingValue, allWindowsRevValue, blockThickness
        blockThickness = wtAF
        windowTypes = input("How many type of windows is used: ")
        # Windows Dimensions
        windowLengths = []
        windowWidths = []
        windowUnits = []
        windowsValues = []
        # Windows for Lintel
        windowLintelLens = []
        windowLintelUnits = []
        windowLintelValues = []
        # Formwork for Lintels
        windowLintelFormworkLengths = []
        windowLintelFormworkUnits = []
        windowLintelFormworkValues = []
        # Reinforcement in Lintel Bars
        windowLintelReinforcementLengths = []
        windowLintelReinforcementUnits = []
        windowLintelReinforcementValues = []
        # Reinforcement in Lintel Rings
        windowLintelReinforcementRingLengths = []
        windowLintelReinforcementRingUnits = []
        windowLintelReinforcementRingValues = []
        # Windows Reavels
        windowRevLengths = []
        windowRevWidths = []
        windowRevUnits = []
        windowsRevValues = []

        windowTypes = int(windowTypes)
        for i in range(1):
            # Loop through to collect the lenght values
            for winLen in range(windowTypes):
                winLenVal = float(input(
                    "Enter the lenght for window type %s : " % (winLen+1)))
                windowLengths.append((winLenVal))
                windowLintelLens.append(winLenVal)
                windowLintelFormworkLengths.append(winLenVal)
                windowLintelReinforcementLengths.append(winLenVal)
                windowLintelReinforcementRingLengths.append(winLenVal)
                windowRevLengths.append(winLenVal)

            for winWid in range(windowTypes):
                winWidVal = float(input(
                    "Enter the width for window type %s : " % (winWid+1)))
                windowWidths.append(winWidVal)
                windowRevWidths.append(winWidVal)

            for winUnit in range(windowTypes):
                winUnitVal = float(input(
                    "How many unit of window type %s : " % (winUnit+1)))
                windowUnits.append(winUnitVal)
                windowLintelUnits.append(winUnitVal)
                windowLintelFormworkUnits.append(winUnitVal)
                windowLintelReinforcementUnits.append(winUnitVal)
                windowLintelReinforcementRingUnits.append(winUnitVal)
                windowRevUnits.append(winUnitVal)

            for value in range(windowTypes):
                windowsValue = (
                    windowLengths[value] * windowWidths[value] * windowUnits[value])
                windowLintelValue = (
                    (windowLintelLens[value] + 0.45) * 0.23 * windowLintelUnits[value] * blockThickness)
                windowLintelFormworkValue = (
                    (windowLintelLens[value] + 0.45) * 0.23 * windowLintelUnits[value] * 3)
                windowLintelReinforcementValue = ((windowLintelReinforcementLengths[value]+0.65)*4 * windowLintelReinforcementUnits[value]*weightOfBars)
                windowLintelReinforcementRingValue = (lenghtOfRings * ((windowLintelReinforcementRingLengths[value]+0.45)/0.2)+1) * windowLintelReinforcementRingUnits[value] * weightOfRings
                windowsRevValue = (((windowRevLengths[value]*2) + (windowRevWidths[value]*2))*windowRevUnits[value])

                windowsValues.append(windowsValue)
                windowLintelValues.append(windowLintelValue)
                windowLintelFormworkValues.append(windowLintelFormworkValue)
                windowLintelReinforcementValues.append(windowLintelReinforcementValue)
                windowLintelReinforcementRingValues.append(windowLintelReinforcementRingValue)
                windowsRevValues.append(windowsRevValue)
                allWindowLintelFormworkValue = sum(windowLintelFormworkValues)
                allWndowsValue = sum(windowsValues)
                allWindowsLintelValue = sum(windowLintelValues)
                windowLintelReinforcementValue = sum(windowLintelReinforcementValues)
                allWindowLintelReinforcementRingValue = sum(windowLintelReinforcementRingValues)
                allWindowsRevValue = sum(windowsRevValues)
                allWndowsValue = round(allWndowsValue, 2)
                allWindowsLintelValue = round(allWindowsLintelValue, 2)
                allWindowLintelFormworkValue = round(
                    allWindowLintelFormworkValue, 2)
                windowLintelReinforcementValue = round(windowLintelReinforcementValue, 2)
                allWindowLintelReinforcementRingValue = round(allWindowLintelReinforcementRingValue, 2)
                allWindowsRevValue = round(allWindowsRevValue, 2)

                print("Total windows value is %s\n" % allWndowsValue)
                print("Total Lintel windows value is %s" %
                      allWindowsLintelValue)
        return allWndowsValue, allWindowsLintelValue, allWindowLintelFormworkValue, windowLintelReinforcementValue, allWindowLintelReinforcementRingValue, allWindowsRevValue

    def getDoorsValue():
        global allDoorsValue, allDoorsLintelValue, allDoorLintelFormworkValue, doorLintelReinforcementValue, allDoorLintelReinforcementRingValue, alldoorFinishingValues
        doorTypes = input("How many type of door is used: ")
        # Door Dimension
        doorLengths = []
        doorWidths = []
        doorUnits = []
        doorValues = []
        # Doors Lintel
        doorLintelLengths = []
        doorLintelUnits = []
        doorLintelValues = []
        # Doors lintel formwork
        doorLintelFormworkLengths = []
        doorLintelFormworkUnits = []
        doorLintelFormworkValues = []
        # Reinforcement in Lintel Bars
        doorLintelReinforcementLengths = []
        doorLintelReinforcementUnits = []
        doorLintelReinforcementValues = []
        # Reinforcement in Lintel Rings
        doorLintelReinforcementRingLengths = []
        doorLintelReinforcementRingUnits = []
        doorLintelReinforcementRingValues = []
        # Door Finishing Area
        doorFinishingLengths = []
        doorFinishingUnits = []
        doorFinishingValues = []

        doorTypes = int(doorTypes)
        for i in range(1):
            # Loop through to collect the lenght values
            for doorLen in range(doorTypes):
                doorLenVal = float(input(
                    "Enter the lenght for door type %s : " % (doorLen+1)))
                doorLengths.append((doorLenVal))
                doorLintelLengths.append(doorLenVal)
                doorLintelFormworkLengths.append(doorLenVal)
                doorLintelReinforcementLengths.append(doorLenVal)
                doorLintelReinforcementRingLengths.append(doorLenVal)
                doorFinishingLengths.append(doorLenVal)

            for doorWid in range(doorTypes):
                doorWidVal = float(input(
                    "Enter the width for door type %s : " % (doorWid+1)))
                doorWidths.append(doorWidVal)

            for doorUnit in range(doorTypes):
                doorUnitVal = int(input(
                    "How many unit of door type %s : " % (doorUnit+1)))
                doorUnits.append(doorUnitVal)
                doorLintelUnits.append(doorUnitVal)
                doorLintelFormworkUnits.append(doorUnitVal)
                doorLintelReinforcementUnits.append(doorUnitVal)
                doorLintelReinforcementRingUnits.append(doorUnitVal)
                doorFinishingUnits.append(doorUnitVal)

            for value in range(doorTypes):
                doorValue = (
                    doorLengths[value] * doorWidths[value] * doorUnits[value])
                doorLintelValue = (
                    (doorLintelLengths[value] + 0.45) * 0.23 * doorLintelUnits[value] * blockThickness)
                doorValues.append(doorValue)
                doorLintelFormworkValue = (
                    (doorLintelLengths[value] + 0.45) * 0.23 * doorLintelUnits[value] * 3)
                doorLintelReinforcementValue = ((doorLintelReinforcementLengths[value] + 0.65)*4*doorLintelReinforcementUnits[value]*weightOfBars)
                doorLintelReinforcementRingValue = (lenghtOfRings * ((doorLintelReinforcementRingLengths[value]+0.45)/0.2)+1) * doorLintelReinforcementRingUnits[value] * weightOfRings
                doorFinishingValue = (doorFinishingLengths[value]*doorFinishingUnits[value]*wtAF)

                doorValues.append(doorValue)
                doorLintelValues.append(doorLintelValue)
                doorLintelFormworkValues.append(doorLintelFormworkValue)
                doorLintelReinforcementValues.append(doorLintelReinforcementValue)
                doorFinishingValues.append(doorFinishingValue)

        allDoorsValue = sum(doorValues)
        allDoorsValue = round(allDoorsValue, 2)
        allDoorsLintelValue = sum(doorLintelValues)
        allDoorsLintelValue = round(allDoorsLintelValue, 2)
        allDoorLintelFormworkValue = sum(doorLintelFormworkValues)
        allDoorLintelFormworkValue = round(allDoorLintelFormworkValue, 2)
        allDoorLintelReinforcementValue = sum(doorLintelReinforcementValues)
        doorLintelReinforcementValue = round(doorLintelReinforcementValue, 2)
        allDoorLintelReinforcementRingValue = sum(doorLintelReinforcementRingValues)
        allDoorLintelReinforcementRingValue = round(doorLintelReinforcementRingValue, 2)
        allDoorFinishingValue = sum(doorFinishingValues)
        alldoorFinishingValues = round(allDoorFinishingValue, 2)
        print("Total windows value is %s" % allDoorsValue)
        return allDoorsValue, allDoorsLintelValue, allDoorLintelFormworkValue, doorLintelReinforcementValue, allDoorLintelReinforcementRingValue, alldoorFinishingValues

    def getOtherOpeningsValue():
        global allopnValues, allOpnLintelValues, allOpnLintelFormworkValues, allOpnLintelReinforcementValues, allOpnLintelReinforcementRingValues
        opnTypes = input("How many other opening types are present: ")
        # Ohter openings Dimension
        opnLengths = []
        opnWidths = []
        opnUnits = []
        opnValues = []
        # Other openings Lintel value
        opnLintelLenghts = []
        opnLintelUnits = []
        opnLintelValues = []
        # Other opening lintel formwork
        opnLintelFormworkLenghts = []
        opnLintelFormworkUnits = []
        opnLintelFormworkValues = []
        # Other opening reinforcement in lintel Bars
        opnLintelReinforcementLengths = []
        opnLintelReinforcementUnits = []
        opnLintelReinforcementValues = []
        # Reinforcement in Lintel Rings
        opnLintelReinforcementRingLengths = []
        opnLintelReinforcementRingUnits = []
        opnLintelReinforcementRingValues = []

        opnTypes = int(opnTypes)
        for i in range(1):
            # Loop through to collect the lenght values
            for opnLen in range(opnTypes):
                opnLenVal = float(input(
                    "Enter the lenght for opening type %s : " % (opnLen+1)))
                opnLengths.append((opnLenVal))
                opnLintelLenghts.append(opnLenVal)
                opnLintelFormworkLenghts.append(opnLenVal)
                opnLintelReinforcementLengths.append(opnLenVal)
                opnLintelReinforcementRingLengths.append(opnLenVal)

            for opnWid in range(opnTypes):
                opnWidVal = float(input(
                    "Enter the width for opening type %s : " % (opnWid+1)))
                opnWidths.append(opnWidVal)

            for opnUnit in range(opnTypes):
                opnUnitVal = int(input(
                    "How many unit of opening type %s : " % (opnUnit+1)))
                opnUnits.append(opnUnitVal)
                opnLintelUnits.append(opnUnitVal)
                opnLintelFormworkUnits.append(opnUnitVal)
                opnLintelReinforcementUnits.append(opnUnitVal)
                opnLintelReinforcementRingUnits.append(opnUnitVal)

            for value in range(opnTypes):
                opnValue = (
                    opnLengths[value] * opnWidths[value] * opnUnits[value])
                opnLintelValue = (
                    (opnLengths[value] + 0.45) * 0.23 * opnLintelUnits[value] * blockThickness)
                opnValues.append(opnValue)
                opnLintelFormworkValue = (
                    (opnLengths[value] + 0.45) * 0.23 * opnLintelUnits[value] * blockThickness)
                opnLintelReinforcementValue = ((opnLintelReinforcementLengths[value]+0.65)*4*opnLintelReinforcementUnits[value]*weightOfBars)
                opnLintelReinforcementRingValue = (lenghtOfRings * ((opnLintelReinforcementRingLengths[value]+0.45)/0.2)+1) * opnLintelReinforcementRingUnits[value] * weightOfRings
                opnValues.append(opnValue)
                opnLintelValues.append(opnLintelValue)
                opnLintelFormworkValues.append(opnLintelFormworkValue)
                opnLintelReinforcementValues.append(opnLintelReinforcementValue)
                opnLintelReinforcementRingValues.append(opnLintelReinforcementRingValue)
                allopnValues = sum(opnValues)
                allOpnLintelValues = sum(opnLintelValues)
                allOpnLintelFormworkValues = sum(opnLintelFormworkValues)
                allOpnLintelReinforcementValues = sum(opnLintelReinforcementValues)
                allOpnLintelReinforcementRingValues = sum(opnLintelReinforcementRingValues)
                allopnValues = round(allopnValues, 2)
                allOpnLintelValues = round(allOpnLintelValues, 2)
                allOpnLintelFormworkValues = round(allOpnLintelFormworkValues)
                allOpnLintelReinforcementValues = round(allOpnLintelReinforcementValues)
                allOpnLintelReinforcementRingValues = round(allOpnLintelReinforcementRingValues, 2)
        print("Total other openings value is %s" % allopnValues)
        return allopnValues, allOpnLintelValues, allOpnLintelFormworkValues, allOpnLintelReinforcementValues, allOpnLintelReinforcementRingValues

    def getWallThickness():
        global wtAF, lenghtOfRings
        wtAF = float(input("Enter the wall thickness above foundation (in meter): "))
        if wtAF == 0.23:
            lenghtOfRings = 0.82
        elif wtAF == 0.15:
            lenghtOfRings = 0.54
        else:
            lenghtOfRings = 0.82

        print(wtAF, lenghtOfRings)
        return wtAF, lenghtOfRings

    def blckWkAboveGndLvl():
        global blockworkInSuper, headRoom, sumOfAllOpenings, totalLintelArea
        headRoom = float(input("Enter the height of blockwork in superstructure: "))
        blockworkInSuper = girthBAF * headRoom
        sumOfAllOpenings = allWndowsValue + allDoorsValue + allopnValues
        totalLintelArea = (allWindowsLintelValue + allDoorsLintelValue + allOpnLintelValues)/wtAF
        totalBlockworkInSuper = blockworkInSuper - (sumOfAllOpenings+totalLintelArea)
        unit = "M2"
        exportValueName.append("Blockwork Above Ground Level")
        exportValue.append(totalBlockworkInSuper)
        exportValueUnit.append(unit)
        return totalBlockworkInSuper

    def plasteringRendering():
        plastblockworkInSuper = (girthBAF * headRoom) * 2
        plastsumOfAllOpenings = (allWndowsValue + allDoorsValue + allopnValues)*2
        totalPlastBlockworkInSuper = blockworkInSuper - (sumOfAllOpenings+totalLintelArea)
        print('The Plastering and rendering value is %s' % totalPlastBlockworkInSuper)
        unit = "M2"
        exportValueName.append("Plastering and Rendering")
        exportValue.append(totalPlastBlockworkInSuper)
        exportValueUnit.append(unit)
        return totalPlastBlockworkInSuper

    def floorFinish():
        flrFinish = areaOfBld - allRcsValues - ((girthBAF * wtAF) - alldoorFinishingValues)
        unit = 'M2'
        exportValueName.append("Floor Finishes")
        exportValue.append(flrFinish)
        exportValueUnit.append(unit)
        return flrFinish

    def cielingFinish():
        ceilingFinish = areaOfBld - allRcsValues - (girthBAF * wtAF)
        unit = 'M2'
        exportValueName.append("Ceiling Finishes")
        exportValue.append(ceilingFinish)
        exportValueUnit.append(unit)
        return ceilingFinish

    def windowRevels():
        totalWindowRev = allWindowsRevValue
        unit = "M"
        exportValueName.append("Window Reveals")
        exportValue.append(totalWindowRev)
        exportValueUnit.append(unit)
        return totalWindowRev

    def concInLintel():
        concInLint = [allWindowsLintelValue, allDoorsLintelValue, allOpnLintelValues]
        concInLint = sum(concInLint)
        concInLint = round(concInLint, 2)
        unit = "M3"
        exportValueName.append("Concrete in Lintel")
        exportValue.append(concInLint)
        exportValueUnit.append(unit)
        print("The value of concrete in lintel is %s " % concInLint)
        return concInLint

    def reinforcementBarsInLintel():
        reinfInLint = [windowLintelReinforcementValue, doorLintelReinforcementValue, allOpnLintelReinforcementValues]
        reinfInLint = sum(reinfInLint)
        reinfInLint = round(reinfInLint, 2)
        print("The value of reinforcement bars in lintel is %s" % reinfInLint)
        unit = "KG"
        exportValueName.append("Reinforcement Bars in Lintel")
        exportValue.append(reinfInLint)
        exportValueUnit.append(unit)
        return reinfInLint

    def reinforcementRingsInLintel():
        reinfRingsInLint = [allWindowLintelReinforcementRingValue, allDoorLintelReinforcementRingValue, allOpnLintelReinforcementRingValues]
        reinfRingsInLint = sum(reinfRingsInLint)
        reinfRingsInLint = round(reinfRingsInLint, 2)
        print("The value for reinforcement rings in lintel is %s" % reinfRingsInLint)
        unit = "KG"
        exportValueName.append("Reinforcement Rings in Lintel")
        exportValue.append(reinfRingsInLint)
        exportValueUnit.append(unit)
        return reinfRingsInLint

    def formWorkInLintel():
        formworkInLint = [allWindowLintelFormworkValue, allDoorLintelFormworkValue, allOpnLintelFormworkValues]
        formworkInLint = sum(formworkInLint)
        formworkInLint = round(formworkInLint, 2)
        print("The value of formwork in lintel is %s" % formworkInLint)
        unit = "M2"
        exportValueName.append("Formwork in Lintel")
        exportValue.append(formworkInLint)
        exportValueUnit.append(unit)
        return formworkInLint

        # Generating the final value of calculations made
    def generateSpreadSheet():
        nameBody = []
        valueBody = []
        unitBody = []
        valuesHeading = ["TRADE LIST", "QUANTITY", "UNIT"]
        for name in exportValueName:
            nameBody.append(name)

        for value in exportValue:
            valueBody.append(value)

        for unit in exportValueUnit:
            unitBody.append(unit)

            # Write the title of the report
        with open("report.csv", 'w+', newline='') as report:
            csvWriter = csv.writer(report)
            csvWriter.writerow(valuesHeading)

            # Write the names of the report
        with open("report.csv", 'a', newline=None) as generalCSV:
            csvWriter = csv.writer(generalCSV)
            csvWriter.writerow(exportValueName)

            # Write the Values of the report
        with open("report.csv", 'a', newline=None) as generalCSV:
            csvWriter = csv.writer(generalCSV)
            csvWriter.writerow(exportValue)

            # Write the Units of the report
        with open("report.csv", 'a', newline=None) as generalCSV:
            csvWriter = csv.writer(generalCSV)
            csvWriter.writerow(exportValueUnit)
