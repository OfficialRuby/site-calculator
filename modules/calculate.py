from tools import Tools

# Tools.getWallThickness()


def siteClearance():
    bldLen = int(input(("Enter the length of the building: ")))
    bldWid = int(input("Enter the width of the building: "))
    siteClr = ((bldLen+2) * (bldWid+2))
    print(siteClr)
    return siteClr


spread = 23
girth = 0
thicknessOfBlock = 0
recess = 0


def topSoilExcavation():
    bldLen = int(input(("Enter the length of the building: ")))
    bldWid = int(input("Enter the width of the building: "))
    tsExcav = ((bldLen+(2*spread)) * (bldWid+(2*spread)))
    print(tsExcav)
    return tsExcav


topSoilExcavation()

# Top soil removal


def remOfTopSoilExcav():
    remOfTSE = tsExcav * 0.15
    return remOfTSE


# Trench Excavation
def trenchExcavation():
    widOfFdn = int(input("Enter the width of the foundation: "))
    depthOfFdn = int(input("Enter the depth of the foundation: "))
    trenchExcav = (girth * widOfFdn * depthOfFdn)
    return trenchExcav, depthOfFdn


# Leveling and compacting
def levAndCompacting():
    levAndComp = girth * widOfFdn
    print(levAndComp)
    return levAndComp

# Concrete Footing


def concFooting():
    widOfFdn = int(input("Enter the width of the foundation: "))
    ftThickness = int(input("Enter the thickness of the footing: "))
    concFT = girth * widOfFdn * ftThickness
    print(concFT)
    return concFT, ftThickness


# Blockwork in foundation
def blockWorkInFDN():
    blckWkHeight = int(input("Enter the height of blockwork in foundation: "))
    thicknessOfBlock = int(
        input("Enter the thickness of blockwork in foundation: "))
    blockWInFDN = girth * blckWkHeight * thicknessOfBlock
    expVal = girth * blckWkHeight  # Value to be exported
    print(blockWInFDN)
    return blockWInFDN, expVal

# Backfilling


def backfilling():
    blockWInFDN2 = girth * (depthOfFdn - ftThickness) * thicknessOfBlock
    remSurplusOffsite = blockWInFDN2 + concFT
    bckFilling = trenchExcav - remSurplusOffsite
    print(bckFilling)
    # Export remSurplusOffsite in Removal of Surplus Offsite
    return bckFilling, remSurplusOffsite


# Removal of surplus offsite
def remofSurpOffsite():
    remSurplusOffsite
    return remSurplusOffsite


# Laterite Earth Filling
def latEarthFilling():
    bldLen = int(input(("Enter the length of the building: ")))
    bldWid = int(input("Enter the width of the building: "))
    thicknessOfLatFillling = int(
        input("Enter the the thickness of laterite earth filling: "))
    areaOfBld = bldLen*bldWid
    peremOfWall = girth * thicknessOfBlock
    fillingArea = (areaOfBld - recess - peremOfWall)
    latEarthFill = fillingArea * thicknessOfLatFillling
    print(latEarthFill)
    return latEarthFill, fillingArea, areaOfBld, peremOfWall


# Hardcore filling
def hardcoreFilling():
    thicknessOfCoreFillling = int(
        input("Enter the thickness of hardcore filling: "))
    hardcoreFill = fillingArea * thicknessOfCoreFillling
    print(hardcoreFill)
    return hardcoreFill


# Floor reinforcement

def floorReinforcement():
    bldLen = int(input(("Enter the length of the building: ")))
    bldWid = int(input("Enter the width of the building: "))
    floorReinf = areaOfBld - recess
    print(floorReinf)
    return floorReinf


# Damp proof course

def dampProofCourse():
    PDC = peremOfWall
    print(peremOfWall)
    return peremOfWall


# Damp proof membrane
def dampProofMembrane():
    DPM = floorReinf
    print(DPM)
    return DPM

# Leveling and compacting on surface of filling


def surfaceLevelingAndCompacting():
    surfLvlAndComp = fillingArea
    print(surfLvlAndComp)
    return surfLvlAndComp


# Oversite concrete

def oversiteConcrete():
    floorThickness = int(input("Enter the floor thickness: "))
    oversiteConc = floorReinf * floorThickness
    print(oversiteConc)
    return oversiteConc

# Formwork for oversite concrete


def oversiteConcreteFormwork():
    bldVal = (bldLen * 2) + (bldWid * 2)
    oversiteConcFormwork = bldVal * floorThickness
    print(oversiteConcFormwork)
    return oversiteConcFormwork
