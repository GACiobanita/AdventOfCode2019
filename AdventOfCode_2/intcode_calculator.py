fp = input("Pass the file path towards the IntCode program: ")

try:
    fr = open(fp, 'r')
    intCodeLine = [int(code) for code in fr.readline().split(',')]
    # get a list containing each intcode variable to a list location
    # did this to have coordinates from the start
    print(len(intCodeLine))
    currentPosition = 0
    currentCode = intCodeLine[currentPosition]
    while currentCode is not 99:
        addition = 0
        multiplication = 0
        if currentCode is 1:
            addition = intCodeLine[intCodeLine[currentPosition + 1]] + intCodeLine[intCodeLine[currentPosition + 2]]
            additionPosition = intCodeLine[currentPosition + 3]
            intCodeLine[additionPosition] = addition
        elif currentCode is 2:
            multiplication = intCodeLine[intCodeLine[currentPosition + 1]] * intCodeLine[
                intCodeLine[currentPosition + 2]]
            multiplicationPosition = intCodeLine[currentPosition + 3]
            intCodeLine[multiplicationPosition] = multiplication
        currentPosition += 4
        currentCode = intCodeLine[currentPosition]
except IOError:
    print('An error occurred trying to read the file.')
except ValueError:
    print('Non-numeric data found in the file.')
except ImportError:
    print
    "NO module found"
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    fr.close()
    print(intCodeLine)
