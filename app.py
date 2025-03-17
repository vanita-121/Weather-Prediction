import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib  # Use joblib for loading .joblib files

# Load your trained model using joblib (adjust if necessary)
try:
    model = joblib.load('weather_model.joblib')  # Make sure the path is correct
except FileNotFoundError:
    messagebox.showerror("File Not Found", "The model file could not be found. Please check the path.")
    exit()

# Dummy weather prediction logic (replace with your model's prediction logic)
def predict_weather(temp, humidity, wind_speed, pressure):
    try:
        # Using the model for prediction (assuming the model takes 4 features as input)
        input_features = np.array([[temp, humidity, wind_speed, pressure]])  # 4 features expected by the model
        prediction = model.predict(input_features)  # Get prediction
        
        # If the model predicts a category like "Rainy" or "Sunny"
        if isinstance(prediction, np.ndarray):
            prediction = prediction[0]  # Extract the value from the array
        
        # Now prediction should be a string ("Rainy" or "Sunny")
        return prediction
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Prediction error"

def on_predict_button_click():
    try:
        # Get input values
        temp_input = temp_entry.get()
        humidity_input = humidity_entry.get()
        wind_speed_input = wind_speed_entry.get()
        pressure_input = pressure_entry.get()

        # Check if inputs are valid numbers
        if not temp_input.replace('.', '', 1).isdigit() or not humidity_input.replace('.', '', 1).isdigit() or \
           not wind_speed_input.replace('.', '', 1).isdigit() or not pressure_input.replace('.', '', 1).isdigit():
            raise ValueError("Invalid input. Please enter valid numeric values for all fields.")

        # Convert inputs to float
        temp = float(temp_input)
        humidity = float(humidity_input)
        wind_speed = float(wind_speed_input)
        pressure = float(pressure_input)
        
        # Call the prediction function
        weather = predict_weather(temp, humidity, wind_speed, pressure)
        
        # Display the result
        result_label.config(text=f"Predicted Weather: {weather}")
        
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))  # Display the error message to the user
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Tkinter UI
root = tk.Tk()
root.title("Weather Prediction")

# Labels and input fields for 4 features
tk.Label(root, text="Enter Temperature (°C):").pack(pady=5)
temp_entry = tk.Entry(root)
temp_entry.pack(pady=5)

tk.Label(root, text="Enter Humidity (%):").pack(pady=5)
humidity_entry = tk.Entry(root)
humidity_entry.pack(pady=5)

tk.Label(root, text="Enter Wind Speed (m/s):").pack(pady=5)
wind_speed_entry = tk.Entry(root)
wind_speed_entry.pack(pady=5)

tk.Label(root, text="Enter Pressure (hPa):").pack(pady=5)
pressure_entry = tk.Entry(root)
pressure_entry.pack(pady=5)

# Button to make the prediction
predict_button = tk.Button(root, text="Predict Weather", command=on_predict_button_click)
predict_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="Predicted Weather: ", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the app
root.mainloop()
