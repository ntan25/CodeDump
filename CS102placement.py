import statistics


def printResults(avgNights,
                 mostUsedFloor,
                 numInvalidRoomNumbers,
                 numNegativeNights):
    print("Average nights per reservation: " + str(avgNights));
    print("Floor with most reservations: " + str(mostUsedFloor));
    print("Invalid room numbers: " + str(numInvalidRoomNumbers));
    print("Number of negative nights: " + str(numNegativeNights));


def main():
    # Add your code here to declare data values, read the input,
    # and compute the desired answers.

    numInputs = 0
    totalNights = 0
    numInvalidRoomNumbers = 0
    numNegativeNights = 0
    floorList = []
    codeList = []

    def isValidInput(roomCode, duration):
        if roomCode >= 100 and roomCode <= 3099 and duration >= 0:
            return True
        else:
            return False

    code = str(input('Enter code: '))

    if code == '0 0':
        totalNights = 0
        numInputs = 1
        maxFloor = 0
        numInvalidRoomNumbers = 0
        numNegativeNights

    while code != '0 0':
        codeList.append(code)

        code = str(input('Enter code: '))

    for i in codeList:

        a = i.split()

        roomInfo = a[0]
        durationInfo = a[1]

        roomInfo = int(roomInfo)
        durationInfo = int(durationInfo)

        if isValidInput(roomInfo, durationInfo):

            numInputs += 1

            floorNum = roomInfo // 100
            floorList.append(floorNum)

            totalNights += durationInfo

        else:

            if roomInfo < 100 or roomInfo > 3099:
                numInvalidRoomNumbers += 1

            if durationInfo < 0:
                numNegativeNights += 1

    maxFloor = statistics.mode(floorList)

    # call printResults before exiting and pass it your answers
    printResults(totalNights / numInputs, maxFloor, numInvalidRoomNumbers, numNegativeNights)


if __name__ == "__main__":
    main()