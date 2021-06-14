class Tools:

    def getWindowsValue():
        blockThickness = float(input("Enter the thickness for block: "))
        windowTypes = input("How many type of windows is used: ")
        # Windows Dimensions
        windowLengths = []
        windowWidths = []
        windowUnits = []
        windowsValues = []
        # Windows Lintel
        windowLintelLens = []
        windowLintelUnits = []
        windowLintelValues = []
        # Formwork for Lintels
        windowLintelFormworkLengths = []
        windowLintelFormworkUnits = []
        windowLintelFormworkValues = []

        windowTypes = int(windowTypes)
        for i in range(1):
            # Loop through to collect the lenght values
            for winLen in range(windowTypes):
                winLenVal = float(input(
                    "Enter the lenght for window type %s : " % (winLen+1)))
                windowLengths.append((winLenVal))
                windowLintelLens.append(winLenVal)
                windowLintelFormworkLengths.append(winLenVal)

            for winWid in range(windowTypes):
                winWidVal = float(input(
                    "Enter the width for window type %s : " % (winWid+1)))
                windowWidths.append(winWidVal)

            for winUnit in range(windowTypes):
                winUnitVal = float(input(
                    "How many unit of window type %s : " % (winUnit+1)))
                windowUnits.append(winUnitVal)
                windowLintelUnits.append(winUnitVal)
                windowLintelFormworkUnits.append(winUnitVal)

            for value in range(windowTypes):
                windowsValue = (
                    windowLengths[value] * windowWidths[value] * windowUnits[value])
                windowLintelValue = (
                    (windowLintelLens[value] + 0.45) * 0.23 * windowLintelUnits[value] * blockThickness)
                windowLintelFormworkValue = (
                    (windowLintelLens[value] + 0.45) * 0.23 * windowLintelUnits[value] * 3)

                windowsValues.append(windowsValue)
                windowLintelValues.append(windowLintelValue)
                windowLintelFormworkValues.append(windowLintelFormworkValue)
                allWindowLintelFormworkValue = sum(windowLintelFormworkValues)
                allWndowsValue = sum(windowsValues)
                allWindowsLintelValue = sum(windowLintelValues)
                allWndowsValue = round(allWndowsValue, 2)
                allWindowsLintelValue = round(allWindowsLintelValue, 2)
                allWindowLintelFormworkValue = round(
                    allWindowLintelFormworkValue, 2)
                print("Total windows value is %s\n" % allWndowsValue)
                print("Total Lintel windows value is %s" %
                      allWindowsLintelValue)
        return allWndowsValue, allWindowsLintelValue, allWindowLintelFormworkValue

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

        doorTypes = int(doorTypes)
        for i in range(1):
            # Loop through to collect the lenght values
            for doorLen in range(doorTypes):
                doorLenVal = int(input(
                    "Enter the lenght for door type %s : " % (doorLen+1)))
                doorLengths.append((doorLenVal))
                doorLintelLengths.append(doorLenVal)
                doorLintelFormworkLengths.append(doorLenVal)

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

            for value in range(doorTypes):
                doorValue = (
                    doorLengths[value] * doorWidths[value] * doorUnits[value])
                doorLintelValue = (
                    (doorLintelLengths[value] + 0.45) * 0.23 * doorLintelUnits[value] * blockThickness)
                doorValues.append(doorValue)
                doorLintelFormworkValue = (
                    (doorLintelLengths[value] + 0.45) * 0.23 * doorLintelUnits[value] * 3)
                doorValues.append(doorValue)
                doorLintelValues.append(doorLintelValue)
                doorLintelFormworkValues.append(doorLintelFormworkValue)

        allDoorsValue = sum(doorValues)
        allDoorsValue = round(allDoorsValue, 2)
        allDoorsLintelValue = sum(doorLintelValues)
        allDoorsLintelValue = round(allDoorsLintelValue, 2)
        allDoorLintelFormworkValue = sum(doorLintelFormworkValues)
        allDoorLintelFormworkValue = round(allDoorLintelFormworkValue, 2)
        print("Total windows value is %s" % allDoorsValue)
        return allDoorsValue, allDoorsLintelValue, allDoorLintelFormworkValue

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

        opnTypes = int(opnTypes)
        for i in range(1):
            # Loop through to collect the lenght values
            for opnLen in range(opnTypes):
                opnLenVal = int(input(
                    "Enter the lenght for opening type %s : " % (opnLen+1)))
                opnLengths.append((opnLenVal))
                opnLintelLenghts.append(opnLenVal)
                opnLintelFormworkLenghts.append(opnLenVal)

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

            for value in range(opnTypes):
                opnValue = (
                    opnLengths[value] * opnWidths[value] * opnUnits[value])
                opnLintelValue = (
                    (opnLengths[value] + 0.45) * 0.23 * opnLintelUnits[value] * blockThickness)
                opnValues.append(opnValue)
                opnLintelFormworkValue = (
                    (opnLengths[value] + 0.45) * 0.23 * opnLintelUnits[value] * blockThickness)
                opnValues.append(opnValue)
                opnLintelValues.append(opnLintelValue)
                opnLintelFormworkValues.append(opnLintelFormworkValue)
                allopnValues = sum(opnValues)
                allOpnLintelValues = sum(opnLintelValues)
                allOpnLintelFormworkValues = sum(opnLintelFormworkValues)
                allopnValues = round(allopnValues, 2)
                allOpnLintelValues = round(opnLintelValues, 2)
                allopnLintelFormworkValues = round(allopnLintelFormworkValues)
        print("Total other openings value is %s" % allopnValues)
        return opnLintelValues, allOpnLintelValues, allopnLintelFormworkValues

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
        girthBIF = int(
            input('Enter the girth of blockwork in foundation: '))
        girthBAF = int(
            input("Enter girth for blockwork above foundation: "))
        print(girthBIF, girthBAF)
        return girthBIF, girthBAF

    def getWallThickness():
        wtIF = int(input("Enter the wall thickness in foundation: "))
        wtAF = int(input("Enter the wall thickness above foundation: "))
        spread = wtIF
        print(wtIF, wtAF, spread)
        return wtAF, wtAF, spread
