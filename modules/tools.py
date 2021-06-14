class Tools:

    def getWindowsValue():
        windowTypes = input("How many type of windows is used: ")
        windowLengths = []
        windowWidths = []
        windowUnits = []
        windowsValues = []
        windowTypes = int(windowTypes)
        answer = 0
        for i in range(1):
            # Loop through to collect the lenght values
            for winLen in range(windowTypes):
                winLenVal = int(input(
                    "Enter the lenght for window type %s : " % (winLen+1)))
                windowLengths.append((winLenVal))

            for winWid in range(windowTypes):
                winWidVal = int(input(
                    "Enter the width for window type %s : " % (winWid+1)))
                windowWidths.append(winWidVal)

            for winUnit in range(windowTypes):
                winUnitVal = int(input(
                    "How many unit of window type %s : " % (winUnit+1)))
                windowUnits.append(winUnitVal)

            for value in range(windowTypes):
                windowsValue = (
                    windowLengths[value] * windowWidths[value] * windowUnits[value])
                windowsValues.append(windowsValue)
        answer = sum(windowsValues)
        print("Total window(s) value is %s" % answer)
        return answer

    def getDoorsValue():
        doorTypes = input("How many type of door is used: ")
        doorLengths = []
        doorWidths = []
        doorUnits = []
        doorValues = []
        doorTypes = int(doorTypes)
        answer = 0
        for i in range(1):
            # Loop through to collect the lenght values
            for doorLen in range(doorTypes):
                doorLenVal = int(input(
                    "Enter the lenght for door type %s : " % (doorLen+1)))
                doorLengths.append((doorLenVal))

            for doorWid in range(doorTypes):
                doorWidVal = int(input(
                    "Enter the width for door type %s : " % (doorWid+1)))
                doorWidths.append(doorWidVal)

            for doorUnit in range(doorTypes):
                doorUnitVal = int(input(
                    "How many unit of door type %s : " % (doorUnit+1)))
                doorUnits.append(doorUnitVal)

            for value in range(doorTypes):
                doorValue = (
                    doorLengths[value] * doorWidths[value] * doorUnits[value])
                doorValues.append(doorValue)
        answer = sum(doorValues)
        print("Total window(s) value is %s" % answer)
        return answer

    def getOtherOpeningsValue():
        opnTypes = input("How many type opening is present: ")
        opnLengths = []
        opnWidths = []
        opnUnits = []
        opnValues = []
        opnTypes = int(opnTypes)
        answer = 0
        for i in range(1):
            # Loop through to collect the lenght values
            for opnLen in range(opnTypes):
                opnLenVal = int(input(
                    "Enter the lenght for opening type %s : " % (opnLen+1)))
                opnLengths.append((opnLenVal))

            for opnWid in range(opnTypes):
                opnWidVal = int(input(
                    "Enter the width for opening type %s : " % (opnWid+1)))
                opnWidths.append(opnWidVal)

            for opnUnit in range(opnTypes):
                opnUnitVal = int(input(
                    "How many unit of opening type %s : " % (opnUnit+1)))
                opnUnits.append(opnUnitVal)

            for value in range(opnTypes):
                opnValue = (
                    opnLengths[value] * opnWidths[value] * opnUnits[value])
                opnValues.append(opnValue)
        answer = sum(opnValues)
        print("Total window(s) value is %s" % answer)
        return answer

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
