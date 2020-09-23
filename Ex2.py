userInput = input("Enter the mass in kg and force in N: ")
mass = float(userInput[:userInput.index(",")])
force = float(userInput[userInput.index(",")+1:])
acceleration = force/mass

print("The acceleration is", acceleration)
