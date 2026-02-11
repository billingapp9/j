
import streamlit as st
import pandas as pd
from database import get_connection
from datetime import datetime, date

def show():
    st.header("🕒 Attendance Marking")
    conn = get_connection()
    cursor = conn.cursor()

    emp_df = pd.read_sql("SELECT * FROM employees", conn)

    if emp_df.empty:
        st.warning("Please add employees first.")
        return

    emp_list = emp_df["name"].tolist()
    selected_emp = st.selectbox("Select Employee", emp_list)

    col1, col2 = st.columns(2)
    in_time = col1.time_input("In Time")
    out_time = col2.time_input("Out Time")

    if st.button("Mark Attendance"):
        emp_id = emp_df[emp_df["name"] == selected_emp]["id"].values[0]
        today = str(date.today())

        in_dt = datetime.combine(date.today(), in_time)
        out_dt = datetime.combine(date.today(), out_time)
        hours = (out_dt - in_dt).total_seconds() / 3600

        if hours >= 8:
            status = "Present"
        elif hours >= 4:
            status = "Half Day"
        else:
            status = "Absent"

        overtime = max(0, hours - 8)

        cursor.execute("""
            INSERT INTO attendance (emp_id, date, in_time, out_time, working_hours, status, overtime)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (emp_id, today, str(in_time), str(out_time), hours, status, overtime))

        conn.commit()
        st.success("Attendance Marked Successfully")
        st.rerun()

    today_df = pd.read_sql(f"SELECT * FROM attendance WHERE date='{date.today()}'", conn)
    st.dataframe(today_df, use_container_width=True)
    conn.close()
