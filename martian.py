import codecs

# 0 1 2 3 4 5 6 7 8 9 A B C D E F

# 360 / 16 = 22.5

digits = {
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


def getPositions(msg):
    res = []

    for letter in msg:
        hexCode = format(ord(letter), "x")

        for hexChar in hexCode:
            res.append(digits[f"{hexChar}"])

    return res


def turnCamera(positions):
    index = 1
    posCount = len(positions)
    deviation = positions[0]

    while (index < posCount):
        print(deviation)
        deviation = positions[index] - positions[index - 1]
        index += 1


msg = input("Type any message: ")
positions = getPositions(msg)
turnCamera(positions)