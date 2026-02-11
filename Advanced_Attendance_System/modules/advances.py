
import streamlit as st
import pandas as pd
from database import get_connection
from datetime import date

def show():
    st.header("💵 Advance Management")
    conn = get_connection()
    cursor = conn.cursor()

    emp_df = pd.read_sql("SELECT * FROM employees", conn)
    if emp_df.empty:
        st.warning("Add employees first.")
        return

    emp_list = emp_df["name"].tolist()
    selected_emp = st.selectbox("Select Employee", emp_list)
    amount = st.number_input("Advance Amount", min_value=0.0)

    if st.button("Give Advance"):
        emp_id = emp_df[emp_df["name"] == selected_emp]["id"].values[0]
        cursor.execute("INSERT INTO advances (emp_id, amount, date) VALUES (?, ?, ?)",
                       (emp_id, amount, str(date.today())))
        conn.commit()
        st.success("Advance Recorded Successfully")
        st.rerun()

    df = pd.read_sql("SELECT * FROM advances", conn)
    st.dataframe(df, use_container_width=True)
    conn.close()
