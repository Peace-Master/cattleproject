import streamlit as st
import pandas as pd
from PIL import Image
import pandas as pd
import random
from streamlit_option_menu import option_menu
#import D_tree as dt

from datetime import datetime
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import flickrapi
import random
from dotenv import load_dotenv
import os
import urllib
import folium

import register as rr
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib


import numpy as np # Scientific computing packages - Array
from pandas import Series, DataFrame
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.model_selection import train_test_split


data = pd.read_csv('symptoms.csv')
data.describe()

data.head()

clf = tree.DecisionTreeClassifier()
train, test = train_test_split(data, test_size = 0.15)


attributes = ["Fever", "Bilsters in the mouth and on feet", "Drop in milk production", "Weight loss", "Loss of appetite", "blisters on teats", "Lameness", "intermittent fever", "anaemia", "oedema", "lacrimation", "Lymph nodes", "Abortion", "Infertility", "emaciation", "Calf dropping the head", "Dull and depressed", "High temperature", "Heavy breathing", "Nasal discharge", "Coughing", "Stillbirth", "Weak calf born", "Retention of fetal membranes", "infection in the membranes", "Swollen testicles in bulls", "Watery Milk", "heat", "Swollen udder", "Pain in udder", "Hardness of the teats", "reduction in milk ", "anorexia", "corneal opacity", "diarrhoea", "milky eye and white gums"]
x_train = train[attributes]
y_train = train["Diseases"]

x_test = test[attributes]
y_test = test["Diseases"]


clf = clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

score = accuracy_score(y_test, y_pred)








def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

URI_SQLITE_DB = "finaldatabase.db"
con = sqlite3.connect(URI_SQLITE_DB)
# DB  Functions

st.set_page_config(page_icon="",page_title="Cattle disease diagnostics System",layout="wide",initial_sidebar_state="expanded")
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


st.sidebar.title("Cattle disease diagnosis System")
Image.open('download (2).png').convert('RGB').save('new.jpeg')
image =Image.open('new.jpeg')

st.sidebar.image(image, caption='cattle disease diagnosis System')

def load_data():
    """ Load the cleaned data with latitudes, longitudes & timestamps """
    travel_log = pd.read_csv("clean_data.csv")
    travel_log["date"] = pd.to_datetime(travel_log["ts"])
    return travel_log
def main():
	"""Simple Login App"""

	st.title("Cattle disease diagnostics System")

	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		#st.subheader("Home")
		 #playsound('welcome.mp3')
                                   st.subheader("Welcome To Cattle disease diagnostics System")
                                   data = load_data()
                                   #st.map(data)
                                   
                                   data=pd.read_csv('symptoms.csv')
                                   n=random.randint(9,20)
                                   test = data.astype(str)
                                   df=test
                                   st.markdown("### symptoms Data View")
                                   st.bar_chart(test )
                                   #map_heatmap = folium.Map(location=[48.1351, 11.5820], zoom_start=11)
                                   #s1,s2,s3,s4=st.beta_columns(4)
                                   #s1.checkbox("Abortion")
                                   #s2.checkbox("mouth and feet blisters")
                                   #s3.checkbox("calf dropping the head")
                                   #s4.checkbox("coughing")
                                   #s1.checkbox("dropping in milk production")
                                   #s2.checkbox("dull and depressed")
                                   #s3.checkbox("fever")
                                   #s4.checkbox("teats harden")
                                   #s1.checkbox("heavy breathing")
                                   #s2.checkbox("high temperature")
                                   #s3.checkbox("infertility")
                                   #s4.checkbox("lameness")
                                   #s1.checkbox("loss of appetite")

                                   #s1.checkbox("lymph nodes")
                                   #s2.checkbox("Nasal discharge")
                                   #s3.checkbox("udder pain")
                                   #s4.checkbox("retention of fetal membranes")
                                   #s1.checkbox("stillbirth")
                                   #s2.checkbox("Swollen balls")
                                   #s3.checkbox("swollen udder")
                                   #s4.checkbox("Watery Milk")
                                   #s1.checkbox("Weak calf born")
                                   #s2.checkbox("weight loss")
                                   #s3.checkbox("anaemia")
                                   #s4.checkbox("anorexia")
                                   #s1.checkbox("blisters on teats")

                                   #s2.checkbox("comeal opacity")
                                   #s3.checkbox("diahorea")
                                   #s4.checkbox("ti34k")
                                   dataup=st.file_uploader("upload a csv file",type=["csv"])
                                   if dataup is not None:
                                           #st.write(dt.predict(data))
                                           data = pd.read_csv(dataup)
                                           X = data[attributes]
                                            #Y = data.Diseases

                                           iris_data = DataFrame(X, columns=["Fever", "Bilsters in the mouth and on feet", "Drop in milk production", "Weight loss", "Loss of appetite", "blisters on teats", "Lameness", "intermittent fever", "anaemia", "oedema", "lacrimation", "Lymph nodes", "Abortion", "Infertility","emaciation", "Calf dropping the head", "Dull and depressed", "High temperature", "Heavy breathing", "Nasal discharge", "Coughing", "Stillbirth", "Weak calf born", "Retention of fetal membranes", "infection in the membranes", "Swollen testicles in bulls", "Watery Milk", "heat", "Swollen udder", "Pain in udder", "Hardness of the teats", "reduction in milk ", "anorexia", "corneal opacity", "diarrhoea", "milky eye and white gums"])
                                            #iris_target = DataFrame(Y, columns=["Diseases"])

                                           predicted = clf.predict(iris_data)
                                           st.write(predicted)

                                            #expected = iris_target
                                            # print(metrics.accuracy_score(expected, predicted)*100, "%")
                                           #return predicted
                                           

                                   #s5,s6,s7,s8=st.beta_columns(4)
                                   #s6.button("Diagonise")
                                   
                                                                   









                                   

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Patient","View Patient Information","Profiles"])
				if task == "Add Patient":
					st.subheader("Patient Registration ")
					rr.build_reg(con)

				elif task == "View Patient Information":
					st.subheader("Registered Patients")
					rr.display_data(con)
					


















					
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")

def predict(data):
    data = pd.read_csv(data)

    X = data[attributes]
    #Y = data.Diseases

    iris_data = DataFrame(X, columns=["Fever", "Bilsters in the mouth and on feet", "Drop in milk production", "Weight loss", "Loss of appetite", "blisters on teats", "Lameness", "intermittent fever", "anaemia", "oedema", "lacrimation", "Lymph nodes", "Abortion", "Infertility","emaciation", "Calf dropping the head", "Dull and depressed", "High temperature", "Heavy breathing", "Nasal discharge", "Coughing", "Stillbirth", "Weak calf born", "Retention of fetal membranes", "infection in the membranes", "Swollen testicles in bulls", "Watery Milk", "heat", "Swollen udder", "Pain in udder", "Hardness of the teats", "reduction in milk ", "anorexia", "corneal opacity", "diarrhoea", "milky eye and white gums"])
    #iris_target = DataFrame(Y, columns=["Diseases"])

    predicted = clf.predict(iris_data)

    #expected = iris_target
    # print(metrics.accuracy_score(expected, predicted)*100, "%")
    return predicted
#print(predict())


if __name__ == '__main__':
	main()
