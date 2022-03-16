import sqlite3
import streamlit as st

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
    

