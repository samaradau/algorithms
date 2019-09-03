alphabeth = {
    "0": 0,
    "1": 22.5,
    "2": 45,
    "3": 67.5,
    "4": 90,
    "5": 112.5,
    "6": 135,
    "7": 157.5,
    "8": 180,
    "9": 202.5,
    "a": 225,
    "b": 247.5,
    "c": 270,
    "d": 292.5,
    "e": 315,
    "f": 337.5
}


def calculatePositions(message):
    res = []

    for letter in message:
        hexCode = format(ord(letter), "x")

        for hexChar in hexCode:
            res.append(alphabeth[f"{hexChar}"])

    return res


def turnCameraOn(positions):
    index = 1
    posCount = len(positions)
    delta = positions[0]

    while (index < posCount):
        print(delta)
        delta = positions[index] - positions[index - 1]
        index += 1


message = input("Type any message: ")
positions = calculatePositions(message)
turnCameraOn(positions)
