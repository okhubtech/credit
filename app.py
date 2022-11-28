import streamlit as st
import pandas as pd
import base64
import pickle
from PIL import Image
from sklearn.neural_network import MLPClassifier
import tensorflow as tf
image = Image.open(r"C:\Users\PHIIL\Pictures\fuoye.jpg")
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
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
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT, email TEXT)')


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



def main():
	"""FRAUD CREDIT CARD DETECTION WEB APPLICATION"""

	st.title("FRAUD CREDIT CARD DETECTION")
	st.write("""
	
	By **Obijole OluwaSegun Michael **
	
	Supervised by **Dr Mrs. ESAN**
	# COMPUTER ENGINEERING""")

	col1, col2, col3 = st.beta_columns([1,8,1])
	with col1:
		st.write('')
	with col2:
		st.image(image, caption='Federal university Oye Ekiti', width=200)
	with col3:
		st.write('')
	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")
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
			
		
				st.sidebar.header("User Input Parameters")

				def user_input():
					t = st.sidebar.slider('Time', 0, 172792, 100)
					a = st.sidebar.slider('Amount', 0.0, 25691.16, 100.0)
					v1 = st.sidebar.slider('V1', -5.640751e+01, 2.454930e+00, -9.203734e-01)
					v2 = st.sidebar.slider('V2', -7.271573e+01, 2.205773e+01, -5.985499e-01)
					v3 = st.sidebar.slider('V3', -4.832559e+01, 9.382558e+00, -8.903648e-01)
					v4 = st.sidebar.slider('V4', -5.683171e+00, 1.687534e+01, -8.486401e-01)
					v5 = st.sidebar.slider('V5', -1.137433e+02, 3.480167e+01, -6.915971e-01)
					v6 = st.sidebar.slider('V6', -2.616051e+01, 7.330163e+01, -7.682956e-01)
					v7 = st.sidebar.slider('V7', -4.355724e+01, 1.205895e+02, -5.540759e-01)
					v8 = st.sidebar.slider('V8', -7.321672e+01, 2.000721e+01, -2.086297e-01)
					v9 = st.sidebar.slider('V9', -1.343407e+01, 1.559499e+01, -6.430976e-01)
					v10 = st.sidebar.slider('V10', -2.458826e+01, 2.374514e+01, -5.354257e-01)
					v11 = st.sidebar.slider('V11', -4.797473e+00, 1.201891e+01, -7.624942e-01)
					v12 = st.sidebar.slider('V12', -1.868371e+01, 7.848392e+00, -4.055715e-01)
					v13 = st.sidebar.slider('V13', -5.791881e+00, 7.126883e+00, -6.485393e-01)
					v14 = st.sidebar.slider('V14', -1.921433e+01, 1.052677e+01, -4.255740e-01)
					v15 = st.sidebar.slider('V15', -4.498945e+00, 8.877742e+00, -5.828843e-01)
					v16 = st.sidebar.slider('V16', -1.412985e+01, 1.731511e+01, -4.680368e-01)
					v17 = st.sidebar.slider('V17', -2.516280e+01, 9.253526e+00, -4.837483e-01)
					v18 = st.sidebar.slider('V18', -9.498746e+00, 5.041069e+00, -4.988498e-01)
					v19 = st.sidebar.slider('V19', -7.213527e+00, 5.591971e+00, -4.562989e-01)
					v20 = st.sidebar.slider('V20', -5.449772e+01, 3.942090e+01, -2.117214e-01)
					v21 = st.sidebar.slider('V21', -3.483038e+01, 2.720284e+01, -2.283949e-01)
					v22 = st.sidebar.slider('V22', -1.093314e+01, 1.050309e+01, -5.423504e-01)
					v23 = st.sidebar.slider('V23', -4.480774e+01, 2.252841e+01, -1.618463e-01)
					v24 = st.sidebar.slider('V24', -2.836627e+00, 4.584549e+00, -2.836627e+00)
					v25 = st.sidebar.slider('V25', -1.029540e+01, 7.519589e+00, -3.171451e-01)
					v26 = st.sidebar.slider('V26', -2.604551e+00, 3.517346e+00, -2.604551e+00)
					v27 = st.sidebar.slider('V27', -2.256568e+01, 3.161220e+01, -7.083953e-02)
					v28 = st.sidebar.slider('V28', -1.543008e+01, 3.384781e+01, -1.543008e+01)
#'Time': t,
					data = { 'V1': v1, 'V2': v2,'V3': v3, 'V4': v4, 'V5': v5, 'V6': v6, 
					'V7': v7, 'V8': v8, 'V9': v9, 'V10': v10, 'V11': v11, 'V12': v12, 'V13': v13,
					'V14': v14, 'V15': v15, 'V16': v16, 'V17': v17, 'V18': v18, 'V19': v19, 'V20': v20, 
					'V21': v21, 'V22': v22,'V23': v23, 'V24': v24, 'V25': v25, 'V26': v26,'V27': v27,
					 'V28': v28, 'Amount': a}
					features= pd.DataFrame(data, index=[0])
					return features
				df_new = user_input()
				st.subheader('User Input Parameters')
				st.write(df_new)
				df = pd.read_csv(r"C:\Users\PHIIL\Desktop\FINAL PROJECTS\segmore\creditcard.csv")
				#st.write(df.head())
				load = pickle.load(open(r"model_credit",'rb'))
				output=load.predict(df_new)
				prob = load.predict_proba(df_new)
				st.write(output)
				if output==1:
					st.write("Fraud detected")
				else: st.write("No fraud")
				st.write(prob)

			else:
				st.warning("Incorrect Username/Password")


#C:/ProgramData/Anaconda3/Scripts/activate

if __name__ == '__main__':
	main()