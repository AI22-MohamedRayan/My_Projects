import streamlit as st
import pandas as pd

def process_data(df):
    try:
        df['date'] = df['date'].astype(str)
        df['time'] = df['time'].astype(str)
        
        st.write("Data types after conversion:")
        st.write(df.dtypes)
        
        df['Timestamp'] = pd.to_datetime(df['date'] + ' ' + df['time'], errors='coerce')
        df['Duration'] = pd.to_timedelta(df['sensor'], unit='s')
        df['Activity'] = df['position'].str.lower()
        df['ActivityType'] = df['activity'].str.lower()
        df['Date'] = df['Timestamp'].dt.date

        duration_data = df.groupby(['Date', 'Activity'])['Duration'].sum().unstack(fill_value=pd.Timedelta(seconds=0))
        activity_count = df.groupby(['Date', 'ActivityType']).size().unstack(fill_value=0)

        return duration_data, activity_count
    except Exception as e:
        st.error(f"Error processing data: {e}")
        return None, None

def load_raw_data(file):
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

st.title('Activity Analysis Dashboard')

st.write("Upload your raw data file (Excel):")
uploaded_file = st.file_uploader("", type="xlsx")

if uploaded_file is not None:
    df = load_raw_data(uploaded_file)
    
    if df is not None:
        st.write("### Raw Data Preview")
        st.write(df.head())
        
        required_columns = ['date', 'time', 'sensor', 'activity', 'position']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if not missing_columns:
            duration_data, activity_count = process_data(df)
            if duration_data is not None and activity_count is not None:
                st.write("### Datewise Total Duration for Inside and Outside")
                st.dataframe(duration_data)

                st.write("### Datewise Number of Picking and Placing Activity")
                st.dataframe(activity_count)

                st.write("### Plotting the results")

                st.write("#### Duration Plot")
                st.line_chart(duration_data)

                st.write("#### Activity Count Plot")
                st.bar_chart(activity_count)
        else:
            st.error(f"The uploaded file is missing the following required columns: {missing_columns}")
else:
    st.write("Please upload an Excel file to see the results.")
