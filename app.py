import sqlite3
from pathlib import Path
import streamlit as st

DB_PATH = Path("job_applications.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile_no TEXT NOT NULL,
            state TEXT NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def save_application(name, email, mobile_no, state):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO applications (name, email, mobile_no, state) VALUES (?, ?, ?, ?)",
        (name, email, mobile_no, state),
    )
    conn.commit()
    conn.close()


def fetch_applications(limit=10):
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        """
        SELECT name, email, mobile_no, state, submitted_at
        FROM applications
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    ).fetchall()
    conn.close()
    return rows


init_db()

st.title("Job Application Form")

with st.form("job_application_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    mobile_no = st.text_input("Mobile Number")
    state = st.selectbox(
        "State",
        [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
            "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
            "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
            "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ],
    )

    submitted = st.form_submit_button("Submit Application")

if submitted:
    if not name or not email or not mobile_no:
        st.warning("Please fill in Name, Email, and Mobile Number.")
    else:
        save_application(name, email, mobile_no, state)
        st.success("Application submitted successfully!")
        st.write("Saved data:")
        st.write({
            "Name": name,
            "Email": email,
            "Mobile No": mobile_no,
            "State": state,
        })

st.subheader("Recent Applications")
rows = fetch_applications(10)
if rows:
    st.table(
        [
            {
                "Name": row[0],
                "Email": row[1],
                "Mobile No": row[2],
                "State": row[3],
                "Submitted At": row[4],
            }
            for row in rows
        ]
    )
else:
    st.info("No applications submitted yet.")
