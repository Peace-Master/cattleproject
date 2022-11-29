import streamlit as st 
import pandas as pd
import random
from streamlit_option_menu import option_menu
import cv2

from playsound import playsound
import numpy as np
import pickle  #to load a saved model
from datetime import datetime, timedelta
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts

import register as rr
from PIL import Image
from pathlib import Path
import sqlite3
from sqlite3 import Connection
#import detector as dr
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import alert as al
import speech as sp


hiden_menu_style="""<style>#MainMenu{visibility:hidden}
footer{visibility:hidden}</style> """
st.markdown(hiden_menu_style,unsafe_allow_html=True)

URI_SQLITE_DB = "finaldatabase.db"
def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect(URI_SQLITE_DB)
        cursor = sqliteConnection.cursor()
        st.write("Connected to Database")

        sql_select_query = """select * from test where platenumber = ?"""
        cursor.execute(sql_select_query, (str(id),))
        records = cursor.fetchall()
        sql_select_quer = """select * from test where platenumber = ?"""
        cursor.execute(sql_select_quer, (str(id),))
        clear=cursor.fetchall()

        sql_select_querrr = """select issues from test where platenumber = ?"""
        cursor.execute(sql_select_querrr, (str(id),))
        issues=cursor.fetchall()
        
        st.write(records)
        if records[0][8]=="infected":
            al.alarm()
            ("infected")
            #sp.blacklisted()
            playsound('blacklist.mp3')
            st.title("Comment on patient:  ")
            st.info(records[0][9])
        elif clear[0][8]=="clear":
            st.write("Cleared")
            #sp.clear()
            #playsound('clear.mp3')
            st.title("Comment on patient:  ")
            st.info(records[0][9])
        elif len(records)==0:
            #sp.notreg()
            st.write("Not registered")
            playsound('notreg.mp3')
            st.title(".............. ")
            st.info(records[0][9])
        cursor.close()
        

    except sqlite3.Error as error:
        st.write("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            st.write("The Database connection is closed")


def get_vstatus(vid,conn: Connection):
    #result=str(result)
    df = "SELECT status FROM test where wardnumber=vid"
    if df=='blacklisted':
        al.alarm()
        st.write("Infected")
def main():
    
    conn = rr.get_connection(URI_SQLITE_DB)
    rr.init_db(conn)
    with st.sidebar:
        selected=option_menu(menu_title=None,options=["Institution","Aboutpage","Contact"])
        if selected=="Institution":
            st.write("Contact Us")
        if selected=="Contact":
            st.write("077777777777")
        if selected=="Aboutpage":
                st.write("The system was mainly developed to .................................................................................................................")

    FRAME_WINDOW = st.image([])
    selected=option_menu(menu_title=None,options=["Home","Covid-19 Reports","Covid19 Ward Report","Registered Patients","Register Patients"], orientation="horizontal")
    if selected=="Home":
        #playsound('welcome.mp3')
        st.header("Welcome To The Cattle Data Collection System")
        
         #opening the image
        
        image = Image.open('download (1).jpeg')
        
        #displaying the image on streamlit app
        im1,im2=st.columns([1,1])
        
        data=pd.read_csv('world_health_statistics_indicators_zwe.csv')
        n=random.randint(9,20)
        test = data.astype(str)
        df=test
        st.markdown("### Cattle disease indicators Data View")
        st.bar_chart(test )
        
    
    if selected=="Cattle Reports":
         
        today = datetime.today().strftime('%Y-%m-%d')
        data=pd.read_excel('june-2017-final-aps-maori-farms-tables-3.xlsx')
        n=random.randint(9,20)
        test = data.astype(str)
        df=test
        st.markdown("### Detailed Data View")
        st.line_chart(test )
        st.dataframe(df)
                        
                

                                   
                     
                                    
    if selected=="Cattle Ward Report":
            st.write("click button on the sidebar to view infected patients.")
            rr.run_inspection(conn)

    if selected=="Registered Patients":
        st.header("Registered Patients ")
        st.dataframe(rr.get_data(conn))
        
        select=option_menu(menu_title="Click to Edit Information Above",options=["","Update Patient","Delete information","Register Patients"])
        if select=="Update Patient":
            st.header("Update patient Infor ")
            s1,s2=st.columns(2)
            a= s1.text_input("Name")
            Name =str(a)
            input2 = s2.text_input("Surname")
            surname=str(input2)
            input3 =  s1.text_input("ID")
            ID=str(input3)
            input9 =  s2.text_input("Gender")
            Gender=str(input9)
            input4 =  s1.text_input("Address Nmber")
            Address=str(input4)
            input5 =  s2.text_input("Ward Nmber")
            Vno=str(input5)
            input6 = s1.text_input("VehicleType")
            Vtype=str(input6)
            input7 =  s2.text_input("Regdate")
            Regdate=str(input7)
                
            input10 =  st.text_input("Patient Status")
            status=str(input10)
                
            if st.button("Save information"):
                conn.execute(f"UPDATE test SET name='{Name}',address='{Address}',surname='{surname}',id='{ID}',gender='{Gender}',vehicletype='{Vtype}',status='{status}'WHERE platenumber= '{Vno}'")
                conn.commit()
        if select=="Delete information":
            s1,s2=st.columns(2)
            inputdel =  s1.text_input("Ward Nmber")
            Vno=str(inputdel)
            if s2.button("delete"):
                conn.execute(f"DELETE FROM test WHERE platenumber= '{Vno}'")
                conn.commit()
        if select=="Register Vehicle":
                st.header("Patient Registration ")
                rr.build_reg(conn)
        
            

        
    if selected=="Register Patients":
        st.header("Patient Registration ")
        rr.build_reg(conn)















        
          
