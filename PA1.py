
"""  Leo Quezada
     Program #1: The area calculator
     COSC 1306
     Spring 2021
     Calculate a figure's area based on the user's input.
"""
#shows user the menu
print("Select a figure from the menu:")
print("1 - Square")
print("2 - Rectangle")
print("3 - Triangle")

#ask user for their shape choice
figureType = int(input("Enter your selection:"))

if figureType == 1: #asking for square side length
    side = int(input("Enter the side length:"))
    square = side*side
    print("The area of the selected figure is: " + "%.2f" %square)

elif figureType == 2: #asking for rectangle length/width
    length = int(input("Enter the length of the rectangle:"))
    width = int(input("Enter the width of the rectangle:"))
    rectangle = length * width
    print("The area of the selected figure is: " + "%.2f" %rectangle)


elif figureType == 3: #asking for triangle base/height
    base = int(input("Enter the base of the triangle:"))
    height = int(input("Enter the height of the triangle:"))
    triangle = (base * height)/2
    print("The area of the selected figure is: " + "%.2f" %triangle)

else:
    print("Invalid option")

#final output
#print("The area of the selected figure is: " + "%.2f" %variable_name)










