import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
import streamlit as st
#import detector as dr


URI_SQLITE_DB = "finaldatabase.db"


def main():
    st.title("Register a Patient")
    st.markdown("Enter data in database from sidebar,")
    
    conn = get_connection(URI_SQLITE_DB)
    init_db(conn)

    build_reg(conn)
    display_data(conn)
    run_calculator(conn)
    run_inspection(conn)


def init_db(conn: Connection):
    conn.execute(
        """CREATE TABLE IF NOT EXISTS test
            (
                name varchar(80),
                surname varchar(80),
                id varchar(80),
                address varchar(80),
                wardnumber varchar(80),

                patienttype varchar(80),
                regdate varchar(80),

                gender varchar(80),
                status varchar(80),
                issues varchar(80)
            );"""
    )
    conn.commit()


def build_reg(conn: Connection):
    st.sidebar.header("Registration")
    #s1,s2=st.columns(2)
    a= st.text_input("Name")
    name =str(a)
    input2 = st.text_input("Surname")
    surname=str(input2)
    input3 =  st.text_input("ID")
    ID=str(input3)
    input9 =  st.text_input("Gender")
    Gender=str(input9)
    input4 =  st.text_input("Address Nmber")
    Address=str(input4)
    input5 =  st.text_input("Ward Nmber")
    Vno=str(input5)
    input6 = st.text_input("PatientType")
    Vtype=str(input6)
    input7 =  st.text_input("Regdate")
    Regdate=str(input7)
    
    input10 =  st.text_input("Patient Status")
    status=str(input10)
    input11 =  st.text_input("Ward Comments")
    issue=str(input11)
    if st.button("Save to database"):
        conn.execute(f"INSERT INTO test (name, surname,id, address,wardnumber, patienttype,regdate,gender,status,issues) VALUES ('{name}', '{surname}','{ID}', '{Address}' , '{Vno}' , '{Vtype}', '{Regdate}' , '{Gender}', '{status}','{issue}')")
        conn.commit()


def display_data(conn: Connection):
    if st.checkbox("Display data in sqlite databse"):
        st.dataframe(get_data(conn))


def run_calculator(conn: Connection):
    #if st.sidebar.button("Black List"):
    st.info("Run your function")
    df = get_data(conn)
    return df
def run_inspection(conn: Connection):
    #if st.sidebar.button("inspect"):
    st.info("Infected Patients")
    dfinf = get_vinfo(conn)
    st.write(dfinf)


def get_data(conn: Connection):
    df = pd.read_sql("SELECT * FROM test", con=conn)
    return df

def get_vinfo(conn: Connection):
    #result=str(result)
    df = pd.read_sql("SELECT * FROM test where status='blacklisted'", con=conn)
    
    return df

def get_vstatus(vid,conn: Connection):
    #result=str(result)
    df = "SELECT status FROM test where platenumber=vid"
    if df=='blacklisted':
        st.write("Black Listed")

@st.cache(hash_funcs={Connection: id})
def get_connection(path: str):
    """Put the connection in cache to reuse if path does not change between Streamlit reruns.
    NB : https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa
    """
    return sqlite3.connect(path, check_same_thread=False)


if __name__ == "__main__":
    main()
