def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    bmi = weight / height ** 2
    return bmi

def get_category(bmi):
    """Return BMI category based on value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=" * 40)
    print("       BMI CALCULATOR (Python)")
    print("=" * 40)

    # Get unit preference
    print("\nChoose unit system:")
    print("  1. Metric  (cm / kg)")
    print("  2. Imperial (ft, in / lbs)")
    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "2":
        # Imperial input
        feet = float(input("Enter height (feet): "))
        inches = float(input("Enter height (inches): "))
        weight_lbs = float(input("Enter weight (lbs): "))

        # Convert to metric
        total_inches = feet * 12 + inches
        height_m = total_inches * 0.0254
        weight_kg = weight_lbs * 0.453592
    else:
        # Metric input
        height_cm = float(input("Enter height (cm): "))
        weight_kg = float(input("Enter weight (kg): "))
        height_m = height_cm / 100

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)
    category = get_category(bmi)

    # Display result
    print("\n" + "=" * 40)
    print(f"  BMI Value  : {bmi:.2f}")
    print(f"  Category   : {category}")
    print("  Healthy BMI: 18.5 – 24.9")
    print("=" * 40)
    print("\n* BMI is a screening tool, not a diagnosis.")

if __name__ == "__main__":
    main()
