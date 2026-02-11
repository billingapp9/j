
import streamlit as st
import pandas as pd
from database import get_connection

def show():
    st.header("💰 Payroll System")
    conn = get_connection()

    emp_df = pd.read_sql("SELECT * FROM employees", conn)
    att_df = pd.read_sql("SELECT * FROM attendance", conn)
    adv_df = pd.read_sql("SELECT * FROM advances", conn)

    if emp_df.empty:
        st.warning("Add employees first.")
        return

    for _, emp in emp_df.iterrows():
        emp_id = emp["id"]
        salary = emp["salary"]

        emp_att = att_df[att_df["emp_id"] == emp_id]
        present_days = len(emp_att[emp_att["status"] == "Present"])
        half_days = len(emp_att[emp_att["status"] == "Half Day"])
        earned_days = present_days + (half_days * 0.5)

        per_day_salary = salary / 30 if salary else 0
        earned_salary = per_day_salary * earned_days

        emp_adv = adv_df[adv_df["emp_id"] == emp_id]["amount"].sum()
        final_salary = earned_salary - (emp_adv if emp_adv else 0)

        st.subheader(emp["name"])
        st.write(f"Earned Days: {earned_days}")
        st.write(f"Earned Salary: ₹{earned_salary:.2f}")
        st.write(f"Advance Deduction: ₹{emp_adv if emp_adv else 0}")
        st.write(f"Final Salary: ₹{final_salary:.2f}")
        st.markdown("---")

    conn.close()
