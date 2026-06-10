# Name: Elento Brent
# Date: June 9, 2026
# Program: Spreadsheet Automation Menu

from datetime import datetime

# This function converts rainfall from inches to centimeters.
def convertData(data):
    convertedValue = data * 2.54
    return convertedValue


# This function writes comma-separated data to a CSV file.
def insertData(filePath, dataString):

    try:
        with open(filePath, "a") as csvFile:
            csvFile.write(dataString + "\n")
        return True

    except Exception as error:
        print("Error writing to file:", error)
        return False


# This function reads and displays the contents of a CSV file.
def viewData(filePath):

    try:
        print(f"\nReading data from: {filePath}\n")

        with open(filePath, "r") as csvFile:
            contents = csvFile.read()

            if contents:
                print(contents)
            else:
                print("The file is empty.")

    except Exception as error:
        print("Error reading file:", error)


# This function collects rainfall data from the user and stores it in a CSV file.
def getInput():

    filePath = "ZooData.csv"

    try:
        numberOfEntries = int(input("How many entries are being entered? "))

        for entry in range(numberOfEntries):

            entryDate = input("Enter the date: ")
            rainInches = float(input("Enter rainfall amount in inches: "))

            # Calling convertData(data) where data is the rainfall amount in inches.
            # Expected return value: rainfall converted from inches to centimeters.
            convertedRain = convertData(rainInches)

            csvData = f"{entryDate},{rainInches},{convertedRain:.2f}"

            insertSuccessful = insertData(filePath, csvData)

            if insertSuccessful:
                print(
                    f"\nThe following data was saved at {datetime.now()}: {csvData}\n"
                )

    except Exception as error:
        print("Error processing input:", error)


def main():

    studentId = "elebre6186"

    print(f"{studentId} Spreadsheet Automation Menu.")
    print()

    menuOptions = [
        "Rainfall Spreadsheet",
        "View Stored Data",
        "Edit Spreadsheet Data",
        "Save Spreadsheet",
        "Generate Report",
        "Exit"
    ]

    for optionNumber, optionName in enumerate(menuOptions, start=1):
        print(f"{optionNumber}. {optionName}")

    print()

    # The next line retrieves the inputted option and stores into the variable called selectedOption.
    selectedOption = input("Please select an option (1-6): ")

    print()

    if selectedOption.isdigit():

        selectedOption = int(selectedOption)

        if 1 <= selectedOption <= len(menuOptions):

            print(f"You selected option number {selectedOption}.")
            print("The time and date is", str(datetime.now()))

            if selectedOption == 1:
                getInput()

            elif selectedOption == 2:
                viewData("ZooData.csv")

            else:
                print("Error: The chosen functionality is not implemented yet")

        else:
            print("Error: Invalid choice selected.")

    else:
        print("Error: Invalid choice selected.")


# Start the application
main()
