# Name: Elento Brent
# Date: June 9, 2026
# Program: Spreadsheet Automation Menu

from datetime import datetime

def main():
    studentId = "elebre6186"

    # First line output
    print(f"{studentId} Spreadsheet Automation Menu.")
    print()

    # Store menu options in a list
    menuOptions = [
        "Create a Spreadsheet",
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
        else:
            print("Error: Invalid choice selected.")
    else:
        print("Error: Invalid choice selected.")

# Call the main function
main()
