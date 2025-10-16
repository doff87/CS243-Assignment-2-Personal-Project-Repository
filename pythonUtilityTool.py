import time
from datetime import date
import pyfiglet as ascii

def measurementConverter():
    imperialOrMetric = 0
    
    while True:
        user_input = input("Please enter the number that corresponds to the measurement type you would like to convert: \n1. Mass\n2. Volume\n3. Length\n4. Quit\n").strip()
    
        userOption = is_int(user_input)

        if userOption is None:
            print("Invalid input. Please enter a number 1-5.")
            continue

        match userOption:
            case 1:
                imperialOrMetric = is_int(input("Please enter 1 if converting from imperial to metric, 2 if converting from metric to imperial, or enter 3 to return to menu: "))
                
                if imperialOrMetric not in (1,2,3):
                    print("Invalid choice. Please review options.")
                    continue
                
                if imperialOrMetric == 1:
                    while True:
                        user_input= input(("Please enter number of ounces to convert: ").strip())

                        numUnits = is_float(user_input)

                        if numUnits is None:
                            print("Invalid input. Please enter a float.")
                            continue
                        
                        print(f"{numUnits} ounces = {numUnits * 28.35} grams")
                        break

                elif imperialOrMetric == 2:
                    while True:
                        user_input= input(("Please enter number of grams to convert: ").strip())

                        numUnits = is_float(user_input)

                        if numUnits is None:
                            print("Invalid input. Please enter a float.")
                            continue
                        
                        print(f"{numUnits} grams = {numUnits/28.35} ounces")
                        break

                elif imperialOrMetric == 3:
                    break

            case 2:
                imperialOrMetric = is_int(input("Please enter 1 if converting from imperial to metric, 2 if converting from metric to imperial, or enter 3 to return to menu: "))
                
                if imperialOrMetric not in (1,2,3):
                    print("Invalid choice. Please review options.")
                    continue
                
                if imperialOrMetric == 1:
                    while True:
                        user_input= input(("Please enter number of fluid ounces to convert: ").strip())

                        numUnits = is_float(user_input)

                        if numUnits is None:
                            print("Invalid input. Please enter a float.")
                            continue
                        
                        print(f"{numUnits} fluid ounces = {numUnits * 29.57} mililiters")
                        break

                elif imperialOrMetric == 2:
                    while True:
                        user_input= input(("Please enter number of mililiters to convert: ").strip())

                        numUnits = is_float(user_input)

                        if numUnits is None:
                            print("Invalid input. Please enter a float.")
                            continue
                        
                        print(f"{numUnits} mililiters = {numUnits/29.57} fluid ounces")
                        break

                elif imperialOrMetric == 3:
                    return
                
            case 3:
                imperialOrMetric = is_int(input("Please enter 1 if converting from imperial to metric, 2 if converting from metric to imperial, or enter 3 to return to menu: "))
                
                if imperialOrMetric not in (1,2,3):
                    print("Invalid choice. Please review options.")
                    continue
                
                if imperialOrMetric == 1:
                    while True:
                        user_input= input(("Please enter number of inches to convert: ").strip())

                        numUnits = is_float(user_input)

                        if numUnits is None:
                            print("Invalid input. Please enter a float.")
                            continue
                        
                        print(f"{numUnits} inches = {numUnits * 2.54} centimeters")
                        break

                elif imperialOrMetric == 2:
                    while True:
                        user_input= input(("Please enter number of centimeters to convert: ").strip())

                        numUnits = is_float(user_input)

                        if numUnits is None:
                            print("Invalid input. Please enter a float.")
                            continue
                        
                        print(f"{numUnits} centimeters = {numUnits/2.54} inches")
                        break

                elif imperialOrMetric == 3:
                    break

            case 4:
                return

            case _:
                print("Invalid Choice")

def clock():


def is_int(userInput):
    try:
        return int(userInput)
    except ValueError:
        return None
    
def is_float(userInput):
    try:
        return float(userInput)
    except ValueError:
        return None

def main():
    while True:
        user_input = input("Please enter the number that corresponds to the function you would like to utilize: 1. Measurement Converter\n2. Clock\n3. Dice Roll").strip()
    
        userOption = is_int(user_input)

        match userOption:

            case 1:
                measurementConverter()
            
            case 2:


main()
        