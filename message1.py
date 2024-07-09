from pywhatkit import sendwhatmsg_instantly as sendwhatmsg
import pandas as pd
from datetime import date, datetime

data = pd.read_csv("sample.csv")

if len(data.columns) != 2:
    print("Please check the file. It should have 2 columns.")
    exit()

today = date.today()
today = today.strftime('%d %b %Y')

first_day = date.today().replace(day=1)
first_day = first_day.strftime('%d %b %Y')

for index, row in data.iterrows():
    name = str(row['Name'])
    message= """
Dear """ + name + """,
SOLES IS BACK !!! ✨ 
We're excited to announce the grand launch of our new store at Bangalore's favourite shopping destination- Commercial Street. 🎆 
Come visit us at our new store and enjoy your  shopping experience with our latest collection of  women's footwear
"""
       
    phone_no = "+91" + str(row['Phone number'])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    current_time = [int(i) for i in current_time]

    sendwhatmsg(phone_no, message, tab_close=True, wait_time=20)

    print(message)
    print("---------------------------------------------------")
print("All messages sent successfully!")
