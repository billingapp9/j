
import streamlit as st
import pandas as pd
from database import get_connection
from datetime import date

def show():
    st.header("📊 Live Dashboard")
    conn = get_connection()

    emp_df = pd.read_sql("SELECT * FROM employees", conn)
    att_df = pd.read_sql("SELECT * FROM attendance", conn)

    today = str(date.today())
    today_att = att_df[att_df["date"] == today]

    total_emp = len(emp_df)
    present = len(today_att[today_att["status"] == "Present"])
    absent = total_emp - present

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employees", total_emp)
    col2.metric("Today Present", present)
    col3.metric("Today Absent", absent)

    if total_emp > 0:
        st.bar_chart(pd.DataFrame({"Count": [present, absent]}, index=["Present", "Absent"]))

    conn.close()
