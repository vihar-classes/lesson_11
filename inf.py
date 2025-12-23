total = 0
while True:
    user_input = input("Enter a number to add (or type 'exit' to stop): ")
    
    if user_input.lower() == 'exit':
        break
        
    total += int(user_input)
    print("Current total:", total)

print("Final total:", total)
