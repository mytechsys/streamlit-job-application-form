# Streamlit Job Application Form

A simple Streamlit app that collects job application details and saves them in a local SQLite database.

## Fields collected

- Full Name
- Email Address
- Mobile Number
- State

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## What it stores

The app saves every submission in a SQLite database file named:

```text
job_applications.db
```

## Deploy on Streamlit Cloud

1. Push this repo to GitHub.
2. Open Streamlit Cloud.
3. Connect the repo and choose `app.py`.
4. Deploy.

Note: on Streamlit Cloud, database files are not always durable across restarts. For production data persistence, use a hosted database such as PostgreSQL, Supabase, or Firebase.
