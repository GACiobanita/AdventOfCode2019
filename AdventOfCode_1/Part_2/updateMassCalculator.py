import math

totalFuelNeeded = 0

fp = input("Pass the file path towards the Input file: ")
try:
    fr = open(fp, 'r')
    line = fr.readline()
    while line:
        inputMass = int(line)
        fuelForMass = math.trunc(inputMass / 3) - 2
        while fuelForMass > 0:  # we assume that all module mass in the input file will not return 0 from the first calculation
            totalFuelNeeded += fuelForMass # and add it
            fuelForMass = math.trunc(fuelForMass / 3) - 2 # calculate new fuel quantity for the new mass
        line = fr.readline()
except:
    print("Specified file pth is not correct")
    fp = input("Pass the file path towards the Input file: ")
else:
    fr.close()
    print(totalFuelNeeded)
