def calculate_electricity_bill():
    print("Electricity Bill Calculator")
    house_number = input("Enter your house number: ")
    purpose = input("Enter the purpose (Domestic/Industrial): ").strip().lower()
    try:
        previous_units = float(input("Enter previous meter reading (units): "))
        present_units = float(input("Enter present meter reading (units): "))
    except ValueError:
        print("Invalid input for units. Please enter numeric values.")
        return

    if present_units < previous_units:
        print("Present units cannot be less than previous units.")
        return

    units_consumed = present_units - previous_units
    print(f"\nHouse Number: {house_number}")
    print(f"Purpose: {purpose.capitalize()}")
    print(f"Previous Units: {previous_units}")
    print(f"Present Units: {present_units}")
    print(f"Units Consumed: {units_consumed}")

    # Set rate per unit based on purpose
    if purpose == "domestic":
        rate = 5.0  # Example rate per unit for domestic
    elif purpose == "industrial":
        rate = 8.0  # Example rate per unit for industrial
    else:
        print("Invalid purpose entered. Please enter 'Domestic' or 'Industrial'.")
        return

    print(f"Rate per unit: {rate} INR")
    bill_amount = units_consumed * rate
    print(f"Total Bill Amount: {bill_amount} INR")

calculate_electricity_bill()
