# Name: Elento Brent
# Date: June 9, 2026
# Program: Spreadsheet Automation Menu

from datetime import datetime

def main():
    studentId = "elebre6186"

    # First line output
    print(f"{studentId} Spreadsheet Automation Menu.")
    print()

    # Menu options
    print("1. Create a Spreadsheet")
    print("2. Open a Spreadsheet")
    print("3. Edit Spreadsheet Data")
    print("4. Save Spreadsheet")
    print("5. Generate Report")
    print("6. Exit")
    print()

    # The next line retrieves the inputted option and stores into the variable called selectedOption.
    selectedOption = input("Please select an option (1-6): ")

    print()
    print(f"You selected option number {selectedOption}.")
    print("The time and date is", str(datetime.now()))

# Call the main function
main()