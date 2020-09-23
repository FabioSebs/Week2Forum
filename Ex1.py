height = input("Please enter height in Feet followed by Inches Ex) 5'7 : ")
feet = int(height[0])
inches = int(height[len(height)-1])
centimeters = 0.0

def cm(feet, inches):
    cm = feet * 30.48
    cm = cm + (inches * 2.54)
    return cm


print("Feet:", feet , "\nInches:", inches , "\nSuggested board length",
      cm(feet, inches))
