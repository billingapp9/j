
import streamlit as st
import pandas as pd
from database import get_connection

def show():
    st.header("👥 Employee Management")
    conn = get_connection()
    cursor = conn.cursor()

    with st.form("Add Employee"):
        name = st.text_input("Employee Name")
        role = st.text_input("Role")
        dept = st.text_input("Department")
        salary = st.number_input("Monthly Salary", min_value=0.0)
        submit = st.form_submit_button("Add Employee")

        if submit:
            cursor.execute("INSERT INTO employees (name, role, department, salary) VALUES (?, ?, ?, ?)",
                           (name, role, dept, salary))
            conn.commit()
            st.success("Employee Added Successfully")
            st.rerun()

    df = pd.read_sql("SELECT * FROM employees", conn)
    st.dataframe(df, use_container_width=True)
    conn.close()
