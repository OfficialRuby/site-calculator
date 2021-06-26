class Soft:
    def getInit():
        global bldLen, bldWid, spread, blockThickness, girthBIF
        print("Please initialize the required values before you continue\n")
        bldLen = float(input(("Enter the length of the building: ")))
        bldWid = float(input("Enter the width of the building: "))
        spread = float(input("Enter the foundation spread: "))
        blockThickness = float(input("Enter the thickness of blockwork in foundation: "))
        girthBIF = float(input('Enter the girth of blockwork in foundation: '))

    def siteClearance():
        print("Calculating for Site Clearance")
        siteClr = ((bldLen+2) * (bldWid+2))
        print(siteClr)
        return siteClr

    def topSoilExcavation():
        global tsExcav
        print("Calculating for Top Soil Excavation")
        tsExcav = ((bldLen+(2*spread)) * (bldWid+(2*spread)))
        print(tsExcav)
        return tsExcav

    # Top soil removal

    def remOfTopSoilExcav():
        global remOfTSE
        remOfTSE = tsExcav * 0.15
        print(remOfTSE)
        return remOfTSE

    # Trench Excavation

    def trenchExcavation():
        global trenchExcav, depthOfFdn, widOfFdn
        widOfFdn = float(input("Enter the width of the foundation: "))
        depthOfFdn = float(input("Enter the depth of the foundation: "))
        trenchExcav = (girthBIF * widOfFdn * depthOfFdn)
        print(trenchExcav)
        return trenchExcav, depthOfFdn

    # Leveling and compacting

    def levAndCompacting():
        global levAndComp
        levAndComp = girthBIF * widOfFdn
        print(levAndComp)
        return levAndComp

    # Concrete Footing

    def concFooting():
        global concFT, ftThickness
        ftThickness = float(input("Enter the thickness of the footing: "))
        concFT = girthBIF * widOfFdn * ftThickness
        concFT = round(concFT, 2)
        print(concFT)
        return concFT, ftThickness

    # Blockwork in foundation

    def blockWorkInFDN():
        global blockWInFDN, expVal
        blckWkHeight = float(input("Enter the height of blockwork in foundation: "))
        blockWInFDN = girthBIF * blckWkHeight * blockThickness
        expVal = girthBIF * blckWkHeight  # Value to be exported
        print(blockWInFDN)
        return blockWInFDN, expVal

    # Backfilling

    def backfilling():
        global bckFilling, remSurplusOffsite
        blockWInFDN2 = girthBIF * (depthOfFdn - ftThickness) * blockThickness
        remSurplusOffsite = blockWInFDN2 + concFT
        bckFilling = trenchExcav - remSurplusOffsite
        print(bckFilling)
        # Export remSurplusOffsite in Removal of Surplus Offsite
        return bckFilling, remSurplusOffsite

    # Removal of surplus offsite

    def remofSurpOffsite():
        global remSurplusOffsite
        remSurplusOffsite
        print(remSurplusOffsite)
        return remSurplusOffsite

    # Laterite Earth Filling

    def latEarthFilling():
        global latEarthFill, fillingArea, areaOfBld, peremOfWall
        thicknessOfLatFillling = float(
            input("Enter the the thickness of laterite earth filling: "))
        areaOfBld = bldLen*bldWid
        peremOfWall = girthBIF * blockThickness
        fillingArea = (areaOfBld - allRcsValues - peremOfWall)
        latEarthFill = fillingArea * thicknessOfLatFillling
        latEarthFill = round(latEarthFill, 2)
        print(latEarthFill)
        return latEarthFill, fillingArea, areaOfBld, peremOfWall

    # Hardcore filling

    def hardcoreFilling():
        global hardcoreFill
        thicknessOfCoreFillling = float(
            input("Enter the thickness of hardcore filling: "))
        hardcoreFill = fillingArea * thicknessOfCoreFillling
        print(hardcoreFill)
        return hardcoreFill

    # Floor reinforcement

    def floorReinforcement():
        global floorReinf
        floorReinf = areaOfBld - recess
        print(floorReinf)
        return floorReinf

    # Damp proof course

    def dampProofCourse():
        global peremOfWall
        PDC = peremOfWall
        print(peremOfWall)
        return peremOfWall

    # Damp proof membrane

    def dampProofMembrane():
        global DPM
        DPM = floorReinf
        print(DPM)
        return DPM

    # Leveling and compacting on surface of filling

    def surfaceLevelingAndCompacting():
        global surfLvlAndComp
        surfLvlAndComp = fillingArea
        print(surfLvlAndComp)
        return surfLvlAndComp

    # Oversite concrete

    def oversiteConcrete():
        global oversiteConc
        floorThickness = int(input("Enter the floor thickness: "))
        oversiteConc = floorReinf * floorThickness
        print(oversiteConc)
        return oversiteConc

    # Formwork for oversite concrete

    def oversiteConcreteFormwork():
        global oversiteConcFormwork
        bldVal = (bldLen * 2) + (bldWid * 2)
        oversiteConcFormwork = bldVal * floorThickness
        print(oversiteConcFormwork)
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
