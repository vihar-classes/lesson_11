n = input("Enter a 4-digit number: ")

while n != "6174":
    digits = list(n)
    
    # Sort descending
    i = 0
    while i < len(digits):
        j = i + 1
        while j < len(digits):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]
            j += 1
        i += 1
    desc = int("".join(digits))
    
    # Sort ascending
    i = 0
    while i < len(digits):
        j = i + 1
        while j < len(digits):
            if digits[i] > digits[j]:
                digits[i], digits[j] = digits[j], digits[i]
            j += 1
        i += 1
    asc = int("".join(digits))
    
    res = desc - asc
    print(f"{desc} - {asc} = {res}")
    
    n = str(res)
    while len(n) < 4:
        n = "0" + n
