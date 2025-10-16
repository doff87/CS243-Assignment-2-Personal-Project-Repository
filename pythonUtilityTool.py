def measurementConverter():
    userOption = input("Please enter the number that corresponds to the measurement type you would like to convert: \n1. Weight\n2. Volume\n3. Distance\n4. Length").strip()
    
    match userOption:
        case 1:
            print("Weight Placeholder")
        case 2:
            print("Volume Placeholder")
        case 3:
            print("Distance Placeholder")
        case 4:
            print("Length Placeholder")
        case _:
            print("Invalid Choice")

def main():
    measurementConverter()
    

main()
        