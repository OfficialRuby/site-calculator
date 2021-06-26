class Tools:
    # TODO: strip wall thickness value
    def getRingsAndBarDia():
        diamOfBars = float(input("what is the diameter of bars in lintel: "))
        diamOfRings = float(input("what is the diameter of rings in lintel: "))
        weightOfBars = ((diamOfBars*diamOfBars)/162)  # refactor with math lib
        weightOfRings = ((diamOfRings*diamOfRings)/162)
        return weightOfBars, weightOfRings  # global

    def getWindowsValue():
        blockThickness = float(input("Enter the thickness for block: "))
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
                windowsRevValue = (((windowRevLengths[value]*2) + (windowRevWidths[value]*2))*windowRevUnits)

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
                doorLenVal = int(input(
                    "Enter the lenght for door type %s : " % (doorLen+1)))
                doorLengths.append((doorLenVal))
                doorLintelLengths.append(doorLenVal)
                doorLintelFormworkLengths.append(doorLenVal)
                doorLintelReinforcementLengths.append(doorLenVal)
                doorLintelReinforcementRingLengths.append(doorLenVal)
                doorFinishingLengths.append((doorLenVal))

            for doorWid in range(doorTypes):
                doorWidVal = int(input(
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
        allDoorFinishingValues = sum(doorFinishingValues)
        alldoorFinishingValues = round(doorFinishingValues, 2)
        print("Total windows value is %s" % allDoorsValue)
        return allDoorsValue, allDoorsLintelValue, allDoorLintelFormworkValue, doorLintelReinforcementValue, allDoorLintelReinforcementRingValue, alldoorFinishingValue

    def getOtherOpeningsValue():
        opnTypes = input("How many type opening is present: ")
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
                opnLenVal = int(input(
                    "Enter the lenght for opening type %s : " % (opnLen+1)))
                opnLengths.append((opnLenVal))
                opnLintelLenghts.append(opnLenVal)
                opnLintelFormworkLenghts.append(opnLenVal)
                opnLintelReinforcementLengths.append(opnLenVal)
                opnLintelReinforcementRingLengths.append(opnLenVal)

            for opnWid in range(opnTypes):
                opnWidVal = int(input(
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
                allOpnLintelValues = round(opnLintelValues, 2)
                allopnLintelFormworkValues = round(allopnLintelFormworkValues)
                allOpnLintelReinforcementValues = round(opnLintelReinforcementValues)
                allOpnLintelReinforcementRingValues = round(allOpnLintelReinforcementRingValues, 2)
        print("Total other openings value is %s" % allopnValues)
        return opnLintelValues, allOpnLintelValues, allopnLintelFormworkValues, allOpnLintelReinforcementValues, allOpnLintelReinforcementRingValues

    def getRecessValue():
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
                rcsLenVal = int(input(
                    "Enter the lenght for recess type %s : " % (rcsLen+1)))
                rcsLengths.append((rcsLenVal))

            for rcsWid in range(rcsTypes):
                rcsWidVal = int(input(
                    "Enter the width for recess type %s : " % (rcsWid+1)))
                rcsWidths.append(rcsWidVal)

            for rcsUnit in range(rcsTypes):
                rcsUnitVal = int(input(
                    "How many unit of recess type %s : " % (rcsUnit+1)))
                rcsUnits.append(rcsUnitVal)

            for value in range(rcsTypes):
                rcsValue = (
                    rcsLengths[value] * rcsWidths[value] * rcsUnits[value])
                rcsValues.append(rcsValue)
        answer = sum(rcsValues)
        print("Total recesses value is %s" % answer)
        return answer

    def getGirth():
        girthBIF = int(input('Enter the girth of blockwork in foundation: '))
        girthBAF = int(input("Enter girth for blockwork above foundation: "))
        print(girthBIF, girthBAF)
        return girthBIF, girthBAF

    def getWallThickness():
        global wiIF, wtAF, spread, lenghtOfRings
        wtIF = float(input("Enter the wall thickness in foundation (in meter): "))
        wtAF = float(input("Enter the wall thickness above foundation (in meter): "))
        if wtAF == 0.23:
            lenghtOfRings = 0.82
        else:
            lenghtOfRings = 0.54

        spread = wtIF
        print(wtIF, wtAF, spread)
        return wtIF, wtAF, spread, lenghtOfRings

    def blckWkAboveGndLvl():
        headRoom = float(input("Enter the height of blockwork in superstructure: "))
        blockworkInSuper = girthBAF * headRoom
        sumOfAllOpenings = allWndowsValue + allDoorsValue + opnLintelValues
        totalLintelArea = (allWindowsLintelValue + allDoorsLintelValue + allOpnLintelValues)/wtAF
        totalBlockworkInSuper = blockworkInSuper - (sumOfAllOpenings+totalLintelArea)
        return totalBlockworkInSuper

    def platering():
        headRoom = float(input("Enter the height of blockwork in superstructure: "))
        plastblockworkInSuper = (girthBAF * headRoom) * 2
        plastsumOfAllOpenings = (allWndowsValue + allDoorsValue + opnLintelValues)*2
        totalPlastBlockworkInSuper = blockworkInSuper - (sumOfAllOpenings+totalLintelArea)
        return totalPlastBlockworkInSuper

    def floorFinish():
        flrFinish = areaOfBld - recess - ((giAF * wtAF) - alldoorFinishingValue)
        return flrFinish

    def cielingFinish():
        ceilingFinish = areaOfBld - recess - (giAF * wtAF)
        return ceilingFinish

    def windowRevels():
        totalWindowRev = allWindowsRevValue
        return totalWindowRev
