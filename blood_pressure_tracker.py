import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# File where the data is stored
FILE_NAME = 'blood_pressure_data.csv'

# Function to categorize blood pressure
def categorize_bp(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "Hypertension Stage 1"
    elif systolic >= 140 or diastolic >= 90:
        return "Hypertension Stage 2"
    else:
        return "Hypertensive Crisis"

# Function to validate user input
def validate_input(prompt, lower_limit, upper_limit):
    while True:
        try:
            value = float(input(prompt))
            if lower_limit <= value <= upper_limit:
                return value
            else:
                print(f"Please enter a value between {lower_limit} and {upper_limit}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to add a reading interactively
def add_reading():
    systolic = validate_input("Enter systolic pressure (in mmHg): ", 70, 250)
    diastolic = validate_input("Enter diastolic pressure (in mmHg): ", 40, 150)
    pulse = validate_input("Enter pulse rate: ", 40, 180)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = categorize_bp(systolic, diastolic)
    
    new_entry = {'Timestamp': timestamp, 'Systolic': systolic, 'Diastolic': diastolic, 'Pulse': pulse, 'Category': category}
    print(f"Added: {systolic}/{diastolic}, Pulse: {pulse}, Category: {category}")
    
    # Append the new data to the DataFrame and save
    save_data(new_entry)

# Function to save the data to a CSV file
def save_data(new_entry):
    try:
        # Load existing data if the file exists, otherwise create a new DataFrame
        df = pd.read_csv(FILE_NAME)
        new_entry_df = pd.DataFrame([new_entry])  # Convert new entry to DataFrame
        df = pd.concat([df, new_entry_df], ignore_index=True)  # Use pd.concat instead of append
    except FileNotFoundError:
        # Create a new DataFrame if the file does not exist
        df = pd.DataFrame([new_entry])
    
    # Save back to CSV
    df.to_csv(FILE_NAME, index=False)
    print(f"Data saved to {FILE_NAME}")

# Function to load and display data
def load_data():
    try:
        df = pd.read_csv(FILE_NAME)
        print(df)
    except FileNotFoundError:
        print(f"No data found in {FILE_NAME}. Please add some readings first.")

# Function to plot blood pressure trends
def plot_data():
    try:
        df = pd.read_csv(FILE_NAME)
        
        plt.plot(df['Timestamp'], df['Systolic'], label='Systolic Pressure', marker='o')
        plt.plot(df['Timestamp'], df['Diastolic'], label='Diastolic Pressure', marker='o')
        
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Timestamp')
        plt.ylabel('Blood Pressure (mmHg)')
        plt.title('Blood Pressure Trends Over Time')
        plt.legend()
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print(f"No data found in {FILE_NAME}. Please add some readings first.")

# Main menu for the blood pressure tracker
def main_menu():
    while True:
        print("\nBlood Pressure Tracker Menu")
        print("1. Add a new reading")
        print("2. View saved readings")
        print("3. Plot blood pressure trends")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_reading()
        elif choice == '2':
            load_data()
        elif choice == '3':
            plot_data()
        elif choice == '4':
            print("Exiting the program. Stay healthy!")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the main menu
if __name__ == '__main__':
    main_menu()
