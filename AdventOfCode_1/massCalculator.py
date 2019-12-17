import math

totalFuel = 0

fp = input("Pass the file path towards the Input file: ")
try:
    fr = open(fp, 'r')
    line = fr.readline()
    while line:
        inputMass = int(line)
        totalFuel += math.trunc(inputMass / 3) - 2
        line = fr.readline()
except: #if something goes wrong we try to read the file path again
    print("Specified file pth is not correct")
    fp = input("Pass the file path towards the Input file: ")
else: #if everything goes smooth we close the file reader and print the result
    fr.close()
    print(totalFuel)
