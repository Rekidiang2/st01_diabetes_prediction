import sqlite3
import streamlit as st
import pandas as pd

# CREATE DATABASE

def create_db():
    # create data base
    # conn = sqlite3.connect(':memory:')  #temporary data base
    conn = sqlite3.connect('diabetes_result.db')
    c = conn.cursor()  # create a cursor
    # data type : NULL, INTEGER, REAL, TEXT, BLOB
    c.execute("""CREATE TABLE patients(
    PatientID text,
    Name text, 
    Age text, 
    Gender text,
    Pregnancies integer, 
    Glucose real,
    Insulin real,
    BMI real,
    BP real,
    DPF real,
    SkinTickness integer,
    Result text
    )""")

    # commit our command
    conn.commit()
    # close connection
    conn.close()


def insert_data(data_dict, result, df):
    conn = sqlite3.connect('diabetes_result.db')
    c = conn.cursor()  # create a cursor
    # FOR DATABASE
    patientID = str(data_dict['patientID'])
    name = data_dict['name']
    age = data_dict['age']
    gender = data_dict['gender']
    preg = data_dict['preg']
    gluco = data_dict['gluco']
    bp = data_dict['bp']
    skin = data_dict['skin']
    insu = data_dict['insu']
    bmi = data_dict['bmi']
    dpf = data_dict['dpf']

    param = (patientID, name, age, gender, preg, gluco, bp, skin, insu, bmi, dpf, result)
    c.execute("INSERT INTO patients VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", param)
    st.write("Result Details : ")
    st.table(df)

    # commit our command
    conn.commit()
    # close connection
    conn.close()

def retrive_data():
    # Create your connection.
    cnx = sqlite3.connect('diabetes_result.db')

    df_all = pd.read_sql_query("SELECT * FROM patients", cnx)
    df_neg = pd.read_sql_query("SELECT * FROM patients WHERE Result = 'Negative'", cnx)
    df_pos = pd.read_sql_query("SELECT * FROM patients WHERE Result = 'Positive'", cnx)
    menu = ["All Result", "Positive Result", "Negative Result"]
    choice = st.radio("Menu", menu)

    if choice == "All Result":
        st.header("All Result")
        st.dataframe(df_all)
    elif choice == "Positive Result":
        st.header("Positive Result")
        st.dataframe(df_pos)
    elif choice == "Negative Result":
        st.header("Negative Result")
        st.dataframe(df_neg)

    

