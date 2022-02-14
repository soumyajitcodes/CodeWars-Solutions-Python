def high_and_low(numbers):
    # ...
    numbers = numbers.split(" ")
    numList = [int(i) for i in numbers]
    return f"{max(numList)} {min(numList)}"
