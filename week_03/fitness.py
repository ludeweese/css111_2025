#week 3 Team Assignment

# Import datetime for age computation.
from datetime import datetime

def main():
    """Gets user input, calculates metrics using functions, and prints results."""
    # Get user input
    gender = input("Please enter your gender (M or F): ").strip().upper()
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()
    try:
        pounds = float(input("Enter your weight in U.S. pounds: "))
        inches = float(input("Enter your height in U.S. inches: "))
    except ValueError:
        print("Invalid number input. Exiting.")
        return

    # Calculate metrics
    age = compute_age(birth_str)
    weight_kg = kg_from_lb(pounds)
    height_cm = cm_from_in(inches)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    # Print results
    print("\n--- Results ---")
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_kg:.2f}") #:.2f or :.1f formats the numbers (2 decimals, 1 decimal, etc.).
    print(f"Height (cm): {height_cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

    # Stretch Challenge: Converts Height in meters and BMI category
    print(f"\nStretch: Height in meters: {height_cm / 100:.2f} m")
    print(f"Stretch: BMI category: {classify_bmi(bmi)}")

# Core Functions 

def compute_age(birth_str):
    """Compute and return a person's age in years."""
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    # Subtract one if birthday hasn't occurred this year
    if birthdate.month > today.month or \
       (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years

def kg_from_lb(pounds):
    """Convert a mass from pounds to kilograms (1 lb = 0.45359237 kg)."""
    return pounds * 0.45359237

def cm_from_in(inches):
    """Convert a length from inches to centimeters (1 in = 2.54 cm)."""
    return inches * 2.54

def body_mass_index(weight, height):
    """Compute and return BMI: bmi = (10,000 * kg) / cm^2."""
    if height <= 0: return 0
    return (10000 * weight) / (height ** 2)

def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return BMR using gender-specific Harris-Benedict formulas."""
    if gender == 'F':
        # Women: 447.593 + 9.247w + 3.098h − 4.330a
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    elif gender == 'M':
        # Men: 88.362 + 13.397w + 4.799h − 5.677a
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        print("Warning: Invalid gender. BMR set to 0.")
        bmr = 0
    return bmr

# Stretch Function 
def classify_bmi(bmi):
    """Return BMI category."""
    if bmi < 18.5: return "Underweight 🥦"
    if bmi < 25: return "Normal ✅"
    if bmi < 30: return "Overweight ⚠️"
    return "Obese 🚨"

# Call main function to start program
if __name__ == "__main__":
    main()