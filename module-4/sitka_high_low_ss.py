# Sebastian Siqueiros  Module 4 Assignment April 20, 2026
# Modified program to allow user to select highs, lows, or exit


import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

filename = 'sitka_weather_2018_simple.csv'

dates = []
highs = []
lows = []

# Read data from CSV
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            continue

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Added menu loop so user can choose what data to view

while True:
    print("\nMenu:")
    print("1 - View High Temperatures")
    print("2 - View Low Temperatures")
    print("3 - Exit")
# Prompt user for menu selection
    choice = input("Enter choice: ")
# Display and save high temperature graph in red and changed from plt.show() to save image
    if choice == '1':
        plt.figure()
        plt.plot(dates, highs, color='red')
        plt.title("Daily High Temperatures")
        plt.xlabel("Date")
        plt.ylabel("Temperature (F)")
        plt.savefig("highs.png")
        print("Highs graph saved as highs.png")
# Display and save low temperature graph in blue changed from plt.show() to save image
    elif choice == '2':
        plt.figure()
        plt.plot(dates, lows, color='blue')
        plt.title("Daily Low Temperatures")
        plt.xlabel("Date")
        plt.ylabel("Temperature (F)")
        plt.savefig("lows.png")
        print("Lows graph saved as lows.png")
# Exit program when user selects option 3
    elif choice == '3':
        print("Exiting program. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice, try again.")
# Changed from plt.show() to plt.savefig() due to Chromebook display limitations
