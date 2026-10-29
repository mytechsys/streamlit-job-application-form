import pandas as pd
import streamlit as st
from pathlib import Path

st.title("Job Application Form")

with st.form("job_application_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    mobile_no = st.text_input("Mobile Number")
    state = st.selectbox(
        "State",
        [
            "Andhra Pradesh",
            "Arunachal Pradesh",
            "Assam",
            "Bihar",
            "Chhattisgarh",
            "Goa",
            "Gujarat",
            "Haryana",
            "Himachal Pradesh",
            "Jharkhand",
            "Karnataka",
            "Kerala",
            "Madhya Pradesh",
            "Maharashtra",
            "Manipur",
            "Meghalaya",
            "Mizoram",
            "Nagaland",
            "Odisha",
            "Punjab",
            "Rajasthan",
            "Sikkim",
            "Tamil Nadu",
            "Telangana",
            "Tripura",
            "Uttar Pradesh",
            "Uttarakhand",
            "West Bengal"
        ]
    )

    submitted = st.form_submit_button("Submit Application")

if submitted:
    if not name or not email or not mobile_no:
        st.warning("Please fill in Name, Email, and Mobile Number.")
    else:
        data = {
            "Name": [name],
            "Email": [email],
            "Mobile No": [mobile_no],
            "State": [state]
        }

        csv_file = Path("job_applications.csv")

        if csv_file.exists():
            df = pd.read_csv(csv_file)
            df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
        else:
            df = pd.DataFrame(data)

        df.to_csv(csv_file, index=False)

        st.success("Application submitted successfully!")
        st.write("Submitted details:")
        st.dataframe(df.tail(1))
