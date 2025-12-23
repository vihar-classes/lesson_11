number = int(input('Numbner: '))
result = ""

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

while number > 0:
    digit = number % 10
    result = words[digit] + result
    number //= 10

print(result)
