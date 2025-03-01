import streamlit as st
from datetime import datetime
import pytz
import geocoder

def main():
    """The main application"""

    st.title("Airport Arrival Time Predictor")
    st.markdown("""Do you regularly pick up friends or family from the airport? 
                Use this tool to predict their arrival time!""")
    
    # User inputs
    airline = st.text_input("Enter your airline")
    airport = st.text_input("Enter the airport you're arriving at")
    arrival_time = st.time_input("Enter your arrival time (HH:MM)")

    current_time = datetime.now(pytz.timezone('UTC'))

    g = geocoder.ip('me')
    location = g.latlng

    if location:
        st.write(f"Your current location: {location}")
    else:
        st.error("Could not retrieve your location. Please enter it manually.")
        location = st.text_input("Enter your current location (latitude, longitude)")
        
    if st.button("Predict Departure Time"):
        if airline and airport and arrival_time and location:
            # Call a function to predict departure time (to be implemented in utils.py)
            departure_time = predict_departure_time(current_time, arrival_time, location)
            st.success(f"You should leave at {departure_time} to arrive at the airport on time.")
        else:
            st.error("Please fill in all the fields.")

    def predict_departure_time(current_time, arrival_time, location):
        # Placeholder function for predicting departure time
        # This function should be implemented in utils.py and imported here
        return "TBD"

if __name__ == "__main__":
    main()