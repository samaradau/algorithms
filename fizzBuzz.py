def isFizzBuzz(number):
    fizz = number % 3 == 0
    buzz = number % 5 == 0

    res = ""

    if (fizz):
        res = "Fizz"
    elif (buzz):
        res += "Buzz"
    else:
        res = number

    print(res)


for number in range(1, 101):
    isFizzBuzz(number)
