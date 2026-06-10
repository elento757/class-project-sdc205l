# Name: Elento Brent
# Date: June 9, 2026
# Program: Spreadsheet Automation Menu

from datetime import datetime

# Function to convert rainfall from inches to centimeters
def convertData(data):
    convertedValue = data * 2.54
    return convertedValue

# Function to collect user input and process entries
def getInput():

    numberOfEntries = int(input("How many entries are being entered? "))

    for entry in range(numberOfEntries):

        entryDate = input("Enter the date: ")
        rainInches = float(input("Enter rainfall amount in inches: "))

        # Calling convertData(data) where data is the rainfall amount in inches.
        # Expected return value: rainfall converted from inches to centimeters.
        convertedRain = convertData(rainInches)

        print()
        print(f"The following was saved at {datetime.now()}:")
        print(f"Date: {entryDate}")
        print(f"Rainfall (in): {rainInches}")
        print(f"Rainfall (cm): {convertedRain:.2f}")
        print()

def main():

    studentId = "elebre6186"

    # First line output
    print(f"{studentId} Spreadsheet Automation Menu.")
    print()

    # Store menu options in a list
    menuOptions = [
        "Rainfall Spreadsheet",
        "Open a Spreadsheet",
        "Edit Spreadsheet Data",
        "Save Spreadsheet",
        "Generate Report",
        "Exit"
    ]

    # Display menu using a for-loop
    for optionNumber, optionName in enumerate(menuOptions, start=1):
        print(f"{optionNumber}. {optionName}")

    print()

    # The next line retrieves the inputted option and stores into the variable called selectedOption.
    selectedOption = input("Please select an option (1-6): ")

    print()

    # Validate the user's choice
    if selectedOption.isdigit():

        selectedOption = int(selectedOption)

        if 1 <= selectedOption <= len(menuOptions):

            print(f"You selected option number {selectedOption}.")
            print("The time and date is", str(datetime.now()))

            if selectedOption == 1:
                getInput()
            else:
                print("Error: The chosen functionality is not implemented yet")

        else:
            print("Error: Invalid choice selected.")

    else:
        print("Error: Invalid choice selected.")

# Start the program
main()
