# Blood Pressure Tracker
The Blood Pressure Tracker is a simple command-line application designed to help individuals monitor and manage their blood pressure levels over time. Blood pressure is a critical indicator of cardiovascular health and is directly linked to heart disease risk. This application allows users to log their blood pressure readings, view saved entries, and plot trends for better insights into their heart health.

## Features
- **Add New Readings**: Users can input their systolic and diastolic blood pressure values along with pulse rate.
- **View Saved Readings**: View a list of all saved blood pressure readings, including timestamp, systolic, diastolic, pulse, and category.
- **Plot Blood Pressure Trends**: Visualize blood pressure readings over time to track trends and changes.
- **Category Classification**: Automatically categorize blood pressure readings according to established health standards.

## Requirements
- Python 3.x
- Pandas
- Matplotlib

## Installation
1. Clone the repository:
  -  ```git clone https://github.com/yourusername/blood-pressure-tracker.git ```
  - ``` cd blood-pressure-tracker ```
2. Install the required libraries:
- ```pip install pandas matplotlib ```

## Usage
1. Run the application:
- ```python blood_pressure_tracker.py```
2. Follow the on-screen menu to:
- Add a new reading
- View saved readings
- Plot blood pressure trends
- Exit the application

## Data Storage
Blood pressure readings are saved in a CSV file named blood_pressure_data.csv. The file contains the following columns:
- Timestamp: The date and time when the reading was recorded.
- Systolic: The systolic pressure (top number).
- Diastolic: The diastolic pressure (bottom number).
- Pulse: The pulse rate.
- Category: The classification of the blood pressure reading.
   
## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to create a pull request.
