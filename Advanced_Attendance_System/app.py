
import streamlit as st
from modules import dashboard, employees, attendance, payroll, advances

st.set_page_config(page_title="Advanced Attendance System", layout="wide")

st.title("🚀 Distributor Business Management System")

menu = st.sidebar.radio("Navigation", ["Dashboard", "Employees", "Attendance", "Payroll", "Advances"])

if menu == "Dashboard":
    dashboard.show()
elif menu == "Employees":
    employees.show()
elif menu == "Attendance":
    attendance.show()
elif menu == "Payroll":
    payroll.show()
elif menu == "Advances":
    advances.show()
