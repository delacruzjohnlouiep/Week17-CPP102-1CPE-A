#PROJECT
def classify_reading(temperature):
    if temperature < 30:
        return "NORMAL"
    elif temperature <= 35:
        return "WARNING"
    else:
        return "CRITICAL"

def view_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")

    for i in range(len(readings)):
        print(f"Reading {i + 1}: {readings[i]} °C")

def add_reading(readings):
    user_input = input("Enter new reading: ")

    if user_input == "":
        print("\nInvalid input. The reading cannot be empty.")
        return

    try:
        temperature = int(user_input)
    except ValueError:
        print("\nInvalid input. Enter a whole number only.")
        return

    if temperature < 0 or temperature > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
    else:
        readings.append(temperature)
        print("\nReading added successfully.")

def classify_readings(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for temperature in readings:
        category = classify_reading(temperature)
        print(f"{temperature} °C -> {category}")

def generate_summary(readings):
    number = len(readings)

    if number == 0:
        print("\nNo readings available.")
        return

    total = 0
    minimum = readings[0]
    maximum = readings[0]

    normal_count = 0
    warning_count = 0
    critical_count = 0

    for temperature in readings:
        total += temperature

        if temperature < minimum:
            minimum = temperature

        if temperature > maximum:
            maximum = temperature

        category = classify_reading(temperature)

        if category == "NORMAL":
            normal_count += 1
        elif category == "WARNING":
            warning_count += 1
        else:
            critical_count += 1

    average = total / number

    normal_percent = normal_count / number * 100
    warning_percent = warning_count / number * 100
    critical_percent = critical_count / number * 100

    if critical_count >= 1:
        status = "ATTENTION REQUIRED"
    elif warning_count >= 1:
        status = "MONITOR"
    else:
        status = "NORMAL"

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")

    print()
    print(f"NORMAL   : {normal_count} ({normal_percent:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percent:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percent:.2f}%)")

    print(f"\nOverall Status: {status}")

def display_menu():
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")

def main():
    readings = [28, 31, 35, 37, 29]

    choice = ""

    while choice != "5":
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            view_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            classify_readings(readings)
        elif choice == "4":
            generate_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

main()
